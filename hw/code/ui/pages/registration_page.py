import time
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class RegistrationMainPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = basic_locators.RegistrationMainPageLocators()

    def go_to_account_creation(self, login, password):
        self.select_mail_account(login, password)
        self.click(self.locators.GO_TO_REGISTRATION)
        return RegistrationPage(self.driver)

    def select_mail_account(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH)
        self.fill_in(self.locators.MAIL_RU_LOGIN, login)
        self.click(self.locators.MAIL_RU_SHOW_PASSWORD)
        self.fill_in(self.locators.MAIL_RU_PASSWORD, password)
        self.click(self.locators.MAIL_RU_SUBMIT)

    def login_vk_id(self, login, password):
        self.fill_in(self.locators.LOGIN, login)
        self.click(self.locators.SUBMIT_BTN)
        self.fill_in(self.locators.PASSWORD, password)
        self.click(self.locators.SUBMIT_BTN)


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration/new'
    locators = basic_locators.RegistrationPageLocators()
