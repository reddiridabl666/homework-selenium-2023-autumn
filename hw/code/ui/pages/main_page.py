from typing import Literal
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = basic_locators.MainPageLocators()

    ACTIVE_BULLET_CLASS = "Active"

    def click_logo(self):
        self.click(self.locators.LOGO)

    def click_footer_business(self):
        self.scroll_click(self.locators.FOOTER_GO_TO_BUSINESS)

    def click_footer_about(self):
        self.scroll_click(self.locators.FOOTER_ABOUT)

    def click_account(self):
        self.click(self.locators.GO_TO_ACCOUNT)

    def click_footer_account(self):
        self.scroll_click(self.locators.FOOTER_GO_TO_ACCOUNT)

    def click_help(self):
        self.click(self.locators.HELP)

    def click_tab(self, tab_name):
        self.click(self.locators.TAB(tab_name))

    def click_dropdown_tab(self, tab_name):
        self.click(self.locators.DROPDOWN_TAB(tab_name))

    def click_footer_tab(self, tab_name: str):
        self.scroll_click(self.locators.FOOTER_TAB(tab_name))

    def click_footer_group(self, url: str):
        self.scroll_click(self.locators.FOOTER_GROUP(url))

    def click_footer_language(self):
        self.scroll_click(self.locators.FOOTER_LANGUAGE)

    def click_footer_language_elem(self, language: Literal["English", "Русский"]):
        self.click(self.locators.FOOTER_LANGUAGE_SELECT_ELEMENT(language))

    def select_language(self, language: Literal["English", "Русский"]):
        self.click_footer_language()
        self.click_footer_language_elem(language)

    def get_footer_language(self) -> str:
        return self.find(self.locators.FOOTER_LANGUAGE_CONTENT).text

    def open_education_dropdown(self):
        self.hover(self.locators.EDUCATION_TAB,
                   cond=EC.visibility_of_element_located)

    def education_dropdown(self):
        try:
            dropdown = self.find(self.locators.EDUCATION_DROPDOWN)
            return dropdown
        except TimeoutException:
            return None

    def side_menu_hamburger(self):
        try:
            hamburger = self.find(self.locators.HAMBURGER)
            return hamburger
        except TimeoutException:
            return None

    def get_carousel_active_img(self):
        element = self.find(self.locators.ACTIVE_SLIDER_IMAGE)
        return element.get_attribute('src')
    
    def get_bullets(self):
        return self.find_multiple(self.locators.BULLETS)
    
    def get_bullet(self, bullet_id):
        return self.get_bullets()[bullet_id]
    
    def wait_until_bullet_becomes_inactive(self, bullet_id, timeout=10):
        ec = lambda _: self.ACTIVE_BULLET_CLASS not in self.get_bullet(bullet_id).get_attribute("class")
        return self.wait(timeout).until(ec)

    def click_nonactive_tab(self):
        button = self.find(self.locators.NON_ACTIVE_BULLET)
        button.click()
