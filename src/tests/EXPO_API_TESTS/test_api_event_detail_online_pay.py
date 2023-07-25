from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_online_pay_event_detail_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_online_pay_event_detail_page():
    assert status_code_api == 200


def test_online_pay_title_is_not_empty():
    online_pay_title = response_api_json['pageProps']['event']['pageTitle']
    assert online_pay_title is not None and online_pay_title != ''


def test_online_pay_slug_is_not_empty():
    online_pay_slug = response_api_json['pageProps']['event']['slug']
    assert online_pay_slug is not None and online_pay_slug != ''


def test_online_pay_price_is_not_empty():
    online_pay_price = response_api_json['pageProps']['event']['pricingOnlineNumber']
    assert online_pay_price is not None and online_pay_price != ''


def test_online_pay_price_vod_is_not_empty():
    online_pay_price = response_api_json['pageProps']['event']['priceVod']
    assert online_pay_price is not None and online_pay_price != ''


def test_online_pay_finished():
    has_finished = response_api_json['pageProps']['event']['eventHasEnded']
    assert has_finished == True


def test_online_pay_mimic_event_url_is_not_empty():
    online_pay_mimic_event_url = response_api_json['pageProps']['event']['mimicEventUrl']
    assert online_pay_mimic_event_url is not None and online_pay_mimic_event_url != ''


def test_online_pay_event_type_is_not_empty():
    online_pay_event_type = response_api_json['pageProps']['event']['eventType']
    assert online_pay_event_type == 'Virtual'


def test_online_pay_event_opening_hours_is_not_empty():
    online_pay_event_opening_hours = response_api_json['pageProps']['event']['onlineEventOpeningHoursNew']
    assert online_pay_event_opening_hours is not None and online_pay_event_opening_hours != ''


def test_online_pay_slider_images_is_not_empty():
    slider_images = response_api_json['pageProps']['event']['images']
    assert slider_images is not None and slider_images != ''


def test_online_pay_banner_image_is_not_empty():
    banner_image = response_api_json['pageProps']['event']['eventHeroLandscapeImage']
    assert banner_image is not None and banner_image != ''


def test_online_pay_hero_video_is_not_empty():
    hero_video = response_api_json['pageProps']['event']['heroVideo']
    assert hero_video is not None and hero_video != ''


def test_online_pay_hero_image_is_empty():
    hero_image = response_api_json['pageProps']['event']['heroImage']
    assert hero_image is None

