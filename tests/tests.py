import unittest
import requests_mock

from decouple import config
from bothub import Bothub


class BothubTestCase(unittest.TestCase):

    def setUp(self):
        self.bothub = Bothub('abc123')

    def test_get_url(self):
        self.assertEqual(self.bothub._get_url('/test'), f'{self.bothub._URL}/test')


if __name__ == '__main__':
    unittest.main()