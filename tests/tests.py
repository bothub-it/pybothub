import unittest

from bothub import Bothub


class BothubTestCase(unittest.TestCase):
    def setUp(self):
        self.bothub = Bothub("xxxxxxxxxx")

    def test_get_url(self):
        self.assertEqual(self.bothub._get_url("/test"), f"{self.bothub._URL}/test")


if __name__ == "__main__":
    unittest.main()
