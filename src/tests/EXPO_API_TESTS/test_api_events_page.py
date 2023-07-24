from src.EXPO_API.API import API

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


def test_news_title_in_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['slider']
    for news in list_news:
        assert news['pageTitle'] is not None and news['pageTitle'] != '', f'Missing news title{news}'


def test_news_slug_in_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['slider']
    for news in list_news:
        assert news['slug'] is not None and news['slug'] != ''


def test_news_image_in_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['slider']
    for news in list_news:
        assert news['eventHeroLandscapeImage'] is not None and news['eventHeroLandscapeImage'] != '', f'Missing news image{news}'


def test_list_events_collection_is_not_empty():
    list_events_collection = response_api_json['pageProps']['events']
    assert list_events_collection is not None and list_events_collection != '' and len(list_events_collection) != 0


def test_titles_in_list_events_is_not_empty():
    list_events_collection = response_api_json['pageProps']['events']
    for event in list_events_collection:
        assert event['pageTitle'] is not None and event['pageTitle'] != '', f'Missing event title{event}'


def test_slug_in_list_events_is_not_empty():
    list_events_collection = response_api_json['pageProps']['events']
    for event in list_events_collection:
        assert event['slug'] is not None and event['slug'] != '', f'Missing event slug{event}'


def test_event_type_in_list_events_is_not_empty():
    list_events_collection = response_api_json['pageProps']['events']
    for event in list_events_collection:
        assert event['eventType'] is not None and event['eventType'] != '', f'Missing event type{event}'


def test_time_event_in_list_events_is_not_empty():
    list_events_collection = response_api_json['pageProps']['events']
    for event in list_events_collection:
        if event['eventType'] == 'Virtual':
            assert event['onlineEventOpeningHoursNew'] is not None and event['onlineEventOpeningHoursNew'] != '', event['pageTitle']
        elif event['eventType'] == 'In-Person':
            assert event['inPersonOpeningHoursNew'] is not None and event['inPersonOpeningHoursNew'] != '', event['pageTitle']
        elif event['eventType'] == 'In-Person & Virtual':
            assert event['inPersonOpeningHoursNew'] is not None and event['inPersonOpeningHoursNew'] != '' and event['onlineEventOpeningHoursNew'] is not None and event['onlineEventOpeningHoursNew'] != '', event['pageTitle']


def test_category_collection_in_list_events_is_not_empty():
    list_events_collection = response_api_json['pageProps']['events']
    for event in list_events_collection:
        assert event['categoriesCollection'] is not None and event['categoriesCollection'] != '', f'Missing event categories{event}'


def test_thumbnail_image_in_list_events_is_not_empty():
    list_events_collection = response_api_json['pageProps']['events']
    for event in list_events_collection:
        assert event['eventHeroSquareImage'] is not None and event['eventHeroSquareImage'] != '', f'Missing event thumbnail{event}'


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''
