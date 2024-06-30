all: merp.py
	merp.py

test: test.sh
	bash test.sh

clean:
	(cd base_data; rm -f people_and_organization.db workflow.db approval.db)
