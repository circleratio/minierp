#!/usr/bin/python3
import sys
import common
from logging import getLogger

class Wage:
    def __init__(self):
        self.db = common.DB().db
        self.logger = getLogger(__name__)

    def set(self, data):
        where = {'name': data['name'], 'fiscal_year': data['fiscal_year']}
        item = self.get(where)
        if item == None:
            self.logger.debug('set: New data')
            self.db.set('wage', data)
            self.db.commit()
        else:
            self.logger.debug('set: Update: {}'.format(item['id']))
            self.db.set('wage', data, dataid=item['id'])
            self.db.commit()
        
    def get(self, args):
        where = {'name': args['name'], 'fiscal_year': args['fiscal_year']}
        for row in self.db.get('wage', where):
            return(row)
        return(None)
        
    def dump(self):
        for row in self.db.get('wage'):
            print(row)
            
def main():
    db = Wage()
    db.dump()
    
if __name__ == '__main__':
    sys.exit(main())
