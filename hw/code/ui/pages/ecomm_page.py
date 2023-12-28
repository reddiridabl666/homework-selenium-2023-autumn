from ui.pages.base_page import BasePage
from ui.locators.basic_locators import EcommPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CreateCatalogModal:
    CATALOG_PATH = 'files/catalog_products.csv'

    def __init__(self, page):
        self.page = page
        self.locators = page.locators

    def click_feed_btn(self):
        self.page.click(self.locators.create_catalog_modal.FEED_BTN)

    def click_marketplace_btn(self):
        self.page.click(self.locators.create_catalog_modal.MARKETPLACE_BTN)

    def click_manual_btn(self):
        self.page.click(self.locators.create_catalog_modal.MANUAL_BTN)

    def get_feed(self):
        return self.page.get_element(self.locators.create_catalog_modal.FEED_LABEL)

    def get_marketplace(self):
        return self.page.get_element(self.locators.create_catalog_modal.MARKETPLACE_LABEL)

    def get_manual(self):
        return self.page.get_element(self.locators.create_catalog_modal.MANUAL_LABEL)

    def create_catalog_from_file(self):
        self.page.upload_file(
            self.locators.create_catalog_modal.MANUAL_FILE_SELECTOR, self.CATALOG_PATH)

        self.page.click(self.locators.create_catalog_modal.SUBMIT_CATALOG_BTN)

    def get_loading_animation(self):
        return self.page.get_element(self.page.locators.FEED_LOADING, timeout=30)

    def wait_for_loading_end(self):
        return self.page.wait_until_element_not_visible(self.page.locators.FEED_LOADING, timeout=600)


class EcommPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = EcommPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.create_catalog_modal = CreateCatalogModal(self)

    def click_create_catalog_btn(self):
        self.click(self.locators.CREATE_CATALOG_BTN)

    def get_catalog_btn(self):
        return self.get_element(self.locators.CREATE_CATALOG_BTN)

    def click_catalog(self):
        self.click(self.locators.CATALOG)

    def open_catalog_options(self):
        self.click(self.locators.SETTINGS_BTN)

    def get_catalog_options_modal(self):
        return self.get_element(self.locators.SETTINGS_MODAL)

    def click_tab(self, tab_name):
        self.click(self.locators.SPAN_BY_TEXT(tab_name))

    def click_add_goods_btn(self):
        self.click(self.locators.ADD_GOODS_BTN)

    def click_promote_btn(self):
        self.click(self.locators.PROMOTE_BTN)
