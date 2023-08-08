from src.EXPO_API.API import API

try:
    api = API()
    response_api = api.get_story_detail_page()
    status_code_api = response_api['status']
    response_api_json = response_api['json']
except BaseException:
    raise Exception('Error')


def test_status_code_story_detail_page():
    assert status_code_api == 200


def test_story_title_is_not_empty():
    story_title = response_api_json['pageProps']['story']['pageTitle']
    assert story_title is not None and story_title != ''


def test_story_slug_is_not_empty():
    story_slug = response_api_json['pageProps']['story']['slug']
    assert story_slug is not None and story_slug != ''


def test_story_subtitle_is_not_empty():
    story_subtitle = response_api_json['pageProps']['story']['pageSubTitle']
    assert story_subtitle is not None and story_subtitle != ''


def test_story_hero_image_is_not_empty():
    story_hero_img = response_api_json['pageProps']['story']['heroLandscapeImage']
    assert story_hero_img is not None and story_hero_img != ''


def test_story_contact_us_form_title_is_not_empty():
    contact_us_form_title = response_api_json['pageProps']['story']['enquiryForm']['items']
    assert contact_us_form_title is not None and contact_us_form_title != ''


def test_list_story_category_collection_is_not_empty():
    list_story_collection = response_api_json['pageProps']['story']['categoriesCollection']
    assert list_story_collection is not None and list_story_collection != '' and len(list_story_collection) != 0


def test_story_pledge_is_not_empty():
    story_pledge = response_api_json['pageProps']['story']['pledge']
    assert story_pledge is not None and story_pledge != ''


def test_individuals_is_not_empty():
    individuals = response_api_json['pageProps']['story']['individualsCollection']['items']
    assert individuals is not None and individuals != '' and len(individuals) != 0

# related services


def test_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['story']['servicesCollection']['items']
    assert related_services is not None and related_services != '' and len(related_services) != 0


def test_title_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['story']['servicesCollection']['items']
    for service in related_services:
        assert service['pageTitle'] is not None and service['pageTitle'] != '', f'Missing service title{service}'


def test_slug_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['story']['servicesCollection']['items']
    for service in related_services:
        assert service['slug'] is not None and service['slug'] != '', f'Missing service slug{service}'


def test_thumbnail_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['story']['servicesCollection']['items']
    for service in related_services:
        assert service['serviceThumbnail'] is not None and service['serviceThumbnail'] != '', f'Missing service thumbnail{service}'


def test_pillar_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['story']['servicesCollection']['items']
    for service in related_services:
        assert service['pillars'] is not None and service['pillars'] != '', f'Missing service pillar{service}'


def test_category_in_list_related_services_is_not_empty():
    related_services = response_api_json['pageProps']['story']['servicesCollection']['items']
    for service in related_services:
        assert service['serviceCategoriesCollection'] is not None and service['serviceCategoriesCollection'] != '', f'Missing service category{service}'


# related resources


def test_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['story']['relatedResourcesCollection']['items']
    assert related_resources is not None and related_resources != '' and len(related_resources) != 0


def test_title_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['story']['relatedResourcesCollection']['items']
    for resource in related_resources:
        assert resource['title'] is not None and resource['title'] != '', f'Missing resource title{resource}'


def test_slug_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['story']['relatedResourcesCollection']['items']
    for resource in related_resources:
        assert resource['slug'] is not None and resource['slug'] != '', f'Missing resource slug{resource}'


def test_thumbnail_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['story']['relatedResourcesCollection']['items']
    for resource in related_resources:
        assert resource['resourceThumbnail'] is not None and resource['resourceThumbnail'] != '', f'Missing resource thumbnail{resource}'


def test_categories_in_list_related_resources_is_not_empty():
    related_resources = response_api_json['pageProps']['story']['relatedResourcesCollection']['items']
    for resource in related_resources:
        assert resource['categoriesCollection'] is not None and resource['categoriesCollection'] != '', f'Missing resource categories{resource}'


# related events

def test_list_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['story']['relatedEventsCollection']['items']
    assert related_events is not None and related_events != '' and len(related_events) != 0


def test_title_event_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['story']['relatedEventsCollection']['items']
    for event in related_events:
        assert event['pageTitle'] is not None and event['pageTitle'] != '', f'Missing event title{event}'


def test_slug_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['story']['relatedEventsCollection']['items']
    for event in related_events:
        assert event['slug'] is not None and event['slug'] != '', f'Missing event slug{event}'


def test_category_collection_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['story']['relatedEventsCollection']['items']
    for event in related_events:
        assert event['categoriesCollection'] is not None and event['categoriesCollection'] != '', f'Missing event category{event}'


def test_thumbnail_image_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['story']['relatedEventsCollection']['items']
    for event in related_events:
        assert event['eventHeroSquareImage'] is not None and event['eventHeroSquareImage'] != '', f'Missing event thumbnail{event}'


def test_event_type_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['story']['relatedEventsCollection']['items']
    for event in related_events:
        assert event['eventType'] is not None and event['eventType'] != '', f'Missing event type{event}'


def test_time_event_in_related_events_is_not_empty():
    related_events = response_api_json['pageProps']['story']['relatedEventsCollection']['items']
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
    story_elements = response_api_json['pageProps']['story']['relatedResourcesCollection']['items']
    assert story_elements is not None and story_elements != '' and len(story_elements) != 0


def test_page_elements_collection_is_not_empty():
    story_elements = response_api_json['pageProps']['story']['pageStoryElementsCollection']['items']
    count = 0
    q, y, p, im, e = 'Missing quote', 'Missing youtube', 'Missing paragraph', 'Missing images', 'Missing embed '
    for story_element in story_elements:
        quote = story_element.get('quoteText')
        if quote is not None and quote != '':
            q = ''
            count += 1
        youtube = story_element.get('youtubeLink')
        if youtube is not None and quote != '':
            y = ''
            count += 1
        paragraph = story_element.get('storyPageParagraph')
        if paragraph is not None and quote != '':
            p = ''
            count += 1
        images = story_element.get('imagesCollection')
        if images is not None and quote != '':
            im = ''
            count += 1
        embed = story_element.get('embedCode')
        if embed is not None and quote != '':
            e = ''
            count += 1
    assert count == 5, f'{q}{y}{p}{im}{e}'
