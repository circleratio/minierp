#!/usr/bin/python3
import common
import people, wage, assignment, expense, project
import workflow
import sys
import logging
import json

def main():
    logging.basicConfig(filename="logs/merp.log")

    arg = sys.argv
    if len(arg) != 4:
        print('Usage: merp type cmd {args in json}')
        return(1)

    arg_json = json.loads(arg[3])

    func = {'people': cmd_people,
            'wage': cmd_wage,
            'assignment': cmd_assignment,
            'expense': cmd_expense,
            'workflow': cmd_workflow,
            'common': cmd_common,
            'project': cmd_project
            }
    
    if arg[1] in func:
        func[arg[1]](arg[2], arg_json)
    else:
        print(f'Wrong command: {arg[1]}')
        return(1)
    
    return(0)

def cmd_common(cmd, arg):
    db = common.Common()  
    if cmd == 'get':
        print(db.get(arg['company_name']))
    elif cmd == 'set':
        db.set(arg)
    elif cmd == 'dump':
        db.dump()
    else:
        print(f'People: wrong command: {cmd}')
        
def cmd_people(cmd, arg):
    db = people.People()  
    if cmd == 'get':
        print(db.get(arg['name']))
    elif cmd == 'set':
        db.set(arg)
    elif cmd == 'dump':
        db.dump()
    else:
        print(f'People: wrong command: {cmd}')

def cmd_project(cmd, arg):
    db = project.Project()  
    if cmd == 'get':
        print(db.get(arg))
    elif cmd == 'set':
        db.set(arg)
    elif cmd == 'dump':
        db.dump()
    else:
        print(f'Project: wrong command: {cmd}')
        
def cmd_wage(cmd, arg):
    db = wage.Wage()  
    if cmd == 'get':
        db.get(arg)
    elif cmd == 'set':
        db.set(arg)
    elif cmd == 'dump':
        db.dump()
    else:
        print(f'Wage: wrong command: {cmd}')
        
def cmd_expense(cmd, arg):
    db = expense.Expense()  
    if cmd == 'get':
        db.get(arg)
    elif cmd == 'set':
        db.set(arg)
    elif cmd == 'dump':
        db.dump()
    else:
        print(f'Wage: wrong command: {cmd}')
        
def cmd_assignment(cmd, arg):
    db = assignment.Assignment()  
    if cmd == 'get':
        db.get(arg)
    if cmd == 'getbyperson':
        l = db.getByPerson(arg['name'], arg['fiscal_year'])
        print(l)
    elif cmd == 'set':
        db.set(arg)
    elif cmd == 'dump':
        db.dump()
    else:
        print(f'Wage: wrong command: {cmd}')
        
def cmd_workflow(cmd, arg):
    db = workflow.Workflow()
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
        db.reject(wf_id, wf_arg)
        pass
    else:
        print(f'Workflow: wrong command: {cmd}')
    
if __name__ == '__main__':
    sys.exit(main())
