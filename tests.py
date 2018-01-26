import unittest

from freezegun import freeze_time
from mock import patch
from requests import Response

from dumbfunctions import count_csv_rows, site_is_up, square, todays_day


class TestDumbMathFunctions(unittest.TestCase):
    def test_squares_ints(self):
        """When passed an integer, it should square it"""
        self.assertEqual(square(2), 4)

    def test_squares_floats(self):
        """When passed a float, it should square it"""
        self.assertEqual(square(1.5), 2.25)

    def test_string_fail(self):
        """Trying to square a string raises a TypeError"""
        with self.assertRaises(TypeError):
            square('string')


class TestDumbRequestsFunctions(unittest.TestCase):
    @patch('dumbfunctions.requests')
    def test_site_requested(self, mock_requests):
        """Should make one GET request to passed URL"""
        site_is_up('http://www.google.com')
        mock_requests.get.assert_called_with('http://www.google.com')
        self.assertEqual(mock_requests.get.call_count, 1)

    @patch('dumbfunctions.requests')
    def test_request_fails(self, mock_requests):
        """Should return False if URL errors"""
        mock_requests.get.return_value = Response()
        mock_requests.get.return_value.status_code = 500
        self.assertEqual(site_is_up('not-a-url.aaaaaa'), False)

    @patch('dumbfunctions.requests')
    def test_request_ok(self,  mock_requests):
        """Should return True if URL returns OK status code"""
        mock_requests.get.return_value = Response()
        mock_requests.get.return_value.status_code = 200
        self.assertEqual(site_is_up('not-a-url.aaaaaa'), True)


@freeze_time('2017-05-03')
class TestDumbDayFunction(unittest.TestCase):
    def test_todays_day(self):
        """Should return the current day of the week"""
        self.assertEqual(todays_day(), 'Today is Wednesday')


class TestDumbCsvFunction(unittest.TestCase):
    def test_returns_row_count(self):
        """Should count the number of rows in a CSV"""
        self.assertEqual(count_csv_rows('fixtures/csv_input.csv'), 2)


if __name__ == '__main__':
    unittest.main()
