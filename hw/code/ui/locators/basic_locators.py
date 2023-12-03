from selenium.webdriver.common.by import By


class BasePageLocators:
    PARENT = (By.XPATH, '..')

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

    VK_UI_SELECT_ELEMS = (
        By.XPATH, f"//*[contains(concat(' ', @class, ' '), ' vkuiCustomSelectOption ')]")

    @staticmethod
    def VK_UI_SELECT_ELEM(text):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']")

    ERROR = (By.CLASS_NAME, "vkuiFormItem--status-error")


class MainPageLocators(BasePageLocators):
    LOGO = (By.CLASS_NAME, "HeaderLeft_left__a9Si1")
    GO_TO_ACCOUNT = (By.LINK_TEXT, "Перейти в кабинет")
    HELP = (By.LINK_TEXT, "Справка")
    EDUCATION_TAB = (By.CLASS_NAME, "NavigationVKAdsItem_item__0_oac")
    EDUCATION_DROPDOWN = (
        By.CLASS_NAME, "NavigationVKAds_subNavigation__kFqx4")
    HAMBURGER = (By.CLASS_NAME, "HeaderWrapper_mobileMenuButton__D38On")

    @staticmethod
    def TAB(tab_name):
        return (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_link__9JjBI')][text()='{tab_name}']")

    @staticmethod
    def DROPDOWN_TAB(tab_name):
        return (By.XPATH, f"//*[contains(@class, 'SubNavigationItem_title__2kBnJ')][text()='{tab_name}']")


class RegistrationMainPageLocators(BasePageLocators):
    GO_TO_REGISTRATION = (
        By.CLASS_NAME, "SocialButton_socialButtonWrapper__0PXSG")
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

    AUDIENCE_NAME = (By.CLASS_NAME, 'vkuiInput__el')

    SOURCE_NAME = (By.XPATH, "(//*[contains(@class, 'vkuiInput__el')])[2]")

    KEYWORDS = (
        By.XPATH, "(//*[contains(@class, 'KeyPhrases_textarea__wzycT')])[1]//textarea")

    NEGATIVE_KEYWORDS = (
        By.XPATH, "(//*[contains(@class, 'KeyPhrases_textarea__wzycT')])[2]//textarea")

    SAVE_AUDIENCE = (By.XPATH, "(//button[@type='submit'])[1]")

    SAVE_SOURCE = (By.XPATH, "(//button[@type='submit'])[2]")

    @staticmethod
    def AUDIENCE_CHECKBOX(name):
        return (By.XPATH, f"*//[contains(@class, 'BaseTable__row') and contains(.//*, '{name}')]//[contains(@class, 'simpleCheckbox_simpleCheckbox__V0tiX')]")

    @staticmethod
    def AUDIENCE_DETAILS(name):
        return (By.XPATH, f"//*[contains(.//*, '{name}')]//button[@data-testid='audience-item-menu']")

    DAYS_INPUT = (
        By.XPATH, "//*[contains(@class, 'Context_daysInput__zQlWQ')]//input")

    @staticmethod
    def AUDIENCE_SOURCE(id):
        return (By.XPATH, f"(//*[contains(@class, 'SourceListItem_sourceListItem__i81J9')])[{id+1}]")

    AUDIENCE_SOURCE_ITEM = (By.CLASS_NAME, 'InfoRow_content__LN5Bb')
    AUDIENCE_SOURCE_NAME = (By.CLASS_NAME, 'vkuiHeadline')

    RULE = (By.CLASS_NAME, 'SourceRuleItem_rule__FEL5b')
    RULE_SELECTOR = (By.CLASS_NAME, 'HintSelector_hintSelectorButton__pfubH')

    def AUDIENCE_SELECT_ITEM(audience_name):
        return (By.XPATH, f"//*[contains(@class, 'ExistsAudience_option__VEao1')][text()='{audience_name}']")

    AUDIENCE_SELECT = (By.CLASS_NAME, 'vkuiCustomSelect')

    AUDIENCE_CREATION_MODAL = (
        By.CLASS_NAME, 'ModalSidebarPage_container__Zopae')

    @staticmethod
    def AUDIENCE_FILTER_VALUE(audience_source):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__children')][text()='{audience_source}']")

    SHOWN_AUDIENCES = (By.CLASS_NAME, 'NameCell_name__lgrNA')
