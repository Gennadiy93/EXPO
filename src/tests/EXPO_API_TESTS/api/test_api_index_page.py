from src.EXPO_API.API import API
import pytest

try:
    api = API()
    response_api = api.get_index_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_index_page():
    assert status_code_api == 200


def test_home_title_is_not_empty():
    home_title = response_api_json['pageProps']['homeTitle']
    assert home_title is not None and home_title != ''


def test_home_description_is_not_empty():
    home_desc = response_api_json['pageProps']['homeDesc']
    assert home_desc is not None and home_desc != ''


def test_story_title_is_not_empty():
    story_title = response_api_json['pageProps']['storyTitle']
    assert story_title is not None and story_title != ''


def test_story_description_is_not_empty():
    story_desc = response_api_json['pageProps']['storyDesc']
    assert story_desc is not None and story_desc != '', 'Empty response body in story description'


def test_service_title_is_not_empty():
    service_title = response_api_json['pageProps']['servicesTitle']
    assert service_title is not None and service_title != ''


def test_services_desc_is_not_empty():
    service_desc = response_api_json['pageProps']['servicesDesc']
    assert service_desc is not None and service_desc != ''


def test_resource_title_is_not_empty():
    resource_title = response_api_json['pageProps']['resourcesTitle']
    assert resource_title is not None and resource_title != ''


def test_resource_desc_is_not_empty():
    resource_desc = response_api_json['pageProps']['resourcesDesc']
    assert resource_desc is not None and resource_desc != ''


def test_contact_us_form_title_is_not_empty():
    contact_us_form_title = response_api_json['pageProps']['contactUsFormTitle']
    assert contact_us_form_title is not None and contact_us_form_title != ''


def test_contact_us_form_description_is_not_empty():
    contact_us_form_desc = response_api_json['pageProps']['contactUsFormDescription']
    assert contact_us_form_desc is not None and contact_us_form_desc != ''


@pytest.mark.asyncio
async def test_list_services_is_not_empty():
    list_services = response_api_json['pageProps']['services']
    assert list_services is not None and list_services != '' and len(list_services) != 0


def test_pillar_title_in_list_services_is_not_empty():
    list_services = response_api_json['pageProps']['services']
    for services in list_services:
        assert services['pillarTitle'] is not None and services[
            'pillarTitle'] != '', f'Missing pillar title, {services}'


def test_pillar_image_in_list_services_is_not_empty():
    list_services = response_api_json['pageProps']['services']
    for services in list_services:
        assert services['pillarImage'] is not None and services['pillarImage'] != '', f'Missing pillar image{services}'


def test_list_resources_is_not_empty():
    list_resources = response_api_json['pageProps']['resources']
    assert list_resources is not None and list_resources != '' and len(list_resources) != 0


def test_resource_title_in_list_resources_is_not_empty():
    list_resources = response_api_json['pageProps']['resources']
    for resource in list_resources:
        assert resource['title'] is not None and resource['title'] != '', f'Missing resource title{resource}'


def test_resource_slug_in_list_resources_is_not_empty():
    list_resources = response_api_json['pageProps']['resources']
    for resource in list_resources:
        assert resource['slug'] is not None and resource['slug'] != '', f'Missing resource slug{resource}'


def test_resource_thumbnail_in_list_resources_is_not_empty():
    list_resources = response_api_json['pageProps']['resources']
    for resource in list_resources:
        assert resource['resourceThumbnail'] is not None and resource[
            'resourceThumbnail'] != '', f'Missing resource thumbnail{resource}'


def test_categories_collection_in_list_resources_is_not_empty():
    list_resources = response_api_json['pageProps']['resources']
    for resource in list_resources:
        assert resource['categoriesCollection'] is not None and resource['categoriesCollection'] != '' and len(
            resource['categoriesCollection']) != 0, f'Missing resource categories{resource}'


def test_home_slider_collection_is_not_empty():
    home_slider_collection = response_api_json['pageProps']['homeSliderCollection']
    assert home_slider_collection is not None and home_slider_collection != '' and len(home_slider_collection) != 0


def test_page_title_in_home_slider_collection_is_not_empty():
    home_slider_collection = response_api_json['pageProps']['homeSliderCollection']
    for item in home_slider_collection:
        if 'pageTitle' in item.keys():
            assert item['pageTitle'] is not None and item['pageTitle'] != '', f'Missing page title{item}'
        elif 'newsTitle' in item.keys():
            assert item['newsTitle'] is not None and item['newsTitle'] != '', f'Missing news title{item}'


def test_slug_in_home_slider_collection_is_not_empty():
    home_slider_collection = response_api_json['pageProps']['homeSliderCollection']
    for item in home_slider_collection:
        if 'pageTitle' in item.keys():
            assert item['slug'] is not None and item['slug'] != '', f'{item}, Missing page slug'
        elif 'newsTitle' in item.keys():
            assert item['newsCtaBtnLink'] is not None and item['newsCtaBtnLink'] != '', f'Missing news link{item}'


def test_thumbnail_in_home_slider_collection_is_not_empty():
    home_slider_collection = response_api_json['pageProps']['homeSliderCollection']
    for item in home_slider_collection:
        if 'onlineEventOpeningHoursNew' in item.keys():
            assert item['futureBannerEvent'] is not None and item[
                'futureBannerEvent'] != '', f'Missing event banner{item}'
        elif 'newsTitle' in item.keys():
            assert item['futureBannerNews'] is not None and item['futureBannerNews'] != '', f'Missing news banner{item}'


def test_tag_in_home_slider_collection_is_not_empty():
    home_slider_collection = response_api_json['pageProps']['homeSliderCollection']
    for item in home_slider_collection:
        if 'pageTitle' in item.keys():
            assert item['tag'] is not None and item['tag'] != '', f'Missing tag{item}'
        elif 'newsTitle' in item.keys():
            assert item['tag'] is not None and item['tag'] != '', f'Missing tag{item}'


def test_story_slider_is_not_empty():
    story_slider = response_api_json['pageProps']['storyslider']
    assert story_slider is not None and story_slider != '' and len(story_slider) != 0


def test_story_title_in_list_stories_is_not_empty():
    story_slider = response_api_json['pageProps']['storyslider']
    for story in story_slider:
        assert story['pageTitle'] is not None and story['pageTitle'] != '', f'Missing story title{story}'


def test_story_slug_in_list_stories_is_not_empty():
    story_slider = response_api_json['pageProps']['storyslider']
    for story in story_slider:
        assert story['slug'] is not None and story['slug'] != '', f'Missing story title{story}'


def test_story_thumbnail_in_list_stories_is_not_empty():
    story_slider = response_api_json['pageProps']['storyslider']
    for story in story_slider:
        assert story['heroSquareImage'] is not None and story[
            'heroSquareImage'] != '', f'Missing story thumbnail{story}'


def test_categories_collection_in_list_stories_is_not_empty():
    story_slider = response_api_json['pageProps']['storyslider']
    for story in story_slider:
        assert story['categoriesCollection'] is not None and story['categoriesCollection'] != '' and len(
            story['categoriesCollection']) != 0, f'Missing story categories{story}'


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''


def test_hero_image_is_not_empty():
    hero_image = response_api_json['pageProps']['heroImage']
    assert hero_image is not None and hero_image != ''
