from src.EXPO_API.API import API
from src.EXPO_API.IndexPageSheme import Index_Page
from pydantic import BaseModel, ValidationError, field_validator, Field
from typing import List


try:
    api = API()
    response_api = api.get_index_page()
    response_api_json = response_api['json']['pageProps']
except BaseException:
    raise Exception('Error')


def test_validate_index_page():
    index_page = Index_Page.model_validate(response_api_json)
    print(index_page.resources)

