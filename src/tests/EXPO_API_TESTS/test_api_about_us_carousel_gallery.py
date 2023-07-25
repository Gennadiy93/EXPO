from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_about_us_carousel_gallery_type_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_about_us_carousel_gallery_type_page():
    assert status_code_api == 200


def test_about_us_carousel_gallery_type_title_is_not_empty():
    about_us_carousel_gallery_type_title = response_api_json['pageProps']['pageData']['pageTitle']
    assert about_us_carousel_gallery_type_title is not None and about_us_carousel_gallery_type_title != ''


def test_about_us_carousel_gallery_type_slug_is_not_empty():
    about_us_carousel_gallery_type_slug = response_api_json['pageProps']['pageData']['slug']
    assert about_us_carousel_gallery_type_slug is not None and about_us_carousel_gallery_type_slug != ''


def test_about_us_carousel_gallery_type_header_style_is_not_empty():
    about_us_carousel_gallery_type_header_style = response_api_json['pageProps']['pageData']['headerStyleType']
    assert about_us_carousel_gallery_type_header_style is not None and about_us_carousel_gallery_type_header_style != '' and about_us_carousel_gallery_type_header_style == 'Carousel Gallery'


def test_about_us_carousel_gallery_type_subtitle_is_not_empty():
    about_us_carousel_gallery_type_subtitle = response_api_json['pageProps']['pageData']['pageSubTitle']
    assert about_us_carousel_gallery_type_subtitle is not None and about_us_carousel_gallery_type_subtitle != ''


def test_about_us_carousel_gallery_type_hero_img_is_none():
    about_us_carousel_gallery_type_hero_img = response_api_json['pageProps']['pageData']['heroImage']
    assert about_us_carousel_gallery_type_hero_img is None


def test_about_us_carousel_gallery_type_images_is_not_none():
    about_us_carousel_gallery_type_images = response_api_json['pageProps']['pageData']['images']
    assert about_us_carousel_gallery_type_images is not None and about_us_carousel_gallery_type_images != ''


def test_about_us_carousel_gallery_type_individuals_title_is_not_empty():
    about_us_carousel_gallery_type_individuals_title = response_api_json['pageProps']['pageData']['organizationSectionTitle']
    assert about_us_carousel_gallery_type_individuals_title is not None and about_us_carousel_gallery_type_individuals_title != ''


def test_about_us_carousel_gallery_type_individuals_collection_is_not_empty():
    about_us_carousel_gallery_type_individuals_collection = response_api_json['pageProps']['pageData']['individualsCollection']['items']
    assert about_us_carousel_gallery_type_individuals_collection is not None and about_us_carousel_gallery_type_individuals_collection != '' and len(about_us_carousel_gallery_type_individuals_collection) != 0


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''