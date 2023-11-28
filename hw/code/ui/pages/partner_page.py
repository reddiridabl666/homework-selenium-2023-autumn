from ui.locators.basic_locators import PartnerPageLocators
from ui.pages.base_page import BasePage

class PartnerPage(BasePage):
    url = 'https://ads.vk.com/partner'
    locators = PartnerPageLocators()

    def click_account(self):
        self.click(self.locators.GO_TO_ACCOUNT)

    def click_help(self):
        self.click(self.locators.HELP)

    def click_site_tab(self):
        self.click(self.locators.SITE_TAB)

    def click_mobile_tab(self):
        self.click(self.locators.MOBILE_TAB)

    def check_format_presence(self, format_text):
        return self.is_visible(self.locators.DIV_BY_TEXT(format_text))
