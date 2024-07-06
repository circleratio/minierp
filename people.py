#!/usr/bin/python3
import sys
import jsondb

class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
class People(Singleton):
    def __init__(self):
        self.db = jsondb.JsonDB('base_data/people_and_organization.db')
        self.db.create_table('people')
        self.db.create_table('wage')

    def list(self):
        for row in self.db.get('people'):
            print(row)

    def add(self, data):
        newid = data['name']
        if self.has(newid):
            print(f'People.add: the user already exists: {newid}')
        else:
            self.db.set('people', data)
            self.db.commit()
            
    def has(self, name):
        where = {'name': name}
        for row in self.db.get('people', where):
            return True
        return False

    def get(self, name):
        where = {'name': name}
        for row in self.db.get('people', where):
            print(row)
            return(yield row)
        return(None)
    
def main():
    db_people = People()
    
if __name__ == '__main__':
    sys.exit(main())
