from src.EXPO_API.API.API import API

try:
    api = API()
    response_api = api.get_impact_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_impact_page():
    assert status_code_api == 200


def test_impact_title_is_not_empty():
    impact_title = response_api_json['pageProps']['title']
    assert impact_title is not None and impact_title != ''


def test_impact_desc_is_not_empty():
    impact_desc = response_api_json['pageProps']['prefaceText']
    assert impact_desc is not None and impact_desc != ''


def test_list_impact_filters_is_not_empty():
    impact_filters = response_api_json['pageProps']['impactPageFilters']
    assert impact_filters is not None and impact_filters != '' and len(impact_filters) != 0


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


def test_list_story_collection_is_not_empty():
    list_story_collection = response_api_json['pageProps']['storyCollection']
    assert list_story_collection is not None and list_story_collection != '' and len(list_story_collection) != 0

def test_story_title_in_list_stories_is_not_empty():
    list_story_collection = response_api_json['pageProps']['storyCollection']
    for story in list_story_collection:
        assert story['pageTitle'] is not None and story['pageTitle'] != ''


def test_story_slug_in_list_stories_is_not_empty():
    list_story_collection = response_api_json['pageProps']['storyCollection']
    for story in list_story_collection:
        assert story['slug'] is not None and story['slug'] != ''


def test_story_thumbnail_in_list_stories_is_not_empty():
    list_story_collection = response_api_json['pageProps']['storyCollection']
    for story in list_story_collection:
        assert story['heroSquareImage'] is not None and story['heroSquareImage'] != ''


def test_categories_collection_in_list_stories_is_not_empty():
    list_story_collection = response_api_json['pageProps']['storyCollection']
    for story in list_story_collection:
        assert story['categoriesCollection'] is not None and story['categoriesCollection'] != '' and len(story['categoriesCollection']) != 0


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''
