src := spider_scrape
test-src := tests

check:
	poetry run black $(src) $(test-src) --check --diff
	poetry run mypy --install-types --non-interactive $(src) $(test-src)
	poetry run ruff $(src) $(test-src)
	poetry run mdformat --check --number .

format:
	poetry run black $(src) $(test-src)
	poetry run ruff $(src) $(test-src) --fix
	poetry run mdformat --number .
