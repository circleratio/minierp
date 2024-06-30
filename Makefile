all: merp.py
	@echo do nothing

test: test.sh
	bash test.sh

clean:
	rm -f data/people_and_organization.db  data/workflow.db
