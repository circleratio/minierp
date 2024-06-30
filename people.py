#!/usr/bin/python3
import sys
import jsondb

def init():
    db = jsondb.JsonDB('data/people_and_organization.db')
    db.create_table('people')
    return(db)

def list(db):
    for row in db.get('people'):
        print(row)

def has(db, name):
    print(name)
    where = {'name': name}
    for row in db.get('people', where):
        return True
    return False

def add(db, data):
    newid = data['name']
    if has(db, newid):
        print('already exists')
    else:
        db.set('people', data)
        db.commit()

if __name__ == '__main__':
    arg_len = len(sys.argv) 
    if  arg_len < 2:
        usage_exit()
        
    cmd = sys.argv[1] 
    if cmd == 'list':
        list()
    elif cmd == 'find':
        if arg_len < 3:
            usage_exit()
        for user in sys.argv[2:]:
            find(user)
    else:
        usage_exit()
