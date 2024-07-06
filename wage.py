#!/usr/bin/python3
import sys
import people

class Wage:
    def __init__(self):
        p = people.People()
        self.db = p.db

    def has(self, name, year):
        where = {'name': name, 'fiscal_year': year}
        for row in self.db.get('wage', where):
            return True
        return False
    
    def set(self, data):
        where = {'name': data['name'], 'fiscal_year': data['fiscal_year']}
        item = self.get(where)
        if item == None:
            print('new data')
            self.db.set('wage', data)
            self.db.commit()
        else:
            print('update: {}'.format(item['id']))
            self.db.set('wage', data, dataid=item['id'])
            self.db.commit()
        
    def get(self, args):
        if 'name' in args:  
            where = {'name': args['name']}
        else:
            return(None)
        
        for row in self.db.get('wage', where):
            return(row)
        
    def dump(self):
        for row in self.db.get('wage'):
            print(row)
