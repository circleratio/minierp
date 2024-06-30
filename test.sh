#!/usr/bin/bash

python3 ./merp.py people add '{"name": "mf", "attr": {"family name": "藤原", "first name": "道長", "title": "代表理事", "mail": "michf@abc.or.jp"}}'
python3 ./merp.py people add '{"name": "kf", "attr": {"family name": "藤原", "first name": "伊周", "title": "事務局長", "mail": "kfuji@abc.or.jp"}}'
python3 ./merp.py people add '{"name": "minamoto", "attr": {"family name": "源", "first name": "良清", "title": "事務局", "mail": "minamoto@abc.or.jp"}}'

python3 ./merp.py workflow add '{"name": "abc", "owner": "abcd", "flow": {"pos": 0, "flow": [{"action": "approval", "person_in_charge": "tf" }, {"action": "close"}]} , "type": "payment", "status": "run"}'
python3 ./merp.py workflow step_forward '{"id": 1, "arg": {"actor": "tf", "message": "I did it."}}'
python3 ./merp.py workflow reject '{"id": 1, "arg": {"actor": "tf", "message": "I did it."}}'
