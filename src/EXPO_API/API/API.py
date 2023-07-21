import requests
from requests.structures import CaseInsensitiveDict
from urllib3.exceptions import InsecureRequestWarning
from src.data.configuration import url_staging_api_index_json


class API():
    def __init__(self):
        # self.headers = CaseInsensitiveDict()
        #
        # # Updating the headlines
        # self.headers["Accept"] = "*/*"
        # self.headers["Accept-Encoding"] = 'gzip, deflate, br'
        # self.headers["Connection"] = 'keep-alive'

        # Announcing the headlines and Updating the token
        self.requests = requests
        self.requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        self.url_index_json = url_staging_api_index_json

    @staticmethod
    def return_formatted(response_status_code, response_json):
        return {'status': response_status_code, 'json': response_json}

    def get_index_page(self):
        response = self.requests.get(self.url_index_json)
        return API.return_formatted(response.status_code, response.json())
