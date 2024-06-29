import sqlite3
import json

class DB:
    def __init__(self, filePath=None):
        if filePath != None:
            self.filePath = filePath
        self.open(self.filePath)

    def open(self, filePath=None):
        if filePath != None:
            self.filePath = filePath
        self.connection = sqlite3.connect(self.filePath, isolation_level="DEFERRED")
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def fetch(self, sql):
        for row in self.cursor.execute(sql):
            yield row

    def query(self, sql):
        self.cursor.execute(sql)

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exctype, excvalue, traceback):
        self.close()


class JsonDB(DB):
    def queryString(self, sql, tablename, where, condition, column):
        if len(where) > 0:
            wstr = []
            for key in where.keys():
                if str(where[key]).find("%") != -1:
                    wstr.append(f"json_extract({column},'$.{key}') like '{where[key]}'")
                else:
                    if type(where[key]) == int:
                        wstr.append(f"json_extract({column},'$.{key}') = {where[key]}")
                    else:
                        wstr.append(f"json_extract({column},'$.{key}') = '{where[key]}'")
            wstr = f" {condition} ".join(wstr)
            sql = " where ".join((sql, wstr))
        return sql

    def get(self, tablename, where={}, condition="and", column="jsondata"):
        sql = f"""select json_set({column}, "$.id", id) from {tablename}"""
        sql = self.queryString(sql, tablename, where, condition, column)
        for row in self.fetch(sql):
            yield json.loads(row[0])
            
    def getByID(self, tablename, tbl_id, column="jsondata"):
        sql = f"""select json_set({column}, "$.id", id) from {tablename} where id = {tbl_id}"""
        for row in self.fetch(sql):
            yield json.loads(row[0])
            
    def count(self, tablename, where={}, condition="and", column="jsondata"):
        sql = f"select count(*) from {tablename}"
        sql = self.queryString(sql, tablename, where, condition, column)
        row = self.fetch(sql)
        return row.__next__()[0]
    
    def set(self, tablename, data={}, where={}, dataid="NULL", condition="and", column="jsondata"):
        if "id" in data:
            del data["id"]
        data = str(data).replace("'", '"')
        if len(where) == 0 and dataid == "NULL":
            sql = f"""replace into {tablename} values({dataid}, '{data}')"""
        else:
            sql = f"""replace into {tablename} select id, json_patch({column}, '{data}') """
            sql += f"""from {tablename}"""
        if dataid != "NULL":
            sql = " where ".join((sql, f"id={dataid}"))
        else:
            sql = self.queryString(sql, tablename, where, condition, column)
        self.query(sql)
    
    def create_table(self, tablename):
        sql = f"""create table if not exists "{tablename}" """
        sql += """("id" INTEGER, "jsondata" TEXT, PRIMARY KEY("id"))"""
        self.query(sql)
        self.commit()
