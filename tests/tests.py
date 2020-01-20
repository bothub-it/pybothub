import unittest
import requests_mock

from bothub import Bothub


class BothubTestCase(unittest.TestCase):
    def setUp(self):
        self.bothub = Bothub("xxxxxxxxxx")

    def test_get_url(self):
        self.assertEqual(self.bothub._get_url("/test"), f"{self.bothub._URL}/test")

    @requests_mock.Mocker()
    def test_request(self, request_mock):
        url = self.bothub._get_url("test")
        json = {"test": "test"}
        request_mock.post(url, json=json)
        request = self.bothub._request(
            authorization="xxxxxxxxxx",
            method="post",
            path="test",
            data={"test": "test"},
        )
        self.assertEqual(request, json)


if __name__ == "__main__":
    unittest.main()
