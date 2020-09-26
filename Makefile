setup:
	python3 -m venv ~/msds434

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C test.py