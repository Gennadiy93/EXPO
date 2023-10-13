# driver
chrome_windows_path = r"C:\webdrivers\chromed-win64\chrome.exe"

# env select master or staging
env = 'staging'

# API urls: check actual url
url_staging_API = 'https://expo-dubai-group-staging-git-master-world-expo.vercel.app/_next/data/zzvu5x5ZFyPabacQmlJ1E'
url_master_API = 'https://expodubaigroup.com/_next/data/dn1hgomMNPMg4lKedeI_Z'
url_staging = 'https://expo-dubai-group-staging-git-master-world-expo.vercel.app/'
url_master = 'https://expodubaigroup.com/'

story_slug = 'api-story-detail'
service_slug = 'api-test-service-detail'
resource_slug = 'api-resource-detail'
about_us_empty_type_slug = 'api-about-us-empty-type-page'
about_us_carousel_gallery_type_slug = 'api-about-us-carousel-gallery-type-page'
about_us_hero_img_type_slug = 'api-about-us-heroimg-type-page'
event_inperson_free_slug = 'api-inperson-free-event-with-slider-and-heroimg-detail'
event_inperson_pay_slug = 'api-inperson-pay-event-with-video-no-heroimg-detail'
event_online_pay_slug = 'api-online-pay-event-with-video-no-heroimg-detail'
event_online_free_slug = 'api-online-free-event-with-slider-and-heroimg-detail'

url = {}


def generate_link():
    if env == 'staging':
        url['url_home'] = f'{url_staging}'
        url['url_impact'] = f'{url_staging}impact'
        url['url_services'] = f'{url_staging}services'
        url['url_resources'] = f'{url_staging}resources'
        url['url_story_detail'] = f'{url_staging}impact/{story_slug}'
        url['url_event_inperson_free_detail'] = f'{url_staging}events/{event_inperson_free_slug}'
        url['url_api'] = f'{url_staging_API}'
        url['url_api_index_page'] = f'{url_staging_API}/index.json'
        url['url_api_impact_page'] = f'{url_staging_API}/impact.json'
        url['url_api_events_page'] = f'{url_staging_API}/events.json'
        url['url_api_services_page'] = f'{url_staging_API}/services.json'
        url['url_api_resources_page'] = f'{url_staging_API}/resources.json'
        url['url_api_story_detail_page'] = f'{url_staging_API}/impact/{story_slug}.json?slug={story_slug}'
        url['url_api_service_detail_page'] = f'{url_staging_API}/services/{service_slug}.json?slug={service_slug}'
        url['url_api_resource_detail_page'] = f'{url_staging_API}/resources/{resource_slug}.json?slug={resource_slug}'
        url[
            'url_api_about_us_empty_type_page'] = f'{url_staging_API}/about-us/{about_us_empty_type_slug}.json?slug={about_us_empty_type_slug}'
        url[
            'url_api_about_us_carousel_gallery_type_page'] = f'{url_staging_API}/about-us/{about_us_carousel_gallery_type_slug}.json?slug={about_us_carousel_gallery_type_slug}'
        url[
            'url_api_about_us_hero_img_type_page'] = f'{url_staging_API}/about-us/{about_us_hero_img_type_slug}.json?slug={about_us_hero_img_type_slug}'
        url[
            'url_api_inperson_free_event_detail_page'] = f'{url_staging_API}/events/{event_inperson_free_slug}.json?slug={event_inperson_free_slug}'
        url[
            'url_api_inperson_pay_event_detail_page'] = f'{url_staging_API}/events/{event_inperson_pay_slug}.json?slug={event_inperson_pay_slug}'
        url[
            'url_api_online_free_event_detail_page'] = f'{url_staging_API}/events/{event_online_free_slug}.json?slug={event_online_free_slug}'
        url[
            'url_api_online_pay_event_detail_page'] = f'{url_staging_API}/events/{event_online_pay_slug}.json?slug={event_online_pay_slug}'
        url['url_support_page'] = f'https://www.expocitydubai.com/en/plan-your-visit-1/support/'
        url['url_media_page'] = f'https://www.expocitydubai.com/en/media-centre/'
        url['url_legal_page'] = f'https://www.expocitydubai.com/en/legals/privacy-policy/'
        url['url_expo_city_dubai_page'] = f'https://www.expocitydubai.com/en/'
        url['url_virtual_expo_dubai_page'] = f'https://virtualexpodubai.com/'
        url['url_expo_2020_page'] = f'https://expo2020dubai.com/'
        url['url_tiktok_page'] = f'https://www.tiktok.com/@expocitydubai'
        url['url_instagram_page'] = f'https://www.instagram.com/expocitydubai/'
        url['url_facebook_page'] = f'https://www.facebook.com/Expo2020Dubai'
        url['url_twitter_page'] = f'https://twitter.com/expocitydubai'
        url['url_linkedin_page'] = f'https://www.linkedin.com/uas/login?session_redirect=%2Fcompany%2F26639576%2F'
        url['url_youtube_page'] = f'https://www.youtube.com/channel/UCTm8zZK7j5WWjqhFSqasz4A'
    if env == 'master':
        url['url_home'] = f'{url_master}'
        url['url_impact'] = f'{url_master}impact'
        url['url_services'] = f'{url_master}services'
        url['url_resources'] = f'{url_master}resources'
        url['url_story_detail'] = f'{url_master}impact/{story_slug}'
        url['url_event_inperson_free_detail'] = f'{url_master}events/{event_inperson_free_slug}'
        url['url_api'] = f'{url_master_API}'
        url['url_api_index_page'] = f'{url_master_API}/index.json'
        url['url_api_impact_page'] = f'{url_master_API}/impact.json'
        url['url_api_events_page'] = f'{url_master_API}/events.json'
        url['url_api_services_page'] = f'{url_master_API}/services.json'
        url['url_api_resources_page'] = f'{url_master_API}/resources.json'
        url['url_api_story_detail_page'] = f'{url_master_API}/impact/{story_slug}.json?slug={story_slug}'
        url['url_api_service_detail_page'] = f'{url_master_API}/services/{service_slug}.json?slug={service_slug}'
        url['url_api_resource_detail_page'] = f'{url_master_API}/resources/{resource_slug}.json?slug={resource_slug}'
        url[
            'url_api_about_us_empty_type_page'] = f'{url_master_API}/about-us/{about_us_empty_type_slug}.json?slug={about_us_empty_type_slug}'
        url[
            'url_api_about_us_carousel_gallery_type_page'] = f'{url_master_API}/about-us/{about_us_carousel_gallery_type_slug}.json?slug={about_us_carousel_gallery_type_slug}'
        url[
            'url_api_about_us_hero_img_type_page'] = f'{url_master_API}/about-us/{about_us_hero_img_type_slug}.json?slug={about_us_hero_img_type_slug}'
        url[
            'url_api_inperson_free_event_detail_page'] = f'{url_master_API}/events/{event_inperson_free_slug}.json?slug={event_inperson_free_slug}'
        url[
            'url_api_inperson_pay_event_detail_page'] = f'{url_master_API}/events/{event_inperson_pay_slug}.json?slug={event_inperson_pay_slug}'
        url[
            'url_api_online_free_event_detail_page'] = f'{url_master_API}/events/{event_online_free_slug}.json?slug={event_online_free_slug}'
        url[
            'url_api_online_pay_event_detail_page'] = f'{url_master_API}/events/{event_online_pay_slug}.json?slug={event_online_pay_slug}'
        url['url_support_page'] = f'https://www.expocitydubai.com/en/plan-your-visit-1/support/'
        url['url_media_page'] = f'https://www.expocitydubai.com/en/media-centre/'
        url['url_legal_page'] = f'https://www.expocitydubai.com/en/legals/privacy-policy/'
        url['url_expo_city_dubai_page'] = f'https://www.expocitydubai.com/en/'
        url['url_virtual_expo_dubai_page'] = f'https://virtualexpodubai.com/'
        url['url_expo_2020_page'] = f'https://expo2020dubai.com/'
        url['url_tiktok_page'] = f'https://www.tiktok.com/@expocitydubai'
        url['url_instagram_page'] = f'https://www.instagram.com/expocitydubai/'
        url['url_facebook_page'] = f'https://www.facebook.com/Expo2020Dubai'
        url['url_twitter_page'] = f'https://twitter.com/expocitydubai'
        url['url_linkedin_page'] = f'https://www.linkedin.com/uas/login?session_redirect=%2Fcompany%2F26639576%2F'
        url['url_youtube_page'] = f'https://www.youtube.com/channel/UCTm8zZK7j5WWjqhFSqasz4A'
    return url
