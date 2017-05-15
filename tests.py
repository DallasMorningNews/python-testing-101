import unittest
from mock import patch

from requests import Response

from dumbfunctions import site_is_up, square


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


if __name__ == '__main__':
    unittest.main()
