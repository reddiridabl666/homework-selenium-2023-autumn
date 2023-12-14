from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WebinarsPage(BasePage):
    url = 'https://ads.vk.com/events'
    locators = basic_locators

    def get_webinar_card(self):
        return self.find((By.CLASS_NAME, 'Event_wrapper__3_Si5'))
    
    def click_back_button(self):
        pass

    def click_register_button(self):
        self.find((By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div/article/div[2]/div/div/div[3]/a/span[1]')).click()