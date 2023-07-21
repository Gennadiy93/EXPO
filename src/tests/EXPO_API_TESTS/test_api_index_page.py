from src.EXPO_API.API.API import API

import pytest

try:
    api = API()
    response_api = api.get_index_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_index_json():
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


def test_list_services_is_not_empty():
    list_services = response_api_json['pageProps']['services']
    assert list_services is not None and list_services != '' and len(list_services) != 0


def test_list_resources_is_not_empty():
    list_resources = response_api_json['pageProps']['resources']
    assert list_resources is not None and list_resources != '' and len(list_resources) != 0


def test_home_slider_collection_is_not_empty():
    home_slider_collection = response_api_json['pageProps']['homeSliderCollection']
    assert home_slider_collection is not None and home_slider_collection != '' and len(home_slider_collection) != 0


def test_story_slider_is_not_empty():
    story_slider = response_api_json['pageProps']['storyslider']
    assert story_slider is not None and story_slider != '' and len(story_slider) != 0


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''


def test_hero_image_is_not_empty():
    hero_image = response_api_json['pageProps']['heroImage']['url']
    assert hero_image is not None and hero_image != ''
