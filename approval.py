#!/usr/bin/python3
import sys
import jsondb
import json
import logging

class Approval:
    def __init__(self):
        self.db = jsondb.JsonDB('data/approval.db')
        self.db.create_table('approval')

    def list(self):
        for row in self.db.get('approval'):
            print(row)
        
    def add(self, data):
        self.db.set('approval', data)
        self.db.commit()
        
def main():
    approval = Approval()
    approval.add({'test': 'test'})
    approval.list()
    
if __name__ == '__main__':
    sys.exit(main())
