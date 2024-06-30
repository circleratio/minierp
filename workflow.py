#!/usr/bin/python3
import sys
import jsondb
import logging

class Workflow:
    def __init__(self):
        self.db = jsondb.JsonDB('base_data/workflow.db')
        self.db.create_table('workflow')

    def list(self):
        for row in self.db.get('workflow'):
            print(row)
        
    def add(self, data):
        self.db.set('workflow', data)
        self.db.commit()
        
    def update_flow(self, data, args):
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

    def step_forward(self, tbl_id, dict_args):
        for row in self.db.getByID('workflow', tbl_id):
            row = self.update_flow(row, dict_args)
            self.db.set('workflow', dataid=tbl_id, data=row)
            self.db.commit()
        
    def reject(self, tbl_id, dict_args):
        for row in self.db.getByID('workflow', tbl_id):
            row['status'] = 'rejected'
            self.db.set('workflow', dataid=tbl_id, data=row)
            self.db.commit()

        # todo: report back to stakeholders.

def main():
    workflow = Workflow()
    
if __name__ == '__main__':
    sys.exit(main())
