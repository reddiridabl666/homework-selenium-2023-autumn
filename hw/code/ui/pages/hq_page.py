import time
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import HqPageLocators


class HqPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = HqPageLocators

    def delete_account(self):
        try:
            self.click(self.locators.CLOSE_HELP)
        except:
            pass
        self.click(self.locators.SETTINGS)
        self.click(self.locators.DELETE_ACCOUNT)
        self.click(self.locators.CONFIRM_DELETION)
        self.wait_for_redirect()
