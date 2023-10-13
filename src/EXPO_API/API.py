from typing import Dict, Any

import httpx
import requests
from httpx import Response
from requests.structures import CaseInsensitiveDict
from urllib3.exceptions import InsecureRequestWarning
from src.data.configuration import generate_link, url


class API:
    def __init__(self):
        self.requests = requests
        self.requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.url = generate_link()
        self.url_index_page = url['url_api_index_page']
        self.url_impact_page = url['url_api_impact_page']
        self.url_events_page = url['url_api_events_page']
        self.url_services_page = url['url_api_services_page']
        self.url_resources_page = url['url_api_resources_page']
        self.url_story_detail_page = url['url_api_story_detail_page']
        self.url_service_detail_page = url['url_api_service_detail_page']
        self.url_resource_detail_page = url['url_api_resource_detail_page']
        self.url_about_us_empty_type_page = url['url_api_about_us_empty_type_page']
        self.url_about_us_carousel_gallery_type_page = url['url_api_about_us_carousel_gallery_type_page']
        self.url_about_us_hero_img_type_page = url['url_api_about_us_hero_img_type_page']
        self.url_inperson_free_event_detail_page = url['url_api_inperson_free_event_detail_page']
        self.url_inperson_pay_event_detail_page = url['url_api_inperson_pay_event_detail_page']
        self.url_online_free_event_detail_page = url['url_api_online_free_event_detail_page']
        self.url_online_pay_event_detail_page = url['url_api_online_pay_event_detail_page']
    @staticmethod
    def return_formatted(response_status_code: int, response_json: Any) -> Dict[str, Any]:
        return {'status': response_status_code, 'json': response_json}

    def get_index_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_index_page)
        return API.return_formatted(response.status_code, response.json())

    async def get_index_page_httpx(self) -> Response:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.url_index_page)
            return response


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

    def get_story_detail_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_story_detail_page)
        return API.return_formatted(response.status_code, response.json())

    def get_service_detail_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_service_detail_page)
        return API.return_formatted(response.status_code, response.json())

    def get_resource_detail_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_resource_detail_page)
        return API.return_formatted(response.status_code, response.json())

    def get_about_us_empty_type_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_about_us_empty_type_page)
        return API.return_formatted(response.status_code, response.json())

    def get_about_us_carousel_gallery_type_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_about_us_carousel_gallery_type_page)
        return API.return_formatted(response.status_code, response.json())

    def get_about_us_hero_img_type_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_about_us_hero_img_type_page)
        return API.return_formatted(response.status_code, response.json())

    def get_inperson_free_event_detail_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_inperson_free_event_detail_page)
        return API.return_formatted(response.status_code, response.json())

    def get_inperson_pay_event_detail_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_inperson_pay_event_detail_page)
        return API.return_formatted(response.status_code, response.json())

    def get_online_free_event_detail_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_online_free_event_detail_page)
        return API.return_formatted(response.status_code, response.json())

    def get_online_pay_event_detail_page(self) -> Dict[str, Any]:
        response = self.requests.get(self.url_online_pay_event_detail_page)
        return API.return_formatted(response.status_code, response.json())