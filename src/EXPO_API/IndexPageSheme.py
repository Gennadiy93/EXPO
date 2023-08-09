from pydantic import BaseModel, ValidationError, field_validator, Field


class ContentInFirstContentInDescription(BaseModel):
    data: dict
    marks: list
    value: str
    nodeType: str

    @field_validator('value')
    def check_home_desc_value_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('value is empty')
        else:
            return v


class FirstContentInDescription(BaseModel):
    data: dict
    content: list[ContentInFirstContentInDescription]
    nodeType: str


class Description(BaseModel):
    data: dict
    content: list[FirstContentInDescription]
    nodeType: str


class Service(BaseModel):
    pillar_title: str = Field(alias='pillarTitle')
    pillar_image: dict = Field(alias='pillarImage')
    pillar_description: dict = Field(alias='pillarDescription')

    @field_validator('pillar_title')
    def check_home_pillar_title_in_list_services_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('pillar_title is empty')
        else:
            return v

    @field_validator('pillar_image')
    def check_home_pillar_image_in_list_services_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('pillar_image is empty')
        else:
            return v


class Resource(BaseModel):
    title: str
    slug: str
    resource_description: dict = Field(alias='resourceDescription')
    resource_thumbnail: dict = Field(alias='resourceThumbnail')
    categories_collection: dict = Field(alias='categoriesCollection')

    @field_validator('title')
    def check_home_resource_title_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('title is empty')
        else:
            return v

    @field_validator('slug')
    def check_home_resource_slug_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('slug is empty')
        else:
            return v

    @field_validator('resource_thumbnail')
    def check_home_resource_thumbnail_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('resource_thumbnail is empty')
        else:
            return v

    @field_validator('categories_collection')
    def check_home_category_collection_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('categories_collection is empty')
        else:
            return v


class Story(BaseModel):
    page_title: str = Field(alias='pageTitle')
    slug: str
    hero_landscape_image: dict = Field(alias='heroLandscapeImage')
    hero_square_image: dict = Field(alias='heroSquareImage')
    banner_image: dict = Field(alias='bannerImage')
    categories_collection: dict = Field(alias='categoriesCollection')

    @field_validator('page_title')
    def check_home_story_title_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('page_title is empty')
        else:
            return v

    @field_validator('slug')
    def check_home_resource_slug_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('slug is empty')
        else:
            return v

    @field_validator('hero_landscape_image')
    def check_home_hero_landscape_image_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('hero_landscape_image is empty')
        else:
            return v

    @field_validator('hero_square_image')
    def check_home_hero_square_image_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('hero_square_image is empty')
        else:
            return v

    @field_validator('banner_image')
    def check_home_banner__image_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('banner_image is empty')
        else:
            return v

    @field_validator('categories_collection')
    def check_home_category_collection_in_list_resources_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('categories_collection is empty')
        else:
            return v


class Index_Page(BaseModel):
    home_title: str = Field(alias='homeTitle')
    home_desc: dict = Field(alias='homeDesc')
    services_title: str = Field(alias='servicesTitle')
    services_desc: Description = Field(alias='servicesDesc')
    resources_title: str = Field(alias='resourcesTitle')
    resources_desc: Description = Field(alias='resourcesDesc')
    services: list[Service]
    resources: list[Resource]
    contact_us_form_title: str = Field(alias='contactUsFormTitle')
    contact_us_form_description: dict = Field(alias='contactUsFormDescription')
    home_slider_collection: list = Field(alias='homeSliderCollection')
    story_title: str = Field(alias='storyTitle')
    story_desc: Description = Field(alias='storyDesc')
    story_slider: list[Story] = Field(alias='storyslider')
    autorotate_future_slider: bool = Field(alias='autorotateFutureSlider')
    autorotate_impact: bool = Field(alias='autorotateImpact')
    autorotate_service_pillars: bool = Field(alias='autorotateServicePillars')
    autorotate_popular_resources: bool = Field(alias='autorotatePopularResources')
    hero_image: dict = Field(alias='heroImage')
    marketing_banner: str = Field(alias='marketingBanner')

    @field_validator('home_title')
    def check_home_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('home_title is empty')
        else:
            return v

    @field_validator('services_title')
    def check_home_services_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('services_title is empty')
        else:
            return v

    @field_validator('resources_title')
    def check_home_resource_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('resources_title is empty')
        else:
            return v

    @field_validator('services')
    def check_home_list_services_is_not_empty(cls, v):
        if v is None or v == '' or len(v) == 0:
            raise ValueError('services is empty')
        else:
            return v

    @field_validator('resources')
    def check_home_list_resources_is_not_empty(cls, v):
        if v is None or v == '' or len(v) == 0:
            raise ValueError('resources is empty')
        else:
            return v

    @field_validator('contact_us_form_title')
    def check_home_contact_us_form_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('contact_us_form_title is empty')
        else:
            return v

    @field_validator('story_title')
    def check_home_story_title_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('story_title is empty')
        else:
            return v

    @field_validator('story_slider')
    def check_home_story_slider_collection_is_not_empty(cls, v):
        if v is None or v == '' or len(v) == 0:
            raise ValueError('story_slider is empty')
        else:
            return v

    @field_validator('home_slider_collection')
    def check_home_slider_collection_is_not_empty(cls, v):
        if v is None or v == '' or len(v) == 0:
            raise ValueError('home_slider_collection collection is empty')
        else:
            return v

    @field_validator('hero_image')
    def check_home_hero_img_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('hero_image is empty')
        else:
            return v

    @field_validator('marketing_banner')
    def check_home_marketing_banner_is_not_empty(cls, v):
        if v is None or v == '':
            raise ValueError('marketing_banner is empty')
        else:
            return v
