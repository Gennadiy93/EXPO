from src.EXPO_API.API import API

try:
    api = API()
except BaseException:
    raise Exception('Error')


def test_status_code_index_page():
    print(api.url['url_api'])