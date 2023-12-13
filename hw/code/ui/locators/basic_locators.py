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

    ERROR = (By.CLASS_NAME, "vkuiFormItem--status-error")


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

    @staticmethod
    def TAB(tab_name):
        return (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_link__9JjBI')][text()='{tab_name}']")

    @staticmethod
    def DROPDOWN_TAB(tab_name):
        return (By.XPATH, f"//*[contains(@class, 'SubNavigationItem_title__2kBnJ')][text()='{tab_name}']")

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

    KEYWORDS = (By.XPATH, "(//*[contains(@class, 'KeyPhrases_textarea__wzycT')])[1]//textarea")

    NEGATIVE_KEYWORDS = (By.XPATH, "(//*[contains(@class, 'KeyPhrases_textarea__wzycT')])[2]//textarea")

    SAVE_AUDIENCE = (By.XPATH, "(//button[@type='submit'])[1]")

    SAVE_SOURCE = (By.XPATH, "(//button[@type='submit'])[2]")

    @staticmethod
    def AUDIENCE_CHECKBOX(name):
        return (
            By.XPATH,
            f"*//[contains(@class, 'BaseTable__row') and contains(.//*, '{name}')]//[contains(@class, 'simpleCheckbox_simpleCheckbox__V0tiX')]"
        )

    @staticmethod
    def AUDIENCE_DETAILS(name):
        return (By.XPATH, f"//*[contains(.//*, '{name}')]//button[@data-testid='audience-item-menu']")

    DAYS_INPUT = (By.XPATH, "//*[contains(@class, 'Context_daysInput__zQlWQ')]//input")

    @staticmethod
    def AUDIENCE_SOURCE(id):
        return (By.XPATH, f"(//*[contains(@class, 'SourceListItem_sourceListItem__i81J9')])[{id+1}]")

    AUDIENCE_SOURCE_ITEM = (By.CLASS_NAME, 'InfoRow_content__LN5Bb')
    AUDIENCE_SOURCE_NAME = (By.CLASS_NAME, 'vkuiHeadline')

    RULE = (By.CLASS_NAME, 'SourceRuleItem_rule__FEL5b')
    RULE_SELECTOR = (By.CLASS_NAME, 'HintSelector_hintSelectorButton__pfubH')

    @staticmethod
    def AUDIENCE_SELECT_ITEM(audience_name):
        return (By.XPATH, f"//*[contains(@class, 'ExistsAudience_option__VEao1')][text()='{audience_name}']")

    AUDIENCE_SELECT = (By.CLASS_NAME, 'vkuiCustomSelect')

    AUDIENCE_CREATION_MODAL = (By.XPATH, f"(//*[contains(@class, 'ModalSidebarPage_container__Zopae')])[1]")

    SOURCE_CREATION_MODAL = (By.XPATH, f"(//*[contains(@class, 'ModalSidebarPage_container__Zopae')])[2]")

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

    SELECT_ALL = (By.XPATH, "//*[contains(@class, 'vkuiCheckbox')][input[@id='checkbox-all']]")

    DELETE = BasePageLocators.BY_TEXT('Удалить')

    CONFIRM_DELETE = (By.XPATH, "//*[contains(@class, 'confirmRemoveModal_footer__dW3aB')]//*[text()='Удалить']")


class AdGroupCreationPageLocators(BasePageLocators):
    REGION_SEARCH = (By.XPATH, "//*[contains(@class, 'RegionsSelector_search__j4BBI')]//input")

    @staticmethod
    def REGION_SEARCH_ITEM(region_name):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__children')][text()='{region_name}']")

    REGION_SEARCH_ITEMS = (By.CLASS_NAME, 'vkuiCheckbox__children')

    REGION_LIST_ITEMS = (By.CLASS_NAME, 'RegionsList_label__KPYrN')

    @staticmethod
    def REGION_LIST_REMOVE_ITEM(region_name):
        return (
            By.XPATH,
            f"//*[contains(@class, 'RegionsList_item__5Z8rf') and contains(.//*, '{region_name}')]//*[contains(@class, 'RegionsList_remove__pl6kK')]"
        )

    CLEAR_REGION_LIST = (By.CLASS_NAME, 'RegionsSelector_clear__mTOGS')


class UpvotePageLocators(BasePageLocators):
    SEARCH_FIELD = (By.XPATH, "//input[contains(@class, 'vkuiSearch__input')]")

    IDEAS_COUNT = (By.XPATH, "//div[contains(@class, 'Idea_cardVote__')]")

    IDEA_THEME_SELECT = (By.XPATH, "(//div[contains(@class, 'vkuiSelect__container')])[1]")
    IDEA_STATUS_SELECT = (By.XPATH, "(//div[contains(@class, 'vkuiSelect__container')])[2]")

    IDEA_TITLE = (By.XPATH, "//*[contains(@class, 'Idea_title__')]")

    @staticmethod
    def IDEA_LINK(title: str):
        return (By.XPATH, f"//a[contains(@class, 'Idea_title__')][text()='{title}']")


class ImageContainer(BasePageLocators):
    IMAGE_CONTAINER_IMGS = (By.XPATH, "//*[contains(@class, 'ImageItems_imageItem__')]")


class LeadPageLocators(ImageContainer):
    ERROR_FIELD_REQUIRED = "Обязательное поле"
    ERROR_FIELD_MAX_LENGTH_LIMIT = "Превышена максимальная длина поля"
    ERROR_FIELD_WRONG_EMAIL = "Некорректный email адрес"

    LEAD_PROCESSING_FORMAL_STAGE_BAD = "Оформление"
    LEAD_PROCESSING_FORMAL_STAGE_GOOD = "1\n" + LEAD_PROCESSING_FORMAL_STAGE_BAD
    LEAD_PROCESSING_QUESTION_STAGE_BAD = "Вопросы"
    LEAD_PROCESSING_QUESTION_STAGE_GOOD = "2\n" + LEAD_PROCESSING_QUESTION_STAGE_BAD
    LEAD_PROCESSING_RESULT_STAGE_BAD = "Результат"
    LEAD_PROCESSING_RESULT_STAGE_GOOD = "3\n" + LEAD_PROCESSING_RESULT_STAGE_BAD
    LEAD_PROCESSING_SETTINGS_STAGE_BAD = "Настройки"
    LEAD_PROCESSING_SETTINGS_STAGE_GOOD = "4\n" + LEAD_PROCESSING_SETTINGS_STAGE_BAD

    @staticmethod
    def _BY_PLACEHOLDER_FIELD_WITH_ERROR(placeholder: str) -> tuple[tuple[str, str], tuple[str, str]]:
        input_xpath = f"//input[@placeholder='{placeholder}']"
        error_xpath = input_xpath + "/../../span[contains(@class, 'vkuiFormItem__bottom')]/div"
        return ((By.XPATH, input_xpath), (By.XPATH, error_xpath))

    @staticmethod
    def _BY_H5_FIELD_WITH_ERROR(title: str) -> tuple[tuple[str, str], tuple[str, str]]:
        base_xpath = f"//h5[contains(@class, 'vkuiSubhead')][text()='{title}']/.."
        input_xpath = base_xpath + "/span[contains(@class, 'vkuiFormField')]/input"
        error_xpath = base_xpath + "/span[contains(@class, 'vkuiFormItem__bottom')]/div"
        return ((By.XPATH, input_xpath), (By.XPATH, error_xpath))

    CREATE_LEAD = (By.XPATH, "//button[contains(@class, 'LeadForms_createButton__')]")

    LEAD_PROCESSING_STAGE = (By.XPATH, "//div[contains(@class, 'CreateLeadFormModal_activeStep__')]")

    LEAD_PROCESSING_FORMAL_LOGO = BasePageLocators.BY_TEST_ID("set-global-image")

    LEAD_PROCESSING_FORMAL_LOGO_ERROR = (By.XPATH, "//*[@data-testid='set-global-image']/../span/div")

    LEAD_PROCESSING_FORMAL_TITLE = _BY_PLACEHOLDER_FIELD_WITH_ERROR("Название лид-формы")
    LEAD_PROCESSING_FORMAL_COMPANY = _BY_PLACEHOLDER_FIELD_WITH_ERROR("Название компании")
    LEAD_PROCESSING_FORMAL_TEXT_TITLE = _BY_PLACEHOLDER_FIELD_WITH_ERROR("Текст заголовка")
    LEAD_PROCESSING_FORMAL_COMPACT_DESC = _BY_PLACEHOLDER_FIELD_WITH_ERROR("Краткое описание опроса")

    LEAD_PROCESSING_NEXT_BUTTON = (By.XPATH, "//button[@title='Продолжить']")
    LEAD_PROCESSING_SAVE_BUTTON = (By.XPATH, "//button[@title='Сохранить']")

    LEAD_PROCESSING_QUESTION_ADD_QUESTION = (
        By.XPATH, "//span[contains(@class, 'vkuiButton__content')][text()='Добавить вопрос']")

    @staticmethod
    def LEAD_PROCESSING_QUESTION_TITLE(question_number: int):
        return (By.XPATH, f"(//textarea[@placeholder='Напишите вопрос'])[{question_number}]")

    LEAD_PROCESSING_QUESTION_ALL_QUESTIONS = (By.XPATH, "//div[contains(@class, 'Questions_questionsDroppable__')]/div")

    LEAD_PROCESSING_QUESTION_ERROR = (
        By.XPATH, "//div[contains(@class, 'Question_question__')]//div[contains(@class, 'Hint_hintTrigger')]")

    @staticmethod
    def LEAD_PROCESSING_QUESTION_ANSWER(question_number: int, answer_number: int):
        return (
            By.XPATH,
            f"((//div[contains(@class, 'Question_question__')])[{question_number}]//input[@placeholder='Введите ответ'])[{answer_number}]"
        )

    @staticmethod
    def LEAD_PROCESSING_QUESTION_ADD_ANSWER(question_number: int):
        return (
            By.XPATH,
            f"(//div[contains(@class, 'Question_question__')])[{question_number}]//span[contains(@class, 'vkuiButton__content')][text()='Добавить ответ']"
        )

    @staticmethod
    def LEAD_PROCESSING_QUESTION_ALL_ANSWERS(question_number: int):
        return (By.XPATH, f"(//div[contains(@class, 'Question_answersDroppable__')])[{question_number}]/div")

    LEAD_PROCESSING_RESULT_TITLE = _BY_H5_FIELD_WITH_ERROR("Заголовок")
    LEAD_PROCESSING_RESULT_DESC = _BY_H5_FIELD_WITH_ERROR("Описание")

    LEAD_PROCESSING_SETTINGS_FULL_NAME = _BY_PLACEHOLDER_FIELD_WITH_ERROR("Введите фамилию, имя и отчество")
    LEAD_PROCESSING_SETTINGS_ADDRESS = _BY_PLACEHOLDER_FIELD_WITH_ERROR("Введите адрес")
    LEAD_PROCESSING_SETTINGS_EMAIL = _BY_PLACEHOLDER_FIELD_WITH_ERROR("Введите email")
    LEAD_PROCESSING_SETTINGS_INN = _BY_PLACEHOLDER_FIELD_WITH_ERROR("Введите ИНН")

    LEAD_SEARCH = (By.XPATH, "//div[contains(@class, 'vkuiSearch__input')]")

    LEAD_ALL_ITEMS = (By.XPATH, "//button[contains(@class, 'NameCell_link__')]")

    @staticmethod
    def LEAD_BY_TITLE(title: str):
        return (By.XPATH, f"//button[contains(@class, 'NameCell_link__')][text()='{title}']")

    @staticmethod
    def LEAD_DELETE_BY_TITLE(title: str):
        return (
            By.XPATH,
            f"//button[contains(@class, 'NameCell_link__')][text()='{title}']/../div/div/button/span[text()='Удалить']")

    LEAD_CONFIRM_DELETE = (By.XPATH, "//div[contains(@class, 'ModalConfirm_wrapper__')]//*[text()='Удалить']")
