from src.EXPO_API.API.API import API

try:
    api = API()
    response_api = api.get_events_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_events_page():
    assert status_code_api == 200


def test_events_title_is_not_empty():
    events_title = response_api_json['pageProps']['title']
    assert events_title is not None and events_title != ''


def test_events_desc_is_not_empty():
    events_desc = response_api_json['pageProps']['desc']
    assert events_desc is not None and events_desc != ''


def test_list_events_filters_is_not_empty():
    events_filters = response_api_json['pageProps']['filters']
    assert events_filters is not None and events_filters != '' and len(events_filters) != 0


def test_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['slider']
    assert list_news is not None and list_news != '' and len(list_news) != 0


def test_list_events_collection_is_not_empty():
    list_events_collection = response_api_json['pageProps']['events']
    assert list_events_collection is not None and list_events_collection != '' and len(list_events_collection) != 0


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''
