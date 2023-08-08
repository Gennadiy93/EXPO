from src.EXPO_API.API import API
from pydantic import BaseModel, ValidationError, field_validator, Field
from typing import List


class ContentInFirstContentInDescription(BaseModel):
    data: dict
    marks: List
    value: str
    nodeType: str

    @field_validator('value')
    def check_home_desc_value_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('value is empty')


class FirstContentInDescription(BaseModel):
    data: dict
    content: List[ContentInFirstContentInDescription]
    nodeType: str


class Description(BaseModel):
    data: dict
    content: List[FirstContentInDescription]
    nodeType: str


class Service(BaseModel):
    pillarTitle: str
    pillarImage: dict
    pillarDescription: dict

    @field_validator('pillarTitle')
    def check_home_pillar_title_in_list_services_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('pillarTitle is empty')

    @field_validator('pillarImage')
    def check_home_pillar_image_in_list_services_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('pillarImage is empty')


class Resource(BaseModel):
    title: str
    slug: str
    resourceDescription: dict
    resourceThumbnail: dict
    categoriesCollection: dict

    @field_validator('title')
    def check_home_resource_title_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('title is empty')

    @field_validator('slug')
    def check_home_resource_slug_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('slug is empty')

    @field_validator('resourceThumbnail')
    def check_home_resource_thumbnail_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('resourceThumbnail is empty')

    @field_validator('categoriesCollection')
    def check_home_category_collection_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('categoriesCollection is empty')


class Story(BaseModel):
    pageTitle: str
    slug: str
    heroLandscapeImage: dict
    heroSquareImage: dict
    bannerImage: dict
    categoriesCollection: dict

    @field_validator('pageTitle')
    def check_home_story_title_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('pageTitle is empty')

    @field_validator('slug')
    def check_home_resource_slug_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('slug is empty')

    @field_validator('heroLandscapeImage')
    def check_home_hero_landscape_image_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('resourceThumbnail is empty')

    @field_validator('heroSquareImage')
    def check_home_hero_square_image_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('heroSquareImage is empty')

    @field_validator('bannerImage')
    def check_home_banner__image_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('bannerImage is empty')

    @field_validator('categoriesCollection')
    def check_home_category_collection_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('categoriesCollection is empty')


class Index_Page(BaseModel):
    homeTitle: str
    homeDesc: Description
    servicesTitle: str
    servicesDesc: dict
    resourcesTitle: str
    resourcesDesc: Description
    services: List[Service]
    resources: List[Resource]
    contactUsFormTitle: str
    contactUsFormDescription: dict
    homeSliderCollection: List
    storyTitle: str
    storyDesc: Description
    storyslider: List[Story]
    autorotateFutureSlider: bool
    autorotateImpact: bool
    autorotateServicePillars: bool
    autorotatePopularResources: bool
    heroImage: dict
    marketingBanner: str

    @field_validator('homeTitle')
    def check_home_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('Hometitle is empty')

    @field_validator('homeDesc')
    def check_home_desc_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('homeDesc is empty')

    @field_validator('servicesTitle')
    def check_home_services_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('servicesTitle is empty')

    @field_validator('servicesDesc')
    def check_home_services_desc_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('servicesDesc is empty')

    @field_validator('resourcesTitle')
    def check_home_resource_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('resourcesTitle is empty')

    @field_validator('resourcesDesc')
    def check_home_resource_desc_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('resourcesDesc is empty')

    @field_validator('services')
    def check_home_list_services_is_not_empty(cls, v):
        if v is None or v == '' or len(v) == 0:
            raise ValueError('services is empty')

    @field_validator('resources')
    def check_home_list_resources_is_not_empty(cls, v):
        if v is None or v == '' or len(v) == 0:
            raise ValueError('resources is empty')

    @field_validator('contactUsFormTitle')
    def check_home_contact_us_form_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('contactUsFormTitle is empty')

    @field_validator('contactUsFormDescription')
    def check_home_contact_us_form_desc_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('contactUsFormDescription is empty')

    @field_validator('storyTitle')
    def check_home_story_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('storyTitle is empty')

    @field_validator('storyDesc')
    def check_home_story_desc_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('storyDesc is empty')

    @field_validator('storyslider')
    def check_home_story_slider_collection_is_not_empty(cls, v):
        if v is None or v == '' or len(v) == 0:
            raise ValueError('storyslider is empty')

    @field_validator('homeSliderCollection')
    def check_home_slider_collection_is_not_empty(cls, v):
        if v is None or v == '' or len(v) == 0:
            raise ValueError('homeSliderCollection collection is empty')

    @field_validator('heroImage')
    def check_home_hero_img_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('heroImage is empty')

    @field_validator('marketingBanner')
    def check_home_marketing_banner_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('marketingBanner is empty')


def test_status_code_index_page():
    api = API()
    response_api = api.get_index_page()
    status_code_api = response_api['status']
    assert status_code_api == 200


def test_validate_index_page():
    api = API()
    response_api = api.get_index_page()
    response_api_json = response_api['json']

    Index_Page.model_validate(response_api_json['pageProps'])
