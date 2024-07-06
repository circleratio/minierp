#!/usr/bin/python3
import jsondb

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class DB(Singleton):
    def __init__(self):
        self.db = jsondb.JsonDB('base_data/people_and_organization.db')
        self.db.create_table('people')
        self.db.create_table('wage')
        self.db.create_table('assignment')
        self.db.create_table('expense')
        self.db.commit()
