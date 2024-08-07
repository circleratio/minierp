#!/usr/bin/bash
python3 ./merp.py common set '{"company_name": "会社名", "consumption_tax": 0.1}'

python3 ./merp.py people set '{"name": "mf", "attr": {"family name": "藤原", "first name": "道長", "title": "代表理事", "mail": "michf@abc.or.jp"}}'
python3 ./merp.py people set '{"name": "kf", "attr": {"family name": "藤原", "first name": "伊周", "title": "事務局長", "mail": "kfuji@abc.or.jp"}}'
python3 ./merp.py people set '{"name": "minamoto", "attr": {"family name": "源", "first name": "良清", "title": "事務局", "mail": "minamoto@abc.or.jp"}}'
python3 ./merp.py people get '{"name": "mf"}'
python3 ./merp.py people dump '{}'

python3 ./merp.py wage set '{"name": "mf", "fiscal_year": 2024, "wages": [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]}'
python3 ./merp.py wage set '{"name": "kf", "fiscal_year": 2024, "wages": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]}'
python3 ./merp.py wage get '{"name": "mf", "fiscal_year": 2024}'
python3 ./merp.py wage dump '{}'

python3 ./merp.py assignment set '{"name": "mf", "fiscal_year": 2024, "project": "プロジェクト1", "assignment": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]}'
python3 ./merp.py assignment set '{"name": "mf", "fiscal_year": 2024, "project": "プロジェクト2", "assignment": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]}'
python3 ./merp.py assignment set '{"name": "kf", "fiscal_year": 2024, "project": "プロジェクト1", "assignment": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]}'
python3 ./merp.py assignment dump '{}'
python3 ./merp.py assignment getbyperson '{"name": "mf", "fiscal_year": 2024}'

python3 ./merp.py expense set '{"name": "会議費", "fiscal_year": 2024, "project": "プロジェクト1", "type": "II.事業費", "subtype": "会議費", "plan": [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250], "result": [249, 249, 249, 249, 249, 249, 0, 0, 0, 0, 0, 0]}'
python3 ./merp.py expense set '{"name": "出張費", "fiscal_year": 2024, "project": "プロジェクト1", "type": "II.事業費", "subtype": "旅費", "plan": [35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35], "result": [20, 29, 33, 20, 0, 0, 0, 0, 0, 0, 0, 0]}'
python3 ./merp.py expense set '{"name": "システム開発費", "fiscal_year": 2024, "project": "プロジェクト1", "type": "III.再委託・外注費", "subtype": "", "plan": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22000], "result": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}'

python3 ./merp.py project set '{"name": "プロジェクト1", "一般管理費率": 0.1, "fiscal_year": 2024, "month_start": 4, "month_end": 3}'
