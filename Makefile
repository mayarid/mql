.PHONY: all clean build

all: build upload clean

test:
			pytest --cov=bql --cov-report=term-missing

build:
			rm -rf dist
			python setup.py sdist
			gpg --detach-sign -a dist/*

upload:
			twine upload dist/*

clean:
			find . -d -name "__pycache__" -exec rm -rf {} \;
			rm -rf .coverage temp neo_cli.egg-info dist build .pytest_cache .ropeproject bql/bqllex.py bql/bqlyacc.py bql/bql_debug
