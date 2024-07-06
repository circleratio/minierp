#!/usr/bin/python3
import sys
import common
from logging import getLogger

class People:
    def __init__(self):
        self.db = common.DB().db
        self.logger = getLogger(__name__)

    def dump(self):
        for row in self.db.get('people'):
            print(row)

    def set(self, data):
        item = self.get(data['name'])
        if item == None:
            self.db.set('people', data)
            self.db.commit()
        else:
            self.logger.debug('add: the user already exists: {} (id={})'.format(data['name'], item['id']))
            self.db.set('people', data, dataid=item['id'])
            self.db.commit()
            
    def has(self, name):
        where = {'name': name}
        for row in self.db.get('people', where):
            return True
        return False

    def get(self, name):
        where = {'name': name}
        for row in self.db.get('people', where):
            return(row)
        return(None)
    
def main():
    db = People()
    db.dump()
    
if __name__ == '__main__':
    sys.exit(main())
