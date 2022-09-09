.PHONY: dev
dev:
	FLASK_APP=./backend/__main__.py FLASK_DEBUG=1 flask run

start:
	FLASK_APP=./backend/__main__.py flask run
