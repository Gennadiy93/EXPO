from selenium.webdriver.support import expected_conditions as EC
from typing import List

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.data.configuration import generate_link



class BasePage:
    def __init__(self, driver, wait, actions):
        # Locators
        self.main_page_title_locator = "//*[starts-with(@class,'PageTitle')]"
        self.main_page_description_locator = "//*[starts-with(@class,'PageTitle')]/..//p"
        self.main_page_featured_title_locator = "//*[text()='Featured']"
        self.main_page_featured_slider_buttons_locator = "//*[@class='slick-track']//button"
        self.main_page_featured_slider_card_title_text_locator = "//*[@class='slick-track']//button/../../../..//h1"
        self.main_page_view_all_stories_locator = "//main//a[@href='/impact']"
        self.main_page_go_deeper_locator = "//*[@href='/resources']//button"
        self.main_page_work_with_us_locator = "//*[@href='/services']//button"
        self.main_page_impact_slider_cards_locator = "//main//*[@href='/impact']/../../..//*[@data-index>=0]"
        self.main_page_resource_slider_cards_locator = "//main//*[@href='/resources']/../../..//*[@data-index<7][@data-index>=0]//a"
        self.main_page_pillars_slider_cards_locator = "//main//*[@href='/services']/../../..//*[@data-index>=0]//a[starts-with(@href,'/services?')]"

        self.header_main_buttons_locator = "//header//*[text()='Impact']/../../a"
        self.header_about_us_dropdown_locator = "//*[@data-dropdown-toggle='dropdownEdg']"
        self.header_edg_pages_buttons_locator = "//*[@data-dropdown-toggle='dropdownEdg']//a"
        self.header_impact_button_locator = "//*[@href='/impact']"
        self.header_events_dropdown_button = "//*[@data-dropdown-toggle='dropdownEvents']"
        self.header_events_button_locator = "//*[@href='/events']"
        self.header_services_button_locator = "//*[@href='/services'][1]"
        self.header_resources_button_locator = "//*[@href='/resources'][1]"

        self.footer_support_button = "//a[text()='Support']"
        self.footer_media_button = "//a[text()='Media']"
        self.footer_legal_button = "//a[text()='Legal']"
        self.footer_expo_city_dubai_button = "//a[text()='Expo City Dubai']"
        self.footer_virtual_expo_dubai_button = "//a[text()='Virtual Expo Dubai']"
        self.footer_expo_2020_button = "//a[text()='Expo 2020']"
        self.footer_tiktok_button = "//*[starts-with(@class,'footer_socialLinks')]//a[@class='tiktok']"
        self.footer_instagram_button = "//*[starts-with(@class,'footer_socialLinks')]//a[@class='instagram']"
        self.footer_facebook_button = "//*[starts-with(@class,'footer_socialLinks')]//a[@class='facebook']"
        self.footer_twitter_button = "//*[starts-with(@class,'footer_socialLinks')]//a[@class='twitter']"
        self.footer_linkedin_button = "//*[starts-with(@class,'footer_socialLinks')]//a[@class='linkedin']"
        self.footer_youtube_button = "//*[starts-with(@class,'footer_socialLinks')]//a[@class='youtube']"

        self.contact_us_fullname_locator = "//*[text()='Personal details']/..//input[@name='name']"
        self.contact_us_email_locator = "//*[text()='Personal details']/..//input[@name='email']"
        self.contact_us_your_profession_dropdown = "//*[text()='Personal details']/..//select"
        self.contact_us_list_your_profession = "//*[text()='Personal details']/..//select//option[text()!='Your Profession']"
        self.contact_us_message_field = "//*[text()='Personal details']/..//*[@name='message']"
        self.contact_us_agree_checkbox = "//*[text()='Personal details']/..//input[@class='checkbox']"
        self.contact_us_submit_button = "//*[text()='Personal details']/..//button"
        self.contact_us_success_message = "//*[text()='Thank you contacting us. Our team will be in touch with you soon.']"

        self.news_letter_fullname_locator = "//*[text()='Connect with us']/..//input[@name='name']"
        self.news_letter_email_locator = "//*[text()='Connect with us']/..//input[@name='email']"
        self.news_letter_submit_button = "//*[text()='Connect with us']/..//button"
        self.news_letter_success_message = "//*[text()='We look forward to keeping you up to date with the latest at Expo Dubai Group and more.']"

        self.error_locator = "//h1[@class='next-error-h1']"

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
        return self.wait.until(EC.visibility_of_any_elements_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List:
        return [str(element.text).replace('\n', ' ').replace('#', ' ').strip() for element in elements]
