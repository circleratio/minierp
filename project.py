#!/usr/bin/python3
import sys
import people

class Project:
    def __init__(self):
        p = people.People()
        self.db = p.db

    def set(self, data):
        where = {'name': data['name'],
                 'fiscal_year': data['fiscal_year'],
                 'project': data['project']}
        item = self.get(where)
        if item == None:
            print('Project.set: New data')
            self.db.set('project', data)
            self.db.commit()
        else:
            print('Project.set: Update: {}'.format(item['id']))
            self.db.set('project', data, dataid=item['id'])
            self.db.commit()
        
    def get(self, args):
        where = {'name': args['name'],
                 'fiscal_year': args['fiscal_year'],
                 'project': args['project']}
        
        for row in self.db.get('project', where):
            return(row)
        return(None)

    def getByPerson(self, name, year):
        where = {'name': name,
                 'fiscal_year': year}
        l = []
        for row in self.db.get('project', where):
            l.append(row)
        return(l)
        
    def dump(self):
        for row in self.db.get('project'):
            print(row)
