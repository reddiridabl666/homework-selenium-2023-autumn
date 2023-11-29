import time
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


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


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration/new'
    locators = basic_locators.RegistrationPageLocators()

    def select_country(self, country_name):
        self.click(self.locators.COUNTRY)
        self.click(self.locators.VK_UI_SELECT_ELEM(country_name))

    def available_currencies_after_country_change(self, main_currency):
        self.wait().until(EC.text_to_be_present_in_element(
            self.locators.CURRENCY, main_currency))

        self.click(self.locators.CURRENCY)
        elems = self.find_multiple(self.locators.VK_UI_SELECT_ELEMS)
        return tuple(elem.get_attribute("title") for elem in elems)

    def fill_in_form(self, email, terms_accepted=True):
        self.fill_in(self.locators.EMAIL_INPUT, email)
        if not terms_accepted:
            self.click(self.locators.TERMS)
        self.click(self.locators.CREATE_ACCOUNT)

    def has_email_error(self, error='Обязательное поле'):
        self.has_error(self.locators.EMAIL_INPUT, error=error)

    def has_terms_error(self):
        self.has_error(self.locators.TERMS)

    def has_error(self, locator, error='Обязательное поле'):
        elem = self.find(self.locators.ERROR)
        self.find_from(elem, locator)
        self.find_from(elem, self.locators.BY_TEXT(error))

    def has_global_error(self):
        elem = self.find(self.locators.FORM_ERROR)
        self.find_from(elem, self.locators.BY_TEXT('Ошибка'))
        self.find_from(elem, self.locators.BY_TEXT('Validation failed'))
