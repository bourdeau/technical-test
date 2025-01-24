.PHONY: run
run:
	poetry run python spark/main.py

.PHONY: test
test:
	poetry run pytest

