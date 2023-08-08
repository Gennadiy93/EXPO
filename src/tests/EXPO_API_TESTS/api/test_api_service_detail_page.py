from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_service_detail_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_service_detail_page():
    assert status_code_api == 200


def test_service_title_is_not_empty():
    service_title = response_api_json['pageProps']['pageTitle']
    assert service_title is not None and service_title != ''


def test_service_slug_is_not_empty():
    service_slug = response_api_json['pageProps']['slug']
    assert service_slug is not None and service_slug != ''


def test_service_subtitle_is_not_empty():
    service_subtitle = response_api_json['pageProps']['pageSubTitle']
    assert service_subtitle is not None and service_subtitle != ''


def test_service_hero_image_is_not_empty():
    service_hero_img = response_api_json['pageProps']['serviceHeroImage']
    assert service_hero_img is not None and service_hero_img != ''


def test_service_enquiry_form_title_is_not_empty():
    enquiry_form_title = response_api_json['pageProps']['enquiryForm']['enquiryFormTitle']
    assert enquiry_form_title is not None and enquiry_form_title != ''


def test_list_service_category_collection_is_not_empty():
    list_service_collection = response_api_json['pageProps']['serviceCategoriesCollection']['items']
    assert list_service_collection is not None and list_service_collection != '' and len(list_service_collection) != 0


def test_list_service_pillar_collection_is_not_empty():
    list_service_pillar_collection = response_api_json['pageProps']['pillars']
    assert list_service_pillar_collection is not None and list_service_pillar_collection != '' and len(list_service_pillar_collection) != 0


# related services


def test_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['services']
    assert related_services is not None and related_services != '' and len(related_services) != 0


def test_title_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['services']
    for service in related_services:
        assert service['pageTitle'] is not None and service['pageTitle'] != '', f'Missing service title{service}'


def test_slug_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['services']
    for service in related_services:
        assert service['slug'] is not None and service['slug'] != '', f'Missing service slug{service}'


def test_thumbnail_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['services']
    for service in related_services:
        assert service['serviceThumbnail'] is not None and service['serviceThumbnail'] != '', f'Missing service thumbnail{service}'


def test_pillar_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['services']
    for service in related_services:
        assert service['pillars'] is not None and service['pillars'] != '', f'Missing service pillar{service}'


def test_category_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['services']
    for service in related_services:
        assert service['serviceCategoriesCollection'] is not None and service['serviceCategoriesCollection'] != '', f'Missing service category{service}'


# related resources


def test_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['relatedResources']
    assert related_resources is not None and related_resources != '' and len(related_resources) != 0


def test_title_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['relatedResources']
    for resource in related_resources:
        assert resource['title'] is not None and resource['title'] != '', f'Missing resource title{resource}'


def test_slug_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['relatedResources']
    for resource in related_resources:
        assert resource['slug'] is not None and resource['slug'] != '', f'Missing resource slug{resource}'


def test_thumbnail_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['relatedResources']
    for resource in related_resources:
        assert resource['resourceThumbnail'] is not None and resource['resourceThumbnail'] != '', f'Missing resource thumbnail{resource}'


def test_categories_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['relatedResources']
    for resource in related_resources:
        assert resource['categoriesCollection'] is not None and resource['categoriesCollection'] != '', f'Missing resource categories{resource}'


# related events

def test_list_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['relatedEvents']
    assert related_events is not None and related_events != '' and len(related_events) != 0


def test_title_event_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['relatedEvents']
    for event in related_events:
        assert event['pageTitle'] is not None and event['pageTitle'] != '', f'Missing event title{event}'


def test_slug_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['relatedEvents']
    for event in related_events:
        assert event['slug'] is not None and event['slug'] != '', f'Missing event slug{event}'


def test_category_collection_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['relatedEvents']
    for event in related_events:
        assert event['categoriesCollection'] is not None and event['categoriesCollection'] != '', f'Missing event category{event}'


def test_thumbnail_image_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['relatedEvents']
    for event in related_events:
        assert event['eventHeroSquareImage'] is not None and event['eventHeroSquareImage'] != '', f'Missing event thumbnail{event}'


def test_event_type_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['relatedEvents']
    for event in related_events:
        assert event['eventType'] is not None and event['eventType'] != '', f'Missing event type{event}'


def test_time_event_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['relatedEvents']
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
# page elements


def test_list_page_elements_is_not_empty():
    service_elements = response_api_json['pageProps']['elements']
    assert service_elements is not None and service_elements != '' and len(service_elements) != 0


def test_page_elements_collection_is_not_empty():
    service_elements = response_api_json['pageProps']['elements']
    count = 0
    q, y, p, im, e = 'Missing quote', 'Missing youtube', 'Missing paragraph', 'Missing images', 'Missing embed '
    for service_element in service_elements:
        quote = service_element.get('quoteText')
        if quote is not None and quote != '':
            q = ''
            count += 1
        youtube = service_element.get('youtubeLink')
        if youtube is not None and quote != '':
            y = ''
            count += 1
        paragraph = service_element.get('storyPageParagraph')
        if paragraph is not None and quote != '':
            p = ''
            count += 1
        images = service_element.get('imagesCollection')
        if images is not None and quote != '':
            im = ''
            count += 1
        embed = service_element.get('embedCode')
        if embed is not None and quote != '':
            e = ''
            count += 1
    assert count == 5, f'{q}{y}{p}{im}{e}'
