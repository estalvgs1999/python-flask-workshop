.PHONY: dev
dev:
	FLASK_APP=./backend/__main__.py FLASK_ENV=development flask run