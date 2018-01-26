test:
	- flake8 **/*.py --exclude="venv/**,tests.py"
	- coverage run --omit="venv/**,tests.py" tests.py
	- coverage html
