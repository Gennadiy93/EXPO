from typing import Dict, Any

import requests
from requests.structures import CaseInsensitiveDict
from urllib3.exceptions import InsecureRequestWarning
from src.data.configuration import url_staging_api_index_page, url_staging_api_impact_page, url_staging_api_events_page, \
    url_staging_api_services_page, url_staging_api_resources_page


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

        self.url_index_page = url_staging_api_index_page
        self.url_impact_page = url_staging_api_impact_page
        self.url_events_page = url_staging_api_events_page
        self.url_services_page = url_staging_api_services_page
        self.url_resources_page = url_staging_api_resources_page

    @staticmethod
    def return_formatted(response_status_code: int, response_json: Any) -> Dict[str, Any]:
        return {'status': response_status_code, 'json': response_json}

    def get_index_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_index_page)
        return API.return_formatted(response.status_code, response.json())

    def get_impact_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_impact_page)
        return API.return_formatted(response.status_code, response.json())

    def get_events_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_events_page)
        return API.return_formatted(response.status_code, response.json())

    def get_services_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_services_page)
        return API.return_formatted(response.status_code, response.json())

    def get_resources_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_resources_page)
        return API.return_formatted(response.status_code, response.json())
