from selenium.webdriver.common.by import By


class BasePageLocators:
    PARENT = (By.XPATH, '..')

    @staticmethod
    def BTN_BY_TEXT(text):
        return (By.XPATH, f'//button[text()="{text}"]')

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
    SITE_TAB = BasePageLocators.BTN_BY_TEXT("Для сайтов")
    # MOBILE_TAB = BasePageLocators.BTN_BY_TEXT("Для приложений")
    MOBILE_TAB = (By.XPATH, '//*[@id="__next"]/article/div/div[2]/div[2]/div[2]/button[2]')
