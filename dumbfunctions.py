"""
These are just some really simple functions that we're going to exercise
using tests in the tests.py module.
"""
from datetime import datetime

import requests


def square(num):
    return num * num


def site_is_up(url):
    r = requests.get(url)

    if r.status_code == 200:
        return True
    else:
        return False


def todays_day():
    return 'Today is %s' % datetime.now().strftime('%A')
