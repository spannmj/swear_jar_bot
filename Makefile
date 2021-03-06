PYTHON = $(shell which python2.7)
ENV = $(CURDIR)/env

virtual-env:
	virtualenv --python=$(PYTHON) $(ENV)

env: virtual-env
	$(ENV)/bin/pip install -r requirements/base.txt

run_bot: 
	$(ENV)/bin/python main.py

run_app:
	$(ENV)/bin/python app.py

clean:
	rm -rf $(ENV)
