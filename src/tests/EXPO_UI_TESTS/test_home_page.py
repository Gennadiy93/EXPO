import random
import time

from src.EXPO_UI.BasePage import BasePage


def test_home_title_is_not_empty(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    title = page.is_present('xpath', page.main_page_title_locator)
    actual_result = page.get_text_from_webelement(title)

    assert actual_result is not ''


def test_home_description_is_not_empty(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    desc = page.is_present('xpath', page.main_page_description_locator)
    actual_result = page.get_text_from_webelement(desc)

    assert actual_result is not ''


def test_home_featured_title_is_not_empty(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    title = page.is_present('xpath', page.main_page_featured_title_locator)
    actual_result = page.get_text_from_webelement(title).strip()

    assert actual_result == 'Featured'


def test_home_featured_slider_is_not_empty(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    buttons = page.are_present('xpath', page.main_page_featured_slider_buttons_locator)

    assert len(buttons) != 0


def test_home_click_any_button_featured_slider(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    buttons = page.are_present('xpath', page.main_page_featured_slider_buttons_locator)
    random.choice(buttons).click()
    time.sleep(0.5)

    assert driver.current_url != url['url_home']

#impact block


def test_button_view_all_stories(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    button = page.is_present('xpath', page.main_page_view_all_stories_locator)
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
    time.sleep(0.5)

    assert driver.current_url == page.url['url_impact']


def test_home_impact_slider_is_not_empty(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    cards = page.are_present('xpath', page.main_page_impact_slider_cards_locator)

    assert len(cards) != 0


def test_home_click_any_button_impact_slider(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    cards = page.are_present('xpath', page.main_page_impact_slider_cards_locator)
    driver.execute_script("arguments[0].scrollIntoView();", random.choice(cards))
    random.choice(cards).click()
    time.sleep(0.5)

    assert driver.current_url != url['url_home']

#resource block


def test_button_go_deeper(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    button = page.is_present('xpath', page.main_page_go_deeper_locator)
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
    time.sleep(0.5)

    assert driver.current_url == page.url['url_resources']


def test_home_resource_slider_is_not_empty(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    cards = page.are_present('xpath', page.main_page_resource_slider_cards_locator)

    assert len(cards) != 0


def test_home_click_any_button_resource_slider(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    cards = page.are_present('xpath', page.main_page_resource_slider_cards_locator)
    driver.execute_script("arguments[0].scrollIntoView();", random.choice(cards))
    random.choice(cards).click()
    time.sleep(0.5)

    assert driver.current_url != url['url_home']


# header block
def test_home_click_any_main_button_header(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    buttons = page.are_present('xpath', page.header_main_buttons_locator)
    random.choice(buttons).click()
    time.sleep(0.5)

    assert driver.current_url != url['url_home']


def test_home_click_any_about_us_button_header(setup):
    driver, wait, actions = setup
    page = BasePage(driver, wait, actions)
    url = page.url
    page.open_page(url['url_home'])

    about_us = page.is_present('xpath', page.header_about_us_locator)
    about_us.click()
    buttons = page.are_present('xpath', page.header_edg_page_buttons_locator)
    random.choice(buttons).click()
    time.sleep(0.5)

    assert driver.current_url != url['url_home']

