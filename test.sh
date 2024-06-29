#!/usr/bin/bash

python3 ./merp.py people add '{"name": "tf", "attr": {"family name": "藤原", "first name": "輝嘉", "title": "代表理事", "mail": "fujiwara@abc.or.jp"}}'
python3 ./merp.py people add '{"name": "yamada", "attr": {"family name": "山田", "first name": "太郎", "title": "センター長", "mail": "yamada@abc.or.jp"}}'

python3 ./merp.py workflow add '{"name": "abc", "owner": "abcd", "flow": {"pos": 0, "flow": [{"action": "approval", "person_in_charge": "tf" }, {"action": "close"}]} , "type": "payment", "status": "run"}'
python3 ./merp.py workflow step_forward '{"id": 1, "arg": {"actor": "tf", "message": "I did it."}}'
python3 ./merp.py workflow reject '{"id": 1, "arg": {"actor": "tf", "message": "I did it."}}'
