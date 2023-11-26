from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class RegistrationMainPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = basic_locators.RegistrationMainPageLocators()

    def click_registration(self):
        self.click(self.locators.GO_TO_REGISTRATION)
        return RegistrationPage(self.driver)


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration/new'
    locators = basic_locators.RegistrationPageLocators()
