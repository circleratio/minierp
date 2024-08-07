#!/usr/bin/python3
import jsondb
from logging import getLogger, StreamHandler, DEBUG, basicConfig

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class DB(Singleton):
    def __init__(self):
        self.db = jsondb.JsonDB('base_data/base.db')
        self.db.create_table('common')
        self.db.create_table('people')
        self.db.create_table('wage')
        self.db.create_table('assignment')
        self.db.create_table('project')
        self.db.create_table('expense')
        self.db.commit()
        
        basicConfig(filename="operation_data/merp.log", level=DEBUG)
        
class Common:
    def __init__(self):
        self.db = DB().db
        self.logger = getLogger(__name__)

    def set(self, data):
        item = self.get('id')
        if item == None:
            self.db.set('common', data)
            self.db.commit()
        else:
            self.logger.debug(f'add: the common info already exists: id={item}')
            self.db.set('common', data, dataid=item)
            self.db.commit()
            
    def get(self, key):
        for row in self.db.get('common'):
            return(row[key])
        return(None)
