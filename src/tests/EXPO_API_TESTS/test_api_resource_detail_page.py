from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_resource_detail_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_resource_detail_page():
    assert status_code_api == 200


def test_resource_title_is_not_empty():
    resource_title = response_api_json['pageProps']['title']
    assert resource_title is not None and resource_title != ''


def test_resource_slug_is_not_empty():
    resource_slug = response_api_json['pageProps']['slug']
    assert resource_slug is not None and resource_slug != ''


def test_resource_subtitle_is_not_empty():
    resource_subtitle = response_api_json['pageProps']['pageSubTitle']
    assert resource_subtitle is not None and resource_subtitle != ''


def test_resource_hero_image_is_not_empty():
    resource_hero_img = response_api_json['pageProps']['resourceHeroImage']
    assert resource_hero_img is not None and resource_hero_img != ''


def test_list_resource_category_collection_is_not_empty():
    list_resource_collection = response_api_json['pageProps']['categoriesCollection']['items']
    assert list_resource_collection is not None and list_resource_collection != '' and len(list_resource_collection) != 0

# page elements


def test_list_page_elements_is_not_empty():
    resource_elements = response_api_json['pageProps']['resourceCardsCollection']['items']
    assert resource_elements is not None and resource_elements != '' and len(resource_elements) != 0


def test_page_elements_collection_is_not_empty():
    resource_elements = response_api_json['pageProps']['resourceCardsCollection']['items']
    count = 0
    p, l, a, v,  = 'Missing pdf', 'Missing link', 'Missing audio', 'Missing video'
    for resource_element in resource_elements:
        if resource_element['resourceType'] == 'PDF' and resource_element['resourceLink'] is not None:
            p = ''
            count += 1
        if resource_element['resourceType'] == 'External Link' and resource_element['resourceLink'] is not None:
            l = ''
            count += 1
        if resource_element['resourceType'] == 'Audio' and resource_element['resourceEmbedCode'] is not None:
            a = ''
            count += 1
        if resource_element['resourceType'] == 'Video' and resource_element['resourceEmbedCode'] is not None:
            v = ''
            count += 1
    assert count == 4, f'{p}{l}{a}{v}'
