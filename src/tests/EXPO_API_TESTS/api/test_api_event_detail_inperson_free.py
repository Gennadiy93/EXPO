from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_inperson_free_event_detail_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_inperson_free_event_detail_page():
    assert status_code_api == 200


def test_inperson_free_title_is_not_empty():
    inperson_free_title = response_api_json['pageProps']['event']['pageTitle']
    assert inperson_free_title is not None and inperson_free_title != ''


def test_inperson_free_slug_is_not_empty():
    inperson_free_slug = response_api_json['pageProps']['event']['slug']
    assert inperson_free_slug is not None and inperson_free_slug != ''


def test_inperson_free_price_is_empty():
    inperson_free_price = response_api_json['pageProps']['event']['pricingNumber']
    assert inperson_free_price is None


def test_inperson_free_platinum_list_url_is_empty():
    inperson_free_platinum_list_url = response_api_json['pageProps']['event']['platinumListUrl']
    assert inperson_free_platinum_list_url is None


def test_inperson_free_event_type_is_not_empty():
    inperson_free_event_type = response_api_json['pageProps']['event']['eventType']
    assert inperson_free_event_type == 'In-Person'


def test_inperson_free_event_opening_hours_is_not_empty():
    inperson_free_event_opening_hours = response_api_json['pageProps']['event']['inPersonOpeningHoursNew']
    assert inperson_free_event_opening_hours is not None and inperson_free_event_opening_hours != ''


def test_inperson_free_list_category_collection_is_not_empty():
    list_category_collection = response_api_json['pageProps']['event']['categoriesCollection']['items']
    assert list_category_collection is not None and list_category_collection != '' and len(list_category_collection) != 0


def test_inperson_free_slider_images_is_not_empty():
    slider_images = response_api_json['pageProps']['event']['images']
    assert slider_images is not None and slider_images != ''


def test_inperson_free_banner_image_is_not_empty():
    banner_image = response_api_json['pageProps']['event']['eventHeroLandscapeImage']
    assert banner_image is not None and banner_image != ''


def test_inperson_free_hero_image_is_not_empty():
    hero_image = response_api_json['pageProps']['event']['heroImage']
    assert hero_image is not None and hero_image != ''


def test_inperson_free_agenda_collection_is_not_empty():
    agenda_collection = response_api_json['pageProps']['event']['agenta']
    assert agenda_collection is not None and agenda_collection != '' and len(agenda_collection) != 0


def test_inperson_free_speaker_group_is_not_empty():
    speaker_group = response_api_json['pageProps']['event']['speakers']['speakersGroups']
    assert speaker_group is not None and speaker_group != '' and len(speaker_group) != 0


def test_inperson_free_list_speakers_is_not_empty():
    speakers = response_api_json['pageProps']['event']['speakers']['speakers']
    assert speakers is not None and speakers != '' and len(speakers) != 0


def test_inperson_free_list_terms_is_not_empty():
    terms = response_api_json['pageProps']['event']['terms']
    assert terms is not None and terms != '' and len(terms) != 0


def test_inperson_free_event_location_is_not_empty():
    terms = response_api_json['pageProps']['event']['eventLocation']
    assert terms is not None and terms != ''


# related services


def test_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['event']['relatedServices']
    assert related_services is not None and related_services != '' and len(related_services) != 0


def test_title_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['event']['relatedServices']
    for service in related_services:
        assert service['pageTitle'] is not None and service['pageTitle'] != '', f'Missing service title{service}'


def test_slug_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['event']['relatedServices']
    for service in related_services:
        assert service['slug'] is not None and service['slug'] != '', f'Missing service slug{service}'


def test_thumbnail_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['event']['relatedServices']
    for service in related_services:
        assert service['serviceThumbnail'] is not None and service['serviceThumbnail'] != '', f'Missing service thumbnail{service}'


def test_pillar_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['event']['relatedServices']
    for service in related_services:
        assert service['pillars'] is not None and service['pillars'] != '', f'Missing service pillar{service}'


def test_category_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['event']['relatedServices']
    for service in related_services:
        assert service['serviceCategoriesCollection'] is not None and service['serviceCategoriesCollection'] != '', f'Missing service category{service}'


# related resources


def test_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['event']['relatedResources']
    assert related_resources is not None and related_resources != '' and len(related_resources) != 0


def test_title_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['event']['relatedResources']
    for resource in related_resources:
        assert resource['title'] is not None and resource['title'] != '', f'Missing resource title{resource}'


def test_slug_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['event']['relatedResources']
    for resource in related_resources:
        assert resource['slug'] is not None and resource['slug'] != '', f'Missing resource slug{resource}'


def test_thumbnail_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['event']['relatedResources']
    for resource in related_resources:
        assert resource['resourceThumbnail'] is not None and resource['resourceThumbnail'] != '', f'Missing resource thumbnail{resource}'


def test_categories_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['event']['relatedResources']
    for resource in related_resources:
        assert resource['categoriesCollection'] is not None and resource['categoriesCollection'] != '', f'Missing resource categories{resource}'


# related events

def test_list_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['event']['relatedEvents']
    assert related_events is not None and related_events != '' and len(related_events) != 0


def test_title_event_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['event']['relatedEvents']
    for event in related_events:
        assert event['pageTitle'] is not None and event['pageTitle'] != '', f'Missing event title{event}'


def test_slug_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['event']['relatedEvents']
    for event in related_events:
        assert event['slug'] is not None and event['slug'] != '', f'Missing event slug{event}'


def test_category_collection_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['event']['relatedEvents']
    for event in related_events:
        assert event['categoriesCollection'] is not None and event['categoriesCollection'] != '', f'Missing event category{event}'


def test_thumbnail_image_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['event']['relatedEvents']
    for event in related_events:
        assert event['eventHeroSquareImage'] is not None and event['eventHeroSquareImage'] != '', f'Missing event thumbnail{event}'


def test_event_type_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['event']['relatedEvents']
    for event in related_events:
        assert event['eventType'] is not None and event['eventType'] != '', f'Missing event type{event}'


def test_time_event_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['event']['relatedEvents']
    o, p, h = 'Missing time virtual event', 'Missing time inperson event', 'Missing time hybrid event',
    for event in related_events:
        if event['eventType'] == 'Virtual' and event['onlineEventOpeningHoursNew'] is not None and event['onlineEventOpeningHoursNew'] != '':
            o = ''
        elif event['eventType'] == 'In-Person' and event['inPersonOpeningHoursNew'] is not None and event['inPersonOpeningHoursNew'] != '':
            p = ''
        elif event['eventType'] == 'In-Person & Virtual' and event['inPersonOpeningHoursNew'] is not None and event['inPersonOpeningHoursNew'] != '' and event[
                'onlineEventOpeningHoursNew'] is not None and event['onlineEventOpeningHoursNew'] != '':
            h = ''
    assert o + p + h == '', f'{o}, {p}, {h}'


def test_marketing_banner_is_not_empty():
    marketing_banner = response_api_json['pageProps']['marketingBanner']
    assert marketing_banner is not None and marketing_banner != ''