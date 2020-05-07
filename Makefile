all: build

build:
	mkdocs build

deploy:
	mkdocs gh-deploy --force

test:
	mkdocs build --strict

preview:
	mkdocs serve
