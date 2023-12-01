from ui.pages.hq_page import HqPage
from ui.locators import basic_locators


class AudiencePage(HqPage):
    url = 'https://ads.vk.com/hq/audience'
    locators = basic_locators.AudiencePageLocators

    def create_audience(self):
        self.click(self.locators.CREATE_AUDIENCE)
