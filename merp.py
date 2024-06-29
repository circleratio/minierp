#!/usr/bin/python3
import people
import workflow
import sys
import logging
import json

def main():
    logging.basicConfig(filename="logs/merp.log")

    db_people = people.init()  
    db_workflow = workflow.init()

    arg = sys.argv
    l = len(arg)
    
    if l != 4:
        print('usage: merp type cmd {args in json}')
        exit(1)

    arg_json = json.loads(arg[3])
        
    if arg[1] == 'people':
        cmd_people(db_people, arg[2], arg_json)
    elif arg[1] == 'workflow':
        cmd_workflow(db_workflow, arg[2], arg_json)
    else:
        print('usage: merp type cmd {args in json format}')
        exit(1)
        
def cmd_people(db, cmd, arg):
    if cmd == 'list':
        people.list(db)
    elif cmd == 'add':
        people.add(db, arg)
    else:
        print(f'wrong command: {cmd}')

def cmd_workflow(db, cmd, arg):
    if cmd == 'list':
        workflow.list(db)
    elif cmd == 'add':
        workflow.add(db, arg)
    elif cmd == 'step_forward':
        wf_id = arg['id']
        wf_arg = arg['arg']
        workflow.step_forward(db, wf_id, wf_arg)
    elif cmd == 'reject':
        wf_id = arg['id']
        wf_arg = arg['arg']
        workflow.reject(db, wf_id, wf_arg)
        pass
    else:
        print(f'wrong command: {cmd}')
    
if __name__ == '__main__':
    sys.exit(main())
