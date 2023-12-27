import time
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import SitesPageLocators
from selenium.webdriver.support import expected_conditions as EC


class SitesPage(BasePage):
    url = "https://ads.vk.com/hq/pixels"
    locators = SitesPageLocators()

    def open_add_pixel_modal(self):
        self.click(self.locators.ADD_PIXEL_BTN)

    def close_add_pixel_modal(self):
        self.click(self.locators.CLOSE_MODAL_BTN)

    def get_pixel_modal(self, timeout=5):
        return self.get_element(self.locators.ADD_PIXEL_MODAL, timeout=timeout)

    def wait_for_pixel_modal_close(self):
        return self.wait_until_element_not_visible(self.locators.ADD_PIXEL_MODAL)

    def fill_domain_input(self, text):
        self.fill_in(self.locators.DOMAIN_INPUT, text)

    def get_submit_btn(self):
        return self.find(self.locators.DOMAIN_SUBMIT_BTN)

    def click_submit_btn(self):
        self.click(self.locators.DOMAIN_SUBMIT_BTN)
   
    def get_pixel_created_modal(self):
        return self.get_element(self.locators.PIXEL_ADDED_MODAL)
