# Flask application make file

VIRTUALENV = $(shell which virtualenv)

venv:
	$(VIRTUALENV) venv

clean: stop
	rm -rf flask_boilerplate.egg-info
	rm -rf build
	rm -rf dist
	rm -rf venv

install: clean venv
	. venv/bin/activate; python setup.py install

test: venv
	. venv/bin/activate; python tests.py

start: venv
	export FLASK_APP=run.py
	. venv/bin/activate; flask run &

stop:
	ps -ef | grep "flask-boilerplate/venv/bin/flask run" | grep -v grep | awk '{print $2}' | xargs kill
