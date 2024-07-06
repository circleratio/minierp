#!/usr/bin/python3
import json
import sys
import common
import people, assignment, wage, expense, project

def calc_personnel_costs(project_dict):
    people_db = people.People() 
    assignment_db = assignment.Assignment()
    wage_db = wage.Wage()

    total = 0
    details = []
    
    l = assignment_db.getByProject(project_dict['name'], project_dict['fiscal_year'])
    for p in l:
        where = {'name': p['name'], 'fiscal_year': p['fiscal_year']}
        unit_prices = wage_db.get(where)['wages']
        rates = p['assignment']
        prices = [x * y for x, y in zip(rates, unit_prices)]
        
        total += sum(prices)
        
        item = {'name': p['name'], 'price': prices, 'rate': rates, 'unit_price': unit_prices}
        details.append(item)
        
    return(total, details)

def calc_expense(project_dict):
    expense_db = expense.Expense()
    total = {}
    details = []

    where = {'fiscal_year': project_dict['fiscal_year'],
             'type': 'II.事業費'}
    l = expense_db.get(where)
    for i in l:
        if i['subtype'] in total:
            total[i['subtype']] += sum(i['plan'])
        else:
            total[i['subtype']] = sum(i['plan'])
        details.append(i)

    return(total, details)

def calc_outsource_costs(project_dict):
    expense_db = expense.Expense()
    total = 0
    details = []

    where = {'fiscal_year': project_dict['fiscal_year'],
             'type': 'III.再委託・外注費'}
    l = expense_db.get(where)
    for i in l:
        total += sum(i['plan'])
        details.append(i)

    return(total, details)

def calc_all(project_dict):
    common_db = common.Common()
    result = {}
    total_expense = 0
    
    result['name'] = project_dict['name'] 
    result['personnel_costs'], result['personnel_costs_details'], = calc_personnel_costs(project_dict)
    result['expense'], result['expense_details'], = calc_expense(project_dict)
    result['outsource_costs'], result['outsource_costs_details'], = calc_outsource_costs(project_dict)
    for i in result['expense']:
        total_expense += result['expense'][i]

    result['administrative_expenses'] = (result['personnel_costs'] + total_expense) * project_dict['一般管理費率']
    result['subtotal'] = result['personnel_costs'] + total_expense + result['outsource_costs'] +  result['administrative_expenses']
    
    result['consumption_tax'] = result['subtotal'] * common_db.get('consumption_tax')
    result['total'] = result['subtotal'] + result['consumption_tax'] 
    return(result)

def render(js):
    common_db = common.Common()

    print('法人名: {}'.format(common_db.get('company_name')))
    print('プロジェクト名: {}'.format(js['name']))
    
    print('I.人件費: {}'.format(js['personnel_costs']))
    print('II.事業費:')
    for i in js['expense']:
          print('    {}: {}'.format(i, js['expense'][i]))
    print('III.再委託・外注費: {}'.format(js['outsource_costs']))
    print('IV.一般管理費: {}'.format(js['administrative_expenses']))
    print('小計: {}'.format(js['subtotal']))
    print('消費税: {}'.format(js['consumption_tax']))
    print('合計: {}'.format(js['total']))
    
    print('\n========== 人件費内訳 ==========')
    for i in js['personnel_costs_details']:
        print(i)
    
    print('\n========== 事業費内訳 ==========')
    for i in js['expense_details']:
        print(i)
    
    print('\n========== 再委託・外注費内訳 ==========')
    for i in js['outsource_costs_details']:
        print(i)
        
def main():
    db = project.Project()
    
    where = json.loads(sys.argv[1])
    project_dict = db.get(where)
    
    res = calc_all(project_dict)
    render(res)
    
if __name__ == '__main__':
    sys.exit(main())
