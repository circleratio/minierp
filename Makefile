all:
	mkdir -p base_data operation_data

test: test-db test-meti

test-db:
	bash tests/test.sh

test-meti:
	bash tests/test-meti.sh

clean:
	(cd base_data; rm -f base.db)
	(cd operation_data; rm -f merp.log)
