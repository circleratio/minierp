all: merp.py
	merp.py

test: test.sh
	bash test.sh

clean:
	(cd base_data; rm -f people_and_organization.db)
	(cd operation_data; rm -f workflow.db approval.db)
	(cd logs; rm -f merp.log)
