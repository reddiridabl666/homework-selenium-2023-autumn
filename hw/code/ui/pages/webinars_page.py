from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WebinarsPage(BasePage):
    url = 'https://ads.vk.com/events'
    locators = basic_locators.WebinarLocators

    def get_webinar_card(self):
        return self.find(self.locators.WEBINAR_CARD)
    
    def click_back_button(self):
        pass

    def click_register_button(self):
        self.find(self.locators.REGISTER_BUTTON).click()
