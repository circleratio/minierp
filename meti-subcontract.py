#!/usr/bin/python3
import work_payment
import json
import sys

def calc(filename):
    personnel_costs = 0
    expense = 0
    outsource = 0
    administrative_expenses = 0
    
    expense_travel = 0
    expense_meeting = 0
    expense_gratuity = 0
    expense_equipment = 0
    expense_rent = 0
    expense_consumables = 0
    expense_print = 0
    expense_assistant = 0
    expense_misc = 0

    with open(filename, 'r') as f:
        project_dict = json.load(f)
        name = project_dict['name']
        year = project_dict['year']
        month_start = project_dict['month_start']
        month_end = project_dict['month_end']
    
        print(project_dict)
        for m in project_dict['member']:
            personnel_costs += work_payment.sum_work(m, 'plan', year, month_start, month_end, name)

            for m in project_dict['expense']:
                expense_type = project_dict['expense'][m]['type'] 
                if expense_type == 'II.事業費':
                    expense = project_dict['expense'][m]['price']
                    subtype = project_dict['expense'][m]['subtype']
                    if subtype == '旅費':
                        expense_travel += expense
                    elif subtype == '会議費':
                        expense_meeting += expense
                    elif subtype == '謝金':
                        expense_gratuity += expense
                    elif subtype == '備品費':
                        expense_equipment += expense
                    elif subtype == '（借料及び損料）':
                        expense_rent += expense
                    elif subtype == '消耗品費':
                        expense_consumables += expense
                    elif subtype == '印刷製本費':
                        expense_print += expense
                    elif subtype == '補助員人件費':
                        expense_assistant += expense
                    elif subtype == 'その他諸経費':
                        expense_misc += expense
                    else:
                        print(f'Invalid expense type: {subtype}')
                        exit(1)
                elif expense_type == 'III.再委託・外注費':
                    outsource += project_dict['expense'][m]['price']

                administrative_expenses = (personnel_costs + expense) * project_dict['一般管理費率']
        
    print(f'I.人件費: {personnel_costs}')
    print(f'II.事業費: {expense}')
    print(f'    旅費: {expense_travel}')
    print(f'    会議費: {expense_meeting}')
    print(f'    謝金: {expense_gratuity}')
    print(f'    備品費: {expense_equipment}')
    print(f'   （借料及び損料）: {expense_rent}')
    print(f'    消耗品費: {expense_consumables}')
    print(f'    印刷製本費: {expense_print}')
    print(f'    補助員人件費: {expense_assistant}')
    print(f'    その他諸経費: {expense_misc}')
    print(f'III.再委託・外注費: {outsource}')
    print(f'IV.一般管理費: {administrative_expenses}')
    
def main():
    calc(sys.argv[1])
    
if __name__ == '__main__':
    sys.exit(main())
