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

    def is_pixel_modal_opened(self):
        return self.is_visible(self.locators.ADD_PIXEL_MODAL)

    def is_pixel_modal_closed(self):
        return self.is_not_visible(self.locators.ADD_PIXEL_MODAL)

    def fill_domain_input(self, text):
        self.fill_in(self.locators.DOMAIN_INPUT, text)

    def submit_btn_enabled(self):
        return self.find(self.locators.SUBMIT_BTN).is_enabled()

    def click_submit_btn(self):
        self.click(self.locators.DOMAIN_SUBMIT_BTN)

    def is_pixel_created_modal_visible(self):
        return self.is_visible(self.locators.PIXEL_ADDED_MODAL)
