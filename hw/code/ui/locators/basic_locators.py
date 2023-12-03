from typing import Literal
from selenium.webdriver.common.by import By


class BasePageLocators:
    PARENT = (By.XPATH, '..')

    COOKIE_BANNER_BUTTON = (By.XPATH, "//button[contains(@class, 'CookieBanner_button__')]")

    @staticmethod
    def BY_MAIL_TEST_ID(id):
        return (By.XPATH, f"//*[@data-test-id='{id}']")

    @staticmethod
    def BY_TEXT(text):
        return (By.XPATH, f".//*[text()='{text}']")

    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")

    @staticmethod
    def BY_TEST_ID(id):
        return (By.XPATH, f"//*[@data-testid='{id}']")

    VK_UI_SELECT_ELEMS = (By.XPATH, "//*[contains(concat(' ', @class, ' '), ' vkuiCustomSelectOption ')]")

    @staticmethod
    def VK_UI_SELECT_ELEM(text):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']")


class MainPageLocators(BasePageLocators):
    LOGO = (By.CLASS_NAME, "HeaderLeft_left__a9Si1")
    GO_TO_ACCOUNT = (By.LINK_TEXT, "Перейти в кабинет")
    HELP = (By.LINK_TEXT, "Справка")
    EDUCATION_TAB = (By.CLASS_NAME, "NavigationVKAdsItem_item__0_oac")
    EDUCATION_DROPDOWN = (By.CLASS_NAME, "NavigationVKAds_subNavigation__kFqx4")
    HAMBURGER = (By.CLASS_NAME, "HeaderWrapper_mobileMenuButton__D38On")
    FOOTER_GO_TO_ACCOUNT = (By.XPATH, "//*[contains(@class, 'Footer_leftContent__')]/a[text()='Перейти в кабинет']")
    FOOTER_GO_TO_BUSINESS = (
        By.XPATH,
        "//*[contains(@class, 'Footer_controls___')]/a[contains(@href, 'https://vk.company/ru/company/business/')]")
    FOOTER_LANGUAGE = (By.XPATH, "//div[contains(@class, 'Footer_control__')]")
    FOOTER_LANGUAGE_CONTENT = (By.XPATH, "//div[contains(@class, 'SelectLanguage_desktopSelect__')]/span")
    FOOTER_ABOUT = (By.XPATH, "//*[contains(@class, 'Footer_about__')]")

    def TAB(self, tab_name):
        return (By.LINK_TEXT, tab_name)

    @staticmethod
    def FOOTER_TAB(tab_name: str):
        return (By.XPATH, f"//*[contains(@class, 'Footer_item__')]/a[text()='{tab_name}']")

    @staticmethod
    def FOOTER_GROUP(url: str):
        return (By.XPATH, f"//a[contains(@class, 'Footer_control__')][contains(@href, '{url}')]")

    @staticmethod
    def FOOTER_LANGUAGE_SELECT_ELEMENT(language: Literal["English", "Русский"]):
        return (By.XPATH, f"//span[contains(@class, 'SelectLanguage_selectElem__')][text()='{language}']")


class RegistrationMainPageLocators(BasePageLocators):
    GO_TO_REGISTRATION = (By.CLASS_NAME, "SocialButton_socialButtonWrapper__0PXSG")
    MAIL_RU_AUTH = BasePageLocators.BY_MAIL_TEST_ID("oAuthService_mail_ru")
    MAIL_RU_SHOW_PASSWORD = BasePageLocators.BY_MAIL_TEST_ID("next-button")
    MAIL_RU_LOGIN = (By.NAME, "username")
    MAIL_RU_PASSWORD = (By.NAME, "password")
    MAIL_RU_SUBMIT = BasePageLocators.BY_MAIL_TEST_ID("submit-button")
    LOGIN = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')


class RegistrationPageLocators(BasePageLocators):
    AGENCY = BasePageLocators.BY_TEXT("Агентство")
    PHYSICAL = BasePageLocators.BY_TEXT("Физическое лицо")
    COUNTRY = BasePageLocators.BY_TEST_ID("country")
    CURRENCY = BasePageLocators.BY_TEST_ID("currency")
    EMAIL_INPUT = (By.NAME, "email")
    ERROR = (By.CLASS_NAME, "vkuiFormItem--status-error")
    CREATE_ACCOUNT = BasePageLocators.BY_TEXT("Создать кабинет")
    TERMS = (By.CLASS_NAME, "registration_offerTitle__BqyqW")
    FORM_ERROR = (By.CLASS_NAME, "vkuiFormStatus--mode-error")


class HqPageLocators(BasePageLocators):
    SETTINGS = (By.LINK_TEXT, "Настройки")
    DELETE_ACCOUNT = (By.CLASS_NAME, 'DeleteAccount_button__BEy7F')
    CONFIRM_DELETION = BasePageLocators.BY_TEXT('Да, удалить')
    CLOSE_HELP = BasePageLocators.BY_TEXT('Попробовать позже')


class AudiencePageLocators(HqPageLocators):
    CREATE_AUDIENCE = HqPageLocators.BY_TEST_ID("create-audience")
