import unittest
from mock import patch

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
        """Should make a GET request to passed URL"""
        site_is_up('http://www.google.com')
        mock_requests.get.assert_called_once_with('http://www.google.com')

    @patch('dumbfunctions.requests')
    def test_request_ok(self, mock_requests):
        """Should return False if URL errors"""
        mock_requests.get.return_value.status_code = 500
        self.assertEqual(site_is_up(), False)

    @patch('dumbfunctions.requests')
    def test_request_fails(self,  mock_requests):
        """Should return True if URL return OK status code"""
        mock_requests.get.return_value.status_code = 200
        self.assertEqual(site_is_up(), True)


if __name__ == '__main__':
    unittest.main()
