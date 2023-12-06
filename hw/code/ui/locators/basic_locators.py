from selenium.webdriver.common.by import By


class BasePageLocators:
    PARENT = (By.XPATH, '..')

    @staticmethod
    def BTN_BY_TEXT(text):
        return (By.XPATH, f'//button[text()="{text}"] | //button//*[text()="{text}"]/ancestor::button')

    @staticmethod
    def DIV_BY_TEXT(text):
        return (By.XPATH, f'//div[text()="{text}"]')


class MainPageLocators(BasePageLocators):
    LOGO = (By.CLASS_NAME, "HeaderLeft_left__a9Si1")
    GO_TO_ACCOUNT = (By.LINK_TEXT, "Перейти в кабинет")
    HELP = (By.LINK_TEXT, "Справка")
    EDUCATION_TAB = (By.CLASS_NAME, "NavigationVKAdsItem_item__0_oac")
    EDUCATION_DROPDOWN = (
        By.CLASS_NAME, "NavigationVKAds_subNavigation__kFqx4")
    HAMBURGER = (By.CLASS_NAME, "HeaderWrapper_mobileMenuButton__D38On")

    def TAB(self, tab_name):
        return (By.LINK_TEXT, tab_name)


class PartnerPageLocators(BasePageLocators):
    GO_TO_ACCOUNT = (By.LINK_TEXT, "Перейти в кабинет")
    HELP = (By.LINK_TEXT, "Справка")

    @staticmethod
    def DIV_IN_ACTIVE_TAB_BY_TEXT(text):
        return (By.XPATH, f"//div[contains(@class, 'tabContentActive')]//div[text()='{text}']")

    SITE_TAB = BasePageLocators.BTN_BY_TEXT("Для сайтов")
    MOBILE_TAB = BasePageLocators.BTN_BY_TEXT("Для приложений")

    FORM_SUBMIT_BTN = BasePageLocators.BTN_BY_TEXT("Отправить")
    FORM_NAME_INPUT = (By.NAME, 'name')
    FORM_EMAIL_INPUT = (By.NAME, 'email')
    FORM_SUBMIT_MSG = BasePageLocators.DIV_BY_TEXT('Спасибо, ваша заявка принята')


class HelpPageLocators(BasePageLocators):
    @staticmethod
    def GET_LINK_WITH_DIV_TEXT(text):
        return (By.XPATH, f'//a//*[text()="{text}"]/ancestor::a')
    
    AUTHORIZE_LINK = GET_LINK_WITH_DIV_TEXT('Авторизация')
    HOW_TO_TUNE_LINK = GET_LINK_WITH_DIV_TEXT('Как настроить рекламу')
    TOOLS_LINK = GET_LINK_WITH_DIV_TEXT('Инструменты рекламы')
    STATISTICS_AND_FINANCE_LINK = GET_LINK_WITH_DIV_TEXT('Статистика и финансы')
    DOCUMENTS_LINK = GET_LINK_WITH_DIV_TEXT('Документы')
    SIMPLIFIED_LINK = GET_LINK_WITH_DIV_TEXT('Упрощенный кабинет')
    FAQ_LINK = GET_LINK_WITH_DIV_TEXT('FAQ')
    PARTNER_CABINET_LINK = GET_LINK_WITH_DIV_TEXT('Кабинет партнера')

    SEARCH = (By.XPATH, '//input[@placeholder="Статистика, правила, пополнение..."]')
    SEARCH_SUGGESTIONS = (By.XPATH, '//div[contains(@class, "fullscreenSuggestions")]')
