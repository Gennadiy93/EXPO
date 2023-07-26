from selenium.webdriver.support import expected_conditions as EC
from typing import List

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.data.configuration import generate_link
from src.tests.conftest import setup


class BasePage:
    def __init__(self, driver, wait, actions):
        # Locators
        self.main_page_title_locator = "//*[starts-with(@class,'PageTitle')]"
        self.main_page_description_locator = "//*[starts-with(@class,'PageTitle')]/..//p"
        self.main_page_featured_title_locator = "//*[text()='Featured']"
        self.main_page_featured_slider_buttons_locator = "//*[@class='slick-track']//button"
        self.main_page_view_all_stories_locator = "//*[@href='/impact']//button"
        self.main_page_impact_slider_cards_locator = "//*[@href='/impact']//button/../../../../following-sibling::*//a"
        self.main_page_go_deeper_locator = "//*[@href='/resources']//button"
        self.main_page_resource_slider_cards_locator = "//*[@href='/resources']//button/../../../../following-sibling::*//a"
        self.header_main_buttons_locator = "//header//*[text()='Impact']/../../a"
        self.header_about_us_locator = "//header//*[text()='Impact']/../../div"
        self.header_edg_page_buttons_locator = "//header//*[text()='Impact']/../../div//a"
        self.header_impact_button_locator = "//header//*[text()='Impact']/.."

        self.driver = driver
        self.wait = wait
        self.actions = actions

        self.url = generate_link()

    @staticmethod
    def get_text_from_webelement(element: WebElement) -> str:
        return str(element.text).strip()

    def open_page(self, url):
        driver = self.driver
        return driver.get(url)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'xpath': By.XPATH}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(EC.invisibility_of_element((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)
