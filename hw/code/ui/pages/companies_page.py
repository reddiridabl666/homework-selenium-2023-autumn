from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.hq_page import HqPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CompaniesPage(HqPage):
    url = 'https://ads.vk.com/hq/dashboard/ads'
    locators = basic_locators.CompaniesLocators

    TARGET_SITE = 'event-radar.ru'

    def click_create_btn(self):
        self.find(self.locators.CREATE_BUTTON).click()

    def select_site_target(self):
        self.find(self.locators.SITE_TARGET).click()

    def input_site_value(self, url):
        input = self.find(self.locators.SITE_INPUT)
        input.click()
        input.send_keys(url)
        input.send_keys(Keys.RETURN)

    def input_money_value(self, money_value):
        input = self.find(self.locators.MONEY_INPUT)
        input.click()
        input.send_keys(money_value)
        input.send_keys(Keys.RETURN)

    def click_contitnue_btn(self):
        self.find(self.locators.CONTINUE_BUTTON).click()

    def create_company(self, url, money):
        self.click_create_btn()
        self.select_site_target()
        self.input_site_value(url)
        self.input_money_value(money)
        self.click_contitnue_btn()

    def select_mobileapp_target(self):
        self.find(self.locators.MOBILEAPP_TARGET).click()

    def has_target_input(self):
        try:
            elem = self.find(self.locators.TARGET_INPUT)
            return True
        except NoSuchElementException:
            return False

    def has_mobile_target_input(self):
        try:
            elem = self.find(self.locators.MOBILE_TARGET_INPUT)
            return True
        except NoSuchElementException:
            return False
        
    def go_to_root(self):
        self.find(self.locators.ROOT).click()
    
    def click_drafts_btn(self):
        self.find(self.locators.DRAFTS_BUTTON).click()

    def input_search_query(self, query):
        input = self.find(self.locators.SEARCH_FIELD)
        input.click()
        input.send_keys(query)
        