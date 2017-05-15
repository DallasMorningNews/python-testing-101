# Testing basics

## Reading

- [Testing Your Code, The Hitchiker's Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/)
- [Testing in Django, official Django docs](https://docs.djangoproject.com/en/1.11/topics/testing/)

## Requirements

- Python 2 or 3

_Optional_

- `virtualenv`

## Installation

1. _Optional:_ Create a virtual environment:

  ```sh
  # for Python 2
  $ virtualenv venv
  ```

  ```sh
  # for Python 3
  $ virtualenv venv --python=python3
  ```

2. Install dependencies:

  ```sh
  # for Python 2
  $ pip install -r requirements-py2.txt
  ```

  ```sh
  # for Python 3
  $ pip install -r requirements-py3.txt
  ```

## Usage

To run tests:

```sh
$ python tests.py
```

To check test coverage while running tests:

```sh
$ coverage run --omit='venv/**/*.py,tests.py' tests.py
```

To view coverage information in the console:

```sh
$ coverage report
```

To see an HTML page with coverage information:

```sh
$ coverage html  # needs to run each time you do "coverage run"
$ open htmlcov/index.html
```
