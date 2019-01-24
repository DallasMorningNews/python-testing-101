# Testing basics [![CircleCI token](https://img.shields.io/circleci/token/ab0c79940dd8b720258ea65fbbd9ce3d4cf965fb/project/github/DallasMorningNews/python-testing-101/master.svg)](https://circleci.com/gh/DallasMorningNews/python-testing-101)

This repo contains the files for the #NICAR18 session "[Python: Writing Tests For Your Code](https://www.ire.org/events-and-training/event/3189/3631/)" and the DMN's Python/Django testing brown bag.

## What's in here

- **[dumbfunctions.py](dumbfunctions.py)**: This is just some sample code, which we'll exercise with our tests
- **[tests.py](tests.py)**: A Python module with two "test cases"; running this file will run our tests
- **[circle.yml](circle.yml)**: A configuration file for [Circle CI](https://circleci.com/), which is wired to this repo as a continuous integration service

## Related reading

- [Unit testing framework, official Python docs](https://docs.python.org/3.6/library/unittest.html)
- [Mock object library, official Python docs](https://docs.python.org/3/library/unittest.mock.html)
- [Testing Your Code, The Hitchiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/tests/)
- [Testing in Django, official Django docs](https://docs.djangoproject.com/en/1.11/topics/testing/)

## Requirements

- Python 2 or 3

_Optional_

- `virtualenv` or `pipenv`

## Installation

#### Using `pipenv`

1. Install dependencies and create a new virtual environment with `pipenv`:

    ```sh
    $ pipenv install
    ```

#### Using `virtualenv`

1. _Optional:_ Create a virtual environment:

    ```sh
    # for Python 2
    $ virtualenv venv
    ```

    ```sh
    # for Python 3
    $ virtualenv venv --python=python3
    ```

2. _Optional:_ If you created a virtual environment, step into it before install dependencies on the next step.
    ```sh
    $ source venv/bin/activate
    ```

3. Install dependencies:
    ```sh
    $ pip install -r requirements.txt
    ```

## Usage

_The below should be run in your virtual environment if you're using one. For example, you should run `pipenv shell` before running the below if you're using `pipenv`._

To run tests:

```sh
$ python tests.py
```

To run tests and check test coverage:

```sh
$ coverage run --omit='.venv/**/*.py,venv/**/*.py,tests.py' tests.py
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
