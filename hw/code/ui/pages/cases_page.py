from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class CasesPage(MainPage):
    url = 'https://ads.vk.com/cases'
    locators = basic_locators.CasesLocators

    def get_case_card(self):
        return self.find(self.locators.CASE_CARD)
