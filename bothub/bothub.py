import requests

from .exceptions import BothubError


class Bothub(object):
    _URL = 'https://nlp.bothub.it/'
    authorization = None

    def __init__(self, authorization):
        self.authorization = authorization

    def _get_url(self, path):
        return f'{self._URL}{path}'

    @staticmethod
    def _request(authorization, method, path, data, **kwargs):
        request = requests.request(
            method=method,
            url=self._get_url(path),
            headers={"Authorization": f"Bearer {authorization}"},
            json=data,
            **kwargs,
        )
        if request.status_code > 200:
            raise BothubError(
                f"Bothub status_code: {request.status_code} ({request.reason})"
            )
        json = request.json()

        return json

    def parse(self, text, language=None, rasa_format=False):
        data = {"text": text}
        if language:
            data["language"] = language
        if rasa_format:
            data["rasa_format"] = rasa_format

        result = self._request(self.authorization, "POST", "v2/parse", data)
        return result
