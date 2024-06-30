#!/usr/bin/python3
import sys
import jsondb

class People:
    def __init__(self):
        self.db = jsondb.JsonDB('data/people_and_organization.db')
        self.db.create_table('people')

    def list(self):
        for row in self.db.get('people'):
            print(row)

    def has(self, name):
        print(name)
        where = {'name': name}
        for row in self.db.get('people', where):
            return True
        return False

    def add(self, data):
        newid = data['name']
        if self.has(newid):
            print('already exists')
        else:
            self.db.set('people', data)
            self.db.commit()

def main():
    db_people = People()
    
if __name__ == '__main__':
    sys.exit(main())
