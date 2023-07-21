from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_resources_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_resources_page():
    assert status_code_api == 200


def test_resources_title_is_not_empty():
    resources_title = response_api_json['pageProps']['pageTitle']
    assert resources_title is not None and resources_title != ''


def test_resources_desc_is_not_empty():
    resources_desc = response_api_json['pageProps']['prefaceText']
    assert resources_desc is not None and resources_desc != ''


def test_list_resources_filters_is_not_empty():
    resources_filters = response_api_json['pageProps']['categories']
    assert resources_filters is not None and resources_filters != '' and len(resources_filters) != 0


def test_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['news']
    assert list_news is not None and list_news != '' and len(list_news) != 0


def test_news_title_in_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['news']
    for news in list_news:
        assert news['newsTitle'] is not None and news['newsTitle'] != ''


def test_news_subtitle_in_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['news']
    for news in list_news:
        assert news['newsSubtitle'] is not None and news['newsSubtitle'] != ''


def test_news_link_in_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['news']
    for news in list_news:
        assert news['newsCtaBtnLink'] is not None and news['newsCtaBtnLink'] != ''


def test_news_image_in_list_news_is_not_empty():
    list_news = response_api_json['pageProps']['news']
    for news in list_news:
        assert news['newsImage'] is not None and news['newsImage'] != ''


def test_list_resources_collection_is_not_empty():
    list_resources_collection = response_api_json['pageProps']['resources']
    assert list_resources_collection is not None and list_resources_collection != '' and len(
        list_resources_collection) != 0


def test_titles_in_list_resources_is_not_empty():
    list_resources_collection = response_api_json['pageProps']['resources']
    for resource in list_resources_collection:
        assert resource['title'] is not None and resource['title'] != ''


def test_slug_in_list_resources_is_not_empty():
    list_resources_collection = response_api_json['pageProps']['resources']
    for resource in list_resources_collection:
        assert resource['slug'] is not None and resource['slug'] != ''


def test_categories_in_list_resources_is_not_empty():
    list_resources_collection = response_api_json['pageProps']['resources']
    for resource in list_resources_collection:
        assert resource['categoriesCollection'] is not None and resource['categoriesCollection'] != ''


def test_thumbnail_image_in_list_resources_is_not_empty():
    list_resources_collection = response_api_json['pageProps']['resources']
    for resource in list_resources_collection:
        assert resource['resourceThumbnail'] is not None and resource['resourceThumbnail'] != ''


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''
