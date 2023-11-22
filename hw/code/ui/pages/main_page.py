from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = basic_locators.MainPageLocators()

    def click_logo(self):
        self.click(self.locators.LOGO)
        return MainPage(self.driver)

    def click_account(self):
        self.click(self.locators.GO_TO_ACCOUNT)

    def click_help(self):
        self.click(self.locators.HELP)

    def click_tab(self, tab_name):
        self.click(self.locators.TAB(tab_name))

    def open_education_dropdown(self):
        education_tab = self.find(self.locators.EDUCATION_TAB)
        hover = ActionChains(self.driver).move_to_element(education_tab)
        hover.perform()

    def is_education_dropdown_visible(self):
        return self.is_visible(self.locators.EDUCATION_DROPDOWN)

    def is_side_menu_hamburger_visible(self):
        return self.is_visible(self.locators.HAMBURGER)
