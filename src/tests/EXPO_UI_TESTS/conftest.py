import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
    yield driver, wait
    driver.quit()


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('window-size=1300,1080')
    # options.add_argument("--headless")
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    return driver


@pytest.fixture
def get_chrome_options_docker():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    return options


@pytest.fixture()
def get_webdriver_docker(get_chrome_options_docker):
    options = get_chrome_options_docker
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
    return driver
