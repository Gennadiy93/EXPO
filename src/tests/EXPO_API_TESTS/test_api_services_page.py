from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_services_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_services_page():
    assert status_code_api == 200


def test_services_title_is_not_empty():
    services_title = response_api_json['pageProps']['title']
    assert services_title is not None and services_title != ''


def test_services_desc_is_not_empty():
    services_desc = response_api_json['pageProps']['prefaceText']
    assert services_desc is not None and services_desc != ''


def test_list_services_filters_is_not_empty():
    services_filters = response_api_json['pageProps']['serviceCategoryFilters']
    assert services_filters is not None and services_filters != '' and len(services_filters) != 0


def test_list_services_pillars_filters_is_not_empty():
    services_pillars_filters = response_api_json['pageProps']['servicePillarsFilters']
    assert services_pillars_filters is not None and services_pillars_filters != '' and len(services_pillars_filters) != 0


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


def test_list_services_collection_is_not_empty():
    list_services_collection = response_api_json['pageProps']['services']
    assert list_services_collection is not None and list_services_collection != '' and len(list_services_collection) != 0


def test_titles_in_list_services_is_not_empty():
    list_services_collection = response_api_json['pageProps']['services']
    for service in list_services_collection:
        assert service['pageTitle'] is not None and service['pageTitle'] != ''


def test_slug_in_list_services_is_not_empty():
    list_services_collection = response_api_json['pageProps']['services']
    for service in list_services_collection:
        assert service['slug'] is not None and service['slug'] != ''


def test_thumbnail_image_in_list_services_is_not_empty():
    list_services_collection = response_api_json['pageProps']['services']
    for service in list_services_collection:
        assert service['serviceThumbnail'] is not None and service['serviceThumbnail'] != ''


def test_category_pillar_in_list_services_is_not_empty():
    list_services_collection = response_api_json['pageProps']['services']
    for service in list_services_collection:
        assert service['pillars'] is not None and service['pillars'] != ''


def test_category_in_list_services_is_not_empty():
    list_services_collection = response_api_json['pageProps']['services']
    for service in list_services_collection:
        assert service['serviceCategoriesCollection'] is not None and service['serviceCategoriesCollection'] != ''


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''
