import time
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import EcommPageLocators
from selenium.webdriver.support import expected_conditions as EC


class CreateCatalogModal:
    def __init__(self, page):
        self.page = page
        self.locators = page.locators

    def click_feed_btn(self):
        self.page.click(self.locators.create_catalog_modal.FEED_BTN)

    def click_marketplace_btn(self):
        self.page.click(self.locators.create_catalog_modal.MARKETPLACE_BTN)

    def click_manual_btn(self):
        self.page.click(self.locators.create_catalog_modal.MANUAL_BTN)

    def check_feed(self):
        self.page.is_visible(self.locators.create_catalog_modal.FEED_LABEL)

    def check_marketplace(self):
        self.page.is_visible(self.locators.create_catalog_modal.MARKETPLACE_LABEL)

    def check_manual(self):
        self.page.is_visible(self.locators.create_catalog_modal.MANUAL_LABEL)

    def create_catalog_from_file(self):
        file_path = 'files/catalog_products.csv'
        self.page.upload_file(self.locators.create_catalog_modal.MANUAL_FILE_SELECTOR, file_path)

        self.page.click(self.locators.create_catalog_modal.SUBMIT_CATALOG_BTN)

    def check_loading_started(self):
        self.page.wait(30).until(EC.visibility_of_element_located(self.locators.FEED_LOADING))
        return True

    def check_loading_finished(self):
        self.page.wait(600).until(EC.invisibility_of_element_located(self.locators.FEED_LOADING))
        return True


class EcommPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = EcommPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.create_catalog_modal = CreateCatalogModal(self)

    def click_create_catalog_btn(self):
        self.click(self.locators.CREATE_CATALOG_BTN)

    def check_catalog_btn_visible(self):
        self.is_visible(self.locators.CREATE_CATALOG_MODAL)

    def click_catalog(self):
        self.click(self.locators.CATALOG)
