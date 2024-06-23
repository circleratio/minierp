#!/usr/bin/python3
import json
import sys

def list():
    with open('data/people.json', 'r') as f:
        person_dict = json.load(f)
        for p in person_dict:
            print(person_dict[p])

def find(id):
    with open('data/people.json', 'r') as f:
        person_dict = json.load(f)
        if id in person_dict:
            print(person_dict[id])

def usage_exit():
    print('Usage people.py [list|find] arg')
    exit(1)
    
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
