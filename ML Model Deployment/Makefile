# if we run "make run", it will run the runner.py file
# it will install all dependency first
run: install
	cd src; poetry run python3 runner.py

install:pyproject.toml
	poetry install 

# remove pycache files and keep project clean
clean:
	rm -rf `find . -type d -name __pycache__`

# execute run and clean commands 
runner: run clean