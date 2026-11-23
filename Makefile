format:
	ruff format .

lint:
	ruff check .

test:
	pytest

check: format lint test
