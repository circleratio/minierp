#!/usr/bin/python3
import sys
import common
from logging import getLogger

class Expense:
    def __init__(self):
        self.db = common.DB().db
        self.logger = getLogger(__name__)

    def dump(self):
        for row in self.db.get('expense'):
            print(row)

    def set(self, data):
        where = {'name': data['name'],
                 'fiscal_year': data['fiscal_year'],
                 'project': data['project']}
        for item in self.get(where): 
            self.logger.debug('set: Update: id={}'.format(item['id']))
            self.db.set('expense', data, dataid=item['id'])
            self.db.commit()
            return(True)
        self.logger.debug('set: New data')
        self.db.set('expense', data)
        self.db.commit()
        return(True)

    def get(self, args):
        for row in self.db.get('expense', args):
            yield(row)
        return(None)

def main():
    db = Expense()
    db.dump()
    
if __name__ == '__main__':
    sys.exit(main())
