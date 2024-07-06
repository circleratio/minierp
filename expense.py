#!/usr/bin/python3
import sys
import common

class Expense:
    def __init__(self):
        self.db = common.DB().db

    def dump(self):
        for row in self.db.get('expense'):
            print(row)

    def set(self, data):
        where = {'name': data['name'],
                 'fiscal_year': data['fiscal_year'],
                 'project': data['project']}
        item = self.get(where)
        if item == None:
            print('Expense.set: New data')
            self.db.set('expense', data)
        else:
            print('Expense.set: Update: {}'.format(item['id']))
            self.db.set('expense', data, dataid=item['id'])
        self.db.commit()

    def get(self, args):
        where = {'name': args['name'],
                 'fiscal_year': args['fiscal_year'],
                 'project': args['project']}
        
        for row in self.db.get('expense', where):
            return(row)
        return(None)

def main():
    db = Expense()
    db.dump()
    
if __name__ == '__main__':
    sys.exit(main())
