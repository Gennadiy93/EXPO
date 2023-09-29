import random
import time
from src.EXPO_UI.BasePage import BasePage
import pytest
from faker import Faker


@pytest.mark.asyncio
async def test_home_title_is_not_empty(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        title = page.is_visible('xpath', page.main_page_title_locator)
        actual_result = page.get_text_from_webelement(title)

        assert actual_result is not ''


@pytest.mark.asyncio
async def test_home_description_is_not_empty(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        desc = page.is_visible('xpath', page.main_page_description_locator)
        actual_result = page.get_text_from_webelement(desc)

        assert actual_result is not ''


@pytest.mark.asyncio
async def test_home_featured_title_is_not_empty(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        title = page.is_visible('xpath', page.main_page_featured_title_locator)
        actual_result = page.get_text_from_webelement(title).strip()

        assert actual_result == 'Featured'


@pytest.mark.asyncio
async def test_home_featured_slider_is_not_empty(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        buttons = page.are_present('xpath', page.main_page_featured_slider_buttons_locator)

        assert len(buttons) != 0


@pytest.mark.asyncio
async def test_home_click_any_button_featured_slider(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        buttons = page.are_visible('xpath', page.main_page_featured_slider_buttons_locator)
        time.sleep(1)
        random.choice(buttons).click()
        time.sleep(1)

        assert driver.current_url != url['url_home'] and page.is_not_present('xpath', page.error_locator)


# impact block

@pytest.mark.asyncio
async def test_button_view_all_stories(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        time.sleep(1)
        button = page.is_visible('xpath', page.main_page_view_all_stories_locator)
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(1)
        button.click()
        time.sleep(1)

        assert driver.current_url == page.url['url_impact'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_impact_slider_is_not_empty(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        cards = page.are_visible('xpath', page.main_page_impact_slider_cards_locator)

        assert len(cards) != 0


@pytest.mark.asyncio
async def test_home_click_any_button_impact_slider(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        time.sleep(0.5)
        cards = page.are_visible('xpath', page.main_page_impact_slider_cards_locator)
        button = page.is_visible('xpath', page.main_page_view_all_stories_locator)
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(1)
        random.choice(cards).click()
        time.sleep(0.5)

        assert driver.current_url != url['url_home'] and page.is_not_present('xpath', page.error_locator)


# resource block

@pytest.mark.asyncio
async def test_button_go_deeper(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        button = page.is_visible('xpath', page.main_page_go_deeper_locator)
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(1)
        button.click()
        time.sleep(0.5)

        assert driver.current_url == page.url['url_resources'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_button_work_with_us(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        button = page.is_visible('xpath', page.main_page_work_with_us_locator)
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(1)
        button.click()
        time.sleep(0.5)

        assert driver.current_url == page.url['url_services'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_resource_slider_is_not_empty(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        cards = page.are_present('xpath', page.main_page_resource_slider_cards_locator)

        assert len(cards) != 0


@pytest.mark.asyncio
async def test_home_pillars_slider_is_not_empty(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        cards = page.are_present('xpath', page.main_page_pillars_slider_cards_locator)

        assert len(cards) != 0


@pytest.mark.asyncio
async def test_home_click_any_button_resource_slider(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        time.sleep(1)
        resource_slider = page.is_visible('xpath', "(//main//*[@class='slick-list'])[last()]")
        driver.execute_script("arguments[0].scrollIntoView();", resource_slider)
        cards = page.are_visible('xpath', page.main_page_resource_slider_cards_locator)
        time.sleep(1)
        random.choice(cards).click()
        time.sleep(1)

        assert driver.current_url != url['url_home'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_any_button_pillars_slider(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        cards = page.are_visible('xpath', page.main_page_pillars_slider_cards_locator)
        driver.execute_script("arguments[0].scrollIntoView();", random.choice(cards))
        time.sleep(1)
        random.choice(cards).click()
        time.sleep(1)

        assert driver.current_url != url['url_home'] and page.is_not_present('xpath', page.error_locator)


# header block
@pytest.mark.asyncio
@pytest.mark.parametrize('header_buttons',
                         ["//header//*[@href='/impact']", "//header//*[@href='/services']",
                          "//header//*[@href='/resources']"])
async def test_home_click_any_main_button_header(setup, header_buttons):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        time.sleep(1)
        button = page.is_visible('xpath', header_buttons)
        button.click()
        time.sleep(1)

        assert driver.current_url != url['url_home']


@pytest.mark.asyncio
async def test_home_click_events_main_button_header(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        dropdown_events = page.is_visible('xpath', page.header_events_dropdown_button)
        dropdown_events.click()
        button_events = page.is_visible('xpath', page.header_events_button_locator)
        button_events.click()
        time.sleep(0.5)

        assert driver.current_url != url['url_home']


@pytest.mark.asyncio
async def test_home_click_any_about_us_button_header(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])
        time.sleep(0.5)
        dropdown_about_us = page.is_visible('xpath', page.header_about_us_dropdown_locator)
        dropdown_about_us.click()
        edg_pages = page.are_visible('xpath', page.header_edg_pages_buttons_locator)
        random.choice(edg_pages).click()
        time.sleep(1)

        assert driver.current_url != url['url_home'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_support_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        support_button = page.is_visible('xpath', page.footer_support_button)
        driver.execute_script("arguments[0].scrollIntoView();", support_button)
        support_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_support_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_media_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        media_button = page.is_visible('xpath', page.footer_media_button)
        driver.execute_script("arguments[0].scrollIntoView();", media_button)
        media_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_media_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_legal_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        legal_button = page.is_visible('xpath', page.footer_legal_button)
        driver.execute_script("arguments[0].scrollIntoView();", legal_button)
        legal_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_legal_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_expo_city_dubai_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        expo_city_dubai_button = page.is_visible('xpath', page.footer_expo_city_dubai_button)
        driver.execute_script("arguments[0].scrollIntoView();", expo_city_dubai_button)
        expo_city_dubai_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_expo_city_dubai_page'] and page.is_not_present('xpath',
                                                                                             page.error_locator)


@pytest.mark.asyncio
async def test_home_click_virtual_expo_dubai_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        virtual_expo_dubai_button = page.is_visible('xpath', page.footer_virtual_expo_dubai_button)
        driver.execute_script("arguments[0].scrollIntoView();", virtual_expo_dubai_button)
        virtual_expo_dubai_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_virtual_expo_dubai_page'] and page.is_not_present('xpath',
                                                                                                page.error_locator)


@pytest.mark.asyncio
async def test_home_click_expo_2020_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        expo_2020_button = page.is_visible('xpath', page.footer_expo_2020_button)
        driver.execute_script("arguments[0].scrollIntoView();", expo_2020_button)
        expo_2020_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_expo_2020_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_tiktok_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        tiktok_button = page.is_visible('xpath', page.footer_tiktok_button)
        driver.execute_script("arguments[0].scrollIntoView();", tiktok_button)
        tiktok_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_tiktok_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_instagram_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        instagram_button = page.is_visible('xpath', page.footer_instagram_button)
        driver.execute_script("arguments[0].scrollIntoView();", instagram_button)
        instagram_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_instagram_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_facebook_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        facebook_button = page.is_visible('xpath', page.footer_facebook_button)
        driver.execute_script("arguments[0].scrollIntoView();", facebook_button)
        facebook_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_facebook_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_twitter_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        twitter_button = page.is_visible('xpath', page.footer_twitter_button)
        driver.execute_script("arguments[0].scrollIntoView();", twitter_button)
        twitter_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_twitter_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_linkedin_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        linkedin_button = page.is_visible('xpath', page.footer_linkedin_button)
        driver.execute_script("arguments[0].scrollIntoView();", linkedin_button)
        linkedin_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_linkedin_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_linkedin_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        linkedin_button = page.is_visible('xpath', page.footer_linkedin_button)
        driver.execute_script("arguments[0].scrollIntoView();", linkedin_button)
        linkedin_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_linkedin_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_click_youtube_button_footer(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        youtube_button = page.is_visible('xpath', page.footer_youtube_button)
        driver.execute_script("arguments[0].scrollIntoView();", youtube_button)
        youtube_button.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.5)

        assert driver.current_url == url['url_youtube_page'] and page.is_not_present('xpath', page.error_locator)


@pytest.mark.asyncio
async def test_home_contact_us_registration(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        fake = Faker()
        fake_name = fake.name()
        fake_email = fake.email()
        fake_text = fake.text()

        fullname = page.is_visible('xpath', page.contact_us_fullname_locator)
        fullname.send_keys(fake_name)

        email = page.is_visible('xpath', page.contact_us_email_locator)
        email.send_keys(fake_email)

        profession_dropdown = page.is_visible('xpath', page.contact_us_your_profession_dropdown)
        profession_dropdown.click()
        your_profession_button = page.are_visible('xpath', page.contact_us_list_your_profession)
        random.choice(your_profession_button).click()

        message = page.is_visible('xpath', page.contact_us_message_field)
        message.send_keys(fake_text)

        checkbox = page.is_visible('xpath', page.contact_us_agree_checkbox)
        checkbox.click()

        submit_button = page.is_visible('xpath', page.contact_us_submit_button)
        submit_button.click()

        assert page.is_visible('xpath', page.contact_us_success_message)


@pytest.mark.asyncio
async def test_home_news_letter_registration(setup):
    async for driver, wait, actions in setup:
        page = BasePage(driver, wait, actions)
        url = page.url
        page.open_page(url['url_home'])

        fake = Faker()
        fake_name = fake.name()
        fake_email = fake.email()

        fullname = page.is_visible('xpath', page.news_letter_fullname_locator)
        fullname.send_keys(fake_name)

        email = page.is_visible('xpath', page.news_letter_email_locator)
        email.send_keys(fake_email)

        submit_button = page.is_visible('xpath', page.news_letter_submit_button)
        submit_button.click()

        assert page.is_visible('xpath', page.news_letter_success_message)
