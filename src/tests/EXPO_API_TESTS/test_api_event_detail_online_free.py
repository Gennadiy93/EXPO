from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_online_free_event_detail_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_online_free_event_detail_page():
    assert status_code_api == 200


def test_online_free_title_is_not_empty():
    online_free_title = response_api_json['pageProps']['event']['pageTitle']
    assert online_free_title is not None and online_free_title != ''


def test_online_free_slug_is_not_empty():
    online_free_slug = response_api_json['pageProps']['event']['slug']
    assert online_free_slug is not None and online_free_slug != ''


def test_online_free_price_is_empty():
    online_free_price = response_api_json['pageProps']['event']['pricingOnlineNumber']
    assert online_free_price is None


def test_online_free_price_vod_is_empty():
    online_free_price = response_api_json['pageProps']['event']['priceVod']
    assert online_free_price == 0


def test_online_free_event_no_finished():
    has_finished = response_api_json['pageProps']['event']['eventHasEnded']
    assert has_finished == False


def test_online_free_mimic_event_url_is_not_empty():
    online_free_mimic_event_url = response_api_json['pageProps']['event']['mimicEventUrl']
    assert online_free_mimic_event_url is not None and online_free_mimic_event_url != ''


def test_online_free_event_type_is_not_empty():
    online_free_event_type = response_api_json['pageProps']['event']['eventType']
    assert online_free_event_type == 'Virtual'


def test_online_free_event_opening_hours_is_not_empty():
    online_free_event_opening_hours = response_api_json['pageProps']['event']['onlineEventOpeningHoursNew']
    assert online_free_event_opening_hours is not None and online_free_event_opening_hours != ''


def test_online_free_slider_images_is_not_empty():
    slider_images = response_api_json['pageProps']['event']['images']
    assert slider_images is not None and slider_images != ''


def test_online_free_banner_image_is_not_empty():
    banner_image = response_api_json['pageProps']['event']['eventHeroLandscapeImage']
    assert banner_image is not None and banner_image != ''


def test_online_free_hero_video_is_empty():
    hero_video = response_api_json['pageProps']['event']['heroVideo']
    assert hero_video is None


def test_online_free_hero_image_is_not_empty():
    hero_image = response_api_json['pageProps']['event']['heroImage']
    assert hero_image is not None and hero_image != ''

