install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black ./python_files ./*.ipynb

lint:
	ruff check ./python_files/main_files ./python_files/test_files 

test:
	python -m pytest -vv --nbval ./python_files/test_files/test_*.py *.ipynb

all: install format lint test 