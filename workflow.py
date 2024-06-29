#!/usr/bin/python3
import sys
import jsondb
import json
import logging

def wf_update_flow(data, args):
    # no action for inactive workflow
    if data['status'] == 'rejected' or data['status'] == 'closed':
        return(data)
    
    flow = data['flow']
    if flow['pos'] >= len(flow['flow']):
        logging.critical(f'workflow: Out of range: {flow}')
        print('aborted')
        exit(1)

    cursor = flow['flow'][flow['pos']]
    action = cursor['action']
    if action == 'close':
        print(action)
        data['status'] = 'closed'
        if 'message' in flow:
            print(flow['message'])
        # todo: report to stakeholders
    elif action == 'approval' or action == 'run':
        print(action)
        pic = cursor['person_in_charge']
        actor = args['actor']
        if pic == actor:
            flow['pos'] = flow['pos'] + 1
            logging.info(f'workflow: successfully approved/ran: {flow}')
            if 'message' in flow:
                flow['message'].append(f'{actor}: {args["message"]}')
            else:
                flow['message'] = [f'{actor}: {args["message"]}']
        else:
            logging.warning(f'workflow: Invalid request for approval/run: {flow}, person_in_charge=pic, actor=actor')
    else:
        logging.critical(f'workflow: unexpected action: {flow}')
        print('aborted')
        exit(1)
        
    data['flow'] = flow 
    return(data)

def wf_list(db):
    for row in db.get('workflow'):
        print(row)
        
def wf_add(db, data):
    db.set('workflow', data)
    db.commit()
        
def wf_step_forward(db, tbl_id, dict_args):
    for row in db.getByID('workflow', tbl_id):
        row = wf_update_flow(row, dict_args)
        db.set('workflow', dataid=tbl_id, data=row)
        db.commit()
        
def wf_reject(db, tbl_id):
    for row in db.getByID('workflow', tbl_id):
        row['status'] = 'rejected'
        db.set('workflow', dataid=tbl_id, data=row)
        db.commit()

        # todo: report back to stakeholders.

def main():
    logging.basicConfig(filename="logs/workflow.log")
                        
    with jsondb.JsonDB('data/workflow.db') as db:
        db.create_table('workflow')
        db.commit()

        #print(wf_update_flow('{"pos": 0, "flow": [{}, {}]}'))
        #exit(1)

        flow = {'pos': 0, 'flow': [
            {'action': 'approval', 'person_in_charge': 'tf' },
            {'action': 'close'}
        ]} 
        data = {'name': 'abc', 'owner': 'abcd', 'flow': flow, 'type': 'payment', "status": "run"}
        wf_add(db, data)
        
        print('-' * 10)
        wf_list(db)
        print('-' * 10)
        wf_step_forward(db, 1, {'actor': 'tf', 'message': 'I did it.'})
        #print('-' * 10)
        #wf_reject(db, 5)
        
if __name__ == '__main__':
    sys.exit(main())
