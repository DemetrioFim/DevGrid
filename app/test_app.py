import unittest

from app import app
from weather_tools import get_city, get_standarted_info

class TestCase(unittest.TestCase):

    def test_get_main_page(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_standarted_info(self):
        tester = get_standarted_info('Santo Andre')
        self.assertEqual(type(tester[0]), list)
        self.assertEqual(type(tester[1]), list)
        self.assertEqual(type(tester[2]), bool)

    def test_get_city(self):
        tester = get_city('Santo Andre',  lang='en', units='metric', TOKEN='68dcc09865f92950175effb9381ee5d1')
        self.assertEqual(type(tester), list)

if __name__ == '__main__':
    unittest.main()
