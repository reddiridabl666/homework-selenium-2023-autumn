from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


def keywords_payload(name='Название', keywords='образование', days='15'):
    return {'name': name, 'keywords': keywords, 'days': days}


class TextInput:
    def __init__(self, page: 'LeadPage', locators: tuple[tuple[str, str], tuple[str, str]], is_last_page: bool = False):
        self.page = page
        self.input_locator, self.error_locator = locators
        self.is_last_page = is_last_page

    def fill(self, text: str) -> WebElement:
        return self.page.fill_in(self.input_locator, text)

    def has_error(self) -> bool:
        return self.page.is_visible(self.error_locator, 1)

    def get_error(self) -> str:
        return self.page.find(self.error_locator).text

    def fill_and_get_error(self, text: str) -> tuple[True, str] | tuple[False, None]:
        self.fill(text)
        if self.is_last_page:
            self.page.click_processing_save()
        else:
            self.page.click_processing_next()

        if self.has_error():
            return (True, self.get_error())

        return (False, None)


class LeadPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = basic_locators.LeadPageLocators()

    def get_processing_stage(self) -> str:
        return self.find(self.locators.LEAD_PROCESSING_STAGE).text

    def open_create_lead(self):
        self.click(self.locators.CREATE_LEAD)

    def click_processing_next(self):
        self.click(self.locators.LEAD_PROCESSING_NEXT_BUTTON)

    def click_processing_save(self):
        self.click(self.locators.LEAD_PROCESSING_SAVE_BUTTON)

    def processing_formal_title(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_FORMAL_TITLE)

    def processing_formal_company(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_FORMAL_COMPANY)

    def processing_formal_text_title(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_FORMAL_TEXT_TITLE)

    def processing_formal_compact_desc(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_FORMAL_COMPACT_DESC)

    def processing_formal_select_logo(self):
        self.click(self.locators.LEAD_PROCESSING_FORMAL_LOGO)
        self.wait_for_count_of_elements(self.locators.IMAGE_CONTAINER_IMGS, 1)
        self.click_may_be_stale(self.locators.IMAGE_CONTAINER_IMGS)

    def has_processing_formal_logo_error(self) -> bool:
        return self.is_visible(self.locators.LEAD_PROCESSING_FORMAL_LOGO_ERROR)

    def get_processing_formal_logo_error(self) -> str:
        return self.find(self.locators.LEAD_PROCESSING_FORMAL_LOGO_ERROR).text

    def processing_formal_and_go_next(self, title: str | None = None):
        if title is not None:
            self.processing_formal_title().fill(title)
        self.processing_formal_select_logo()
        self.processing_formal_company().fill("company")
        self.processing_formal_text_title().fill("text_title")
        self.processing_formal_compact_desc().fill("desc")
        self.click_processing_next()

    def processing_question_add_question(self):
        self.click(self.locators.LEAD_PROCESSING_QUESTION_ADD_QUESTION)

    def processing_question_add_answer(self, question_number: int):
        self.click(self.locators.LEAD_PROCESSING_QUESTION_ADD_ANSWER(question_number))

    def processing_question_has_error(self) -> bool:
        return self.is_visible(self.locators.LEAD_PROCESSING_QUESTION_ERROR)

    def processing_question_fill_title(self, question_number: int, title: str):
        self.fill_in(self.locators.LEAD_PROCESSING_QUESTION_TITLE(question_number), title)

    def processing_question_fill_answer(self, question_number: int, answer_number: int, text: str):
        self.fill_in(self.locators.LEAD_PROCESSING_QUESTION_ANSWER(question_number, answer_number), text)

    def processing_result_title(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_RESULT_TITLE)

    def processing_result_desc(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_RESULT_DESC)

    def processing_settings_full_name(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_SETTINGS_FULL_NAME, True)

    def processing_settings_address(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_SETTINGS_ADDRESS, True)

    def processing_settings_email(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_SETTINGS_EMAIL, True)

    def processing_settings_inn(self):
        return TextInput(self, self.locators.LEAD_PROCESSING_SETTINGS_INN, True)

    def processing_settings_and_save(self):
        self.processing_settings_full_name().fill("Лат Ми Ан")
        self.processing_settings_address().fill("ул Пушкина дом")
        self.click_processing_save()

    def search(self, title_or_id: str | int):
        self.fill_in(self.locators.LEAD_SEARCH, str(title_or_id))

    def delete(self, title: str):
        self.hover(self.locators.LEAD_BY_TITLE(title))
        self.is_visible(self.locators.LEAD_DELETE_BY_TITLE(title))
        self.click_may_be_stale(self.locators.LEAD_DELETE_BY_TITLE(title))
        self.click_may_be_stale(self.locators.LEAD_CONFIRM_DELETE)

    def get_leads_count(self) -> int:
        return len(self.find_multiple(self.locators.LEAD_ALL_ITEMS))
