#!/usr/bin/python3
import sys
import people

class Assignment:
    def __init__(self):
        p = people.People()
        self.db = p.db

    def set(self, data):
        where = {'name': data['name'],
                 'fiscal_year': data['fiscal_year'],
                 'project': data['project']}
        item = self.get(where)
        if item == None:
            print('Assignment.set: New data')
            self.db.set('assignment', data)
            self.db.commit()
        else:
            print('Assignment.set: Update: {}'.format(item['id']))
            self.db.set('assignment', data, dataid=item['id'])
            self.db.commit()
        
    def get(self, args):
        where = {'name': args['name'],
                 'fiscal_year': args['fiscal_year'],
                 'project': args['project']}
        
        for row in self.db.get('assignment', where):
            return(row)
        return(None)

    def getByPerson(self, name, year):
        where = {'name': name,
                 'fiscal_year': year}
        l = []
        for row in self.db.get('assignment', where):
            l.append(row)
        return(l)
        
    def getByProject(self, project, year):
        where = {'project': project,
                 'fiscal_year': year}
        l = []
        for row in self.db.get('assignment', where):
            l.append(row)
        return(l)
    
    def dump(self):
        for row in self.db.get('assignment'):
            print(row)
