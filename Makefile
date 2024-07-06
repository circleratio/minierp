all:
	@echo do nothing.

test:
	bash test.sh

test-meti:
	python3 ./meti-subcontract.py '{"name": "プロジェクト1", "fiscal_year": 2024}' 

clean:
	(cd base_data; rm -f people_and_organization.db)
	(cd operation_data; rm -f workflow.db approval.db)
	(cd logs; rm -f merp.log)
