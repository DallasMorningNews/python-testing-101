"""
These are just some really simple functions that we're going to exercise
using tests in the tests.py module.
"""
from csv import DictReader
from datetime import datetime
import random

import requests


def square(num):
    return num * num


def site_is_up(url):
    r = requests.get(url)

    if r.status_code >= 200 and r.status_code < 400:
        return True
    else:
        return False


def todays_day():
    return 'Today is %s' % datetime.now().strftime('%A')


def test_ready_for_publication(pub_date):
    if pub_date >= datetime.now().date():
        return True
    else:
        return False


def get_next_story(current_story_id, all_story_ids):
    random_story_id = random.choice(all_story_ids)
    while current_story_id == random_story_id:
        random_story_id = random.choice(all_story_ids)
    return random_story_id


def parse_date(date_str):
    """Turns a report date from the FEC disclosures into a Python datetime"""
    try:
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        try:
            return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        except ValueError:
            raise ValueError('Error converting "%s".' % date_str)


def count_csv_rows(csv_file):
    num_rows = 0

    with open(csv_file, 'r') as csv_infile:
        parsed = DictReader(csv_infile)

        for row in parsed:
            num_rows += 1

    return num_rows
