#!/usr/bin/python3
import people, wage
import workflow
import sys
import logging
import json

def main():
    logging.basicConfig(filename="logs/merp.log")

    db_people = people.People()  
    db_wage = wage.Wage()  
    db_workflow = workflow.Workflow()

    arg = sys.argv
    if len(arg) != 4:
        print('Usage: merp type cmd {args in json}')
        exit(1)

    arg_json = json.loads(arg[3])
        
    if arg[1] == 'people':
        cmd_people(db_people, arg[2], arg_json)
    elif arg[1] == 'workflow':
        cmd_workflow(db_workflow, arg[2], arg_json)
    elif arg[1] == 'wage':
        cmd_wage(db_wage, arg[2], arg_json)
    else:
        print('Usage: merp type cmd {args in json format}')
        
    exit(1)
        
def cmd_people(db, cmd, arg):
    if cmd == 'list':
        db.list()
    elif cmd == 'add':
        db.add(arg)
    else:
        print(f'wrong command: {cmd}')

def cmd_wage(db, cmd, arg):
    if cmd == 'get':
        db.get(arg)
    elif cmd == 'set':
        db.set(arg)
    elif cmd == 'dump':
        db.dump()
    else:
        print(f'wrong command: {cmd}')
        
def cmd_workflow(db, cmd, arg):
    if cmd == 'list':
        db.list()
    elif cmd == 'add':
        db.add(arg)
    elif cmd == 'step_forward':
        wf_id = arg['id']
        wf_arg = arg['arg']
        db.step_forward(wf_id, wf_arg)
    elif cmd == 'reject':
        wf_id = arg['id']
        wf_arg = arg['arg']
        db.reject( wf_id, wf_arg)
        pass
    else:
        print(f'wrong command: {cmd}')
    
if __name__ == '__main__':
    sys.exit(main())
