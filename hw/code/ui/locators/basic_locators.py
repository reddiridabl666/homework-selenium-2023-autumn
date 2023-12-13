from selenium.webdriver.common.by import By


class BasePageLocators:
    PARENT = (By.XPATH, '..')

    @staticmethod
    def BTN_BY_TEXT(text):
        return (By.XPATH, f'//button[text()="{text}"] | //button//*[text()="{text}"]/ancestor::button')

    @staticmethod
    def DIV_BY_TEXT(text):
        return (By.XPATH, f'//div[text()="{text}"]')

    @staticmethod
    def SPAN_BY_TEXT(text):
        return (By.XPATH, f'//span[text()="{text}"]')

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
        By.XPATH, f"(//*[contains(@class, 'ModalSidebarPage_container__Zopae')])[1]")

    SOURCE_CREATION_MODAL = (
        By.XPATH, f"(//*[contains(@class, 'ModalSidebarPage_container__Zopae')])[2]")

    AUDIENCE_FILTERS_SELECTED = (By.CLASS_NAME, 'vkuiCheckbox__icon--on')

    @staticmethod
    def AUDIENCE_FILTER_VALUE(audience_source):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__children')][text()='{audience_source}']")

    SHOWN_AUDIENCES = (By.CLASS_NAME, 'NameCell_name__lgrNA')


class AdGroupsPageLocators(HqPageLocators):
    SITE_CONVERSIONS = (By.XPATH, "//*[@data-id='site_conversions']")

    SITE_NAME = (By.XPATH, "//*[@placeholder='Введите ссылку на сайт']")

    TARGET_PRICE = BasePageLocators.BY_TEST_ID('targeting-not-set')

    NEXT = BasePageLocators.BY_TEXT('Продолжить')

    CREATE = BasePageLocators.BY_TEST_ID('create-button')

    ERROR_TOOLTIP = (By.CLASS_NAME, 'ErrorsTooltip_button__YyIDS')

    SELECT_ALL = (
        By.XPATH, "//*[contains(@class, 'vkuiCheckbox')][input[@id='checkbox-all']]")

    DELETE = BasePageLocators.BY_TEXT('Удалить')

    CONFIRM_DELETE = (
        By.XPATH, "//*[contains(@class, 'confirmRemoveModal_footer__dW3aB')]//*[text()='Удалить']")


class AdGroupCreationPageLocators(BasePageLocators):
    REGION_SEARCH = (
        By.XPATH, "//*[contains(@class, 'RegionsSelector_search__j4BBI')]//input")

    @staticmethod
    def REGION_SEARCH_ITEM(region_name):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__children')][text()='{region_name}']")

    REGION_SEARCH_ITEMS = (By.CLASS_NAME, 'vkuiCheckbox__children')

    REGION_LIST_ITEMS = (By.CLASS_NAME, 'RegionsList_label__KPYrN')

    @staticmethod
    def REGION_LIST_REMOVE_ITEM(region_name):
        return (By.XPATH, f"//*[contains(@class, 'RegionsList_item__5Z8rf') and contains(.//*, '{region_name}')]//*[contains(@class, 'RegionsList_remove__pl6kK')]")

    CLEAR_REGION_LIST = (By.CLASS_NAME, 'RegionsSelector_clear__mTOGS')


class EcommPageLocators(BasePageLocators):
    CREATE_CATALOG_BTN = BasePageLocators.BTN_BY_TEXT("Создать каталог")
    CREATE_CATALOG_MODAL = (By.CLASS_NAME, "ModalRoot_componentWrapper__uzHTL")

    class CreateCatalogModal:
        @staticmethod
        def TAB_BY_TEXT(text):
            return (By.XPATH, f'//div/span[text()="{text}"]')
        FEED_BTN = TAB_BY_TEXT("Фид или сообщество")
        MARKETPLACE_BTN = TAB_BY_TEXT("Маркетплейс")
        MANUAL_BTN = TAB_BY_TEXT("Вручную")

        FEED_LABEL = BasePageLocators.SPAN_BY_TEXT("Ссылка на фид или сообщество")
        MARKETPLACE_LABEL = BasePageLocators.SPAN_BY_TEXT("Ссылка на страницу продавца")
        MANUAL_LABEL = BasePageLocators.SPAN_BY_TEXT("Категория фида")

        MANUAL_FILE_SELECTOR = (By.XPATH, '//label[contains(@class, "FileSelector")]//input')
        SUBMIT_CATALOG_BTN = (By.XPATH, '//button[@type="submit"]//span[text()="Создать каталог"]/ancestor::button')

    create_catalog_modal = CreateCatalogModal()

    FEED_LOADING = BasePageLocators.SPAN_BY_TEXT('Загрузка фида')
    CATALOG = (By.XPATH, '//span[contains(text(), "Каталог")]')
    SETTINGS_BTN = BasePageLocators.BTN_BY_TEXT("Настройки")
    SETTINGS_MODAL = (By.XPATH, '//div[contains(@class, "ModalRoot_componentWrapper")]')

    ADD_GOODS_BTN = BasePageLocators.BTN_BY_TEXT("Добавить товары")
    PROMOTE_BTN = BasePageLocators.SPAN_BY_TEXT("Рекламировать")


class SitesPageLocators(BasePageLocators):
    ADD_PIXEL_BTN = BasePageLocators.BTN_BY_TEXT("Добавить пиксель")
    
    ADD_PIXEL_MODAL = (By.XPATH, '//div[contains(@class, "ModalRoot_componentWrapper")]')
    CLOSE_MODAL_BTN = (By.CLASS_NAME, 'vkuiModalDismissButton')

    DOMAIN_INPUT = (By.XPATH, '//input[@placeholder="Домен сайта"]')
    DOMAIN_SUBMIT_BTN = (By.XPATH, '//div[contains(@class, "ModalRoot")]//button//*[text()="Добавить пиксель"]/ancestor::button')
    PIXEL_ADDED_MODAL = (By.XPATH, '//h2[contains(text(), "Создан ID пикселя")]')
    SETTINGS_LINK = (By.LINK_TEXT, 'Настройка')
