import requests
# coding=utf-8

class ApiRequest:
    def __init__(self, url, headers=None, cookies=None):
        self.url = url
        self.headers = headers
        self.cookies = cookies

    def request(self, method, path, data=None, params=None, json=None, files=None):
        url = self.url + path
        response = requests.request(method=method, url=url, headers=self.headers, cookies=self.cookies, data=data, params=params, json=json, files=files)
        return response

    def get(self, path, params=None):
        return self.request('GET', path, params=params)

    def post(self, path, data=None, json=None, files=None):
        return self.request('POST', path, data=data, json=json, files=files)

    def put(self, path, data=None, json=None, files=None):
        return self.request('PUT', path, data=data, json=json, files=files)

    def delete(self, path, data=None, json=None, files=None):
        return self.request('DELETE', path, data=data, json=json, files=files)