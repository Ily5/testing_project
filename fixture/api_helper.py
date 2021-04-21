import requests
import json
from model.model import TemplateModel


class ApiHelper:
    """ Вспомогательный класс для работы с api, есть метод получения авторизационного заголовка, \
    отправки запроса , получения данных об полном api endpoint """

    def __init__(self, url=None, payload=None, headers=None, method=None, route=None):
        self.url = url
        self.base_url = self.url
        self.payload = payload
        self.headers = headers
        self.method = method
        self.route = route
        self.model = TemplateModel(self)

    def request_send(self, method=None, url=None, payload="", file=None):
        self.payload = payload
        if url:
            url = self.url + url
        else:
            url = self.url
        if file and '.txt' not in file:
            file = {'file': open(f'../model/data/{file}.yaml', 'rb')}
            response = requests.request(method=method, url=url, files=file)
        elif 'txt' in file:
            file = {'file': open(f'../model/data/{file}', 'rb')}
            response = requests.request(method=method, url=url, files=file)
        else:
            response = requests.request(method=method, url=url, data=self.payload, headers=self.headers)
        return response

    def reset(self):
        # self.base_url = "http://127.0.0.1:5000/api/v1/templates"
        response = requests.request("GET", self.base_url, data="")
        s = self.get_array(response)
        # s = json.loads(response.text)
        if len(s["templates"]) > 0:
            for i in s["templates"]:
                self.request_send("DELETE", url=f'/{i}')

    def get_array(self, response):
        return json.loads(response.text)