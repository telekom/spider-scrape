src := spider_scrape
test-src := tests

check:
	poetry run black $(src) $(test-src) --check --diff
	poetry run mypy --install-types --non-interactive $(src) $(test-src)
	poetry run ruff $(src) $(test-src)

format:
	poetry run black $(src) $(test-src)
	poetry run ruff $(src) $(test-src) --fix

install-all:
	poetry install --all-extras
