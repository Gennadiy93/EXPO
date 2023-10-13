from selenium.webdriver.support import expected_conditions as EC
from typing import List

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        # Locators

    @staticmethod
    def get_text_from_webelement(element: WebElement) -> str:
        return str(element.text).strip()

    def open_page(self, url):
        driver = self.driver
        return driver.get(url)

    def is_visible(self, locator: str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def is_present(self, locator: str) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    def is_not_visible(self, locator: str) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def are_visible(self, locator: str) -> List[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, locator)))

    def are_present(self, locator: str) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))

    def get_text_from_webelements(self, elements: List[WebElement]) -> List:
        return [str(element.text).replace('\n', ' ').replace('#', ' ').strip() for element in elements]
