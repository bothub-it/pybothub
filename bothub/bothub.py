import requests


class BothubError(Exception):
    pass


class Bothub(object):
    authorization = None

    def __init__(self, authorization):
        self.authorization = authorization

    @staticmethod
    def _request(authorization, method, path, data, **kwargs):
        request = requests.request(
            method=method,
            url=f"https://nlp.bothub.it/{path}",
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
