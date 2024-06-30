#!/usr/bin/python3
import datetime
import json
import people

def fiscal_year_to_index(fy_month):
    if fy_month >= 4 and fy_month <= 12:
        return(fy_month - 4)
    elif fy_month > 0 and fy_month < 4:
        return(fy_month + 8)
    else:
        print(f'Invalid month: {fy_month}')
        exit(1)

def index_to_fiscal_year_str(idx):
    fy_month_str = ['4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3']
    return(fy_month_str[idx])

def sum_work(person, calc_type, year, month_from, month_to, assignment):
    sum = 0
    year_str = f'FY{year}'

    if calc_type != 'plan' and calc_type != 'result':
        print('calc_type must be plan or result. Aborted.')
        exit(1)

    db_people = people.People()

    if not db_people.has(person):
        print(f'No user found: {person}')
        exit(1)
    
    with open(f'{calc_type}/work-{year_str}.json', 'r') as f:
        work_dict = json.load(f)
        #print(work_dict)

        mf = fiscal_year_to_index(month_from)
        mt = fiscal_year_to_index(month_to)
    
        for i in range(mf, mt + 1):
            km = index_to_fiscal_year_str(i)
            if km in work_dict[person]:
                item = work_dict[person][km]
                unit_price = item['unit price']
                assignment_dict = item['assignment']
                if assignment in assignment_dict:
                    sum += unit_price * assignment_dict[assignment]
                
        return(sum)
    print(f'No data found: {year}')
    exit(1)

def main():
    s = sum_work('mf', 'plan', 2024, 4, 3, '事務局')
    print(s)
    
if __name__ == '__main__':
    sys.exit(main())
