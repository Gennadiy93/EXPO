import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.wait import WebDriverWait

from src.data.configuration import chrome_windows_path
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('window-size=1300,1080')
    #options.add_argument("--headless")
    return options


@pytest.fixture()
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    s = Service(chrome_windows_path)
    driver = webdriver.Chrome(service=s, options=options)
    return driver


@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
    actions = ActionChains(driver)
    yield driver, wait, actions
    driver.quit()
