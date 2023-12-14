from typing import Literal
from selenium.webdriver.common.action_chains import ActionChains
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = basic_locators.MainPageLocators()

    def click_logo(self):
        self.click(self.locators.LOGO)
        return MainPage(self.driver)

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
        self.hover(self.locators.EDUCATION_TAB)

    def is_education_dropdown_visible(self):
        return self.is_visible(self.locators.EDUCATION_DROPDOWN)

    def is_side_menu_hamburger_visible(self):
        return self.is_visible(self.locators.HAMBURGER)

    def get_carousel_active_img(self):
        element = self.find(self.locators.ACTIVE_SLIDER).find_element(By.XPATH, "//img")
        return element.get_attribute('src')

    def click_nonactive_tab(self):
        button = self.find(self.locators.BULLETS_TAB).find_element(By.CLASS_NAME, "Bullets_box__xAFrY")
        button.click()

    