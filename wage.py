#!/usr/bin/python3
import sys
import people

class Wage:
    def __init__(self):
        p = people.People()
        self.db = p.db

    def set(self, data):
        where = {'name': data['name'], 'fiscal_year': data['fiscal_year']}
        item = self.get(where)
        if item == None:
            print('Wage.set: New data')
            self.db.set('wage', data)
            self.db.commit()
        else:
            print('Wage.set: Update: {}'.format(item['id']))
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
