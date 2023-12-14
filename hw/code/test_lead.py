from typing import Callable
import time
import pytest
from base import BaseCase
from ui.pages.lead_page import LeadPage, TextInput

CallableTextInput = Callable[[LeadPage], TextInput]

formal_text_fields_error_more = [
    (LeadPage.processing_formal_title, 255),
    (LeadPage.processing_formal_company, 30),
    (LeadPage.processing_formal_text_title, 50),
    (LeadPage.processing_formal_compact_desc, 35),
]

formal_text_fields_error_empty = [
    (LeadPage.processing_formal_title),
    (LeadPage.processing_formal_company),
    (LeadPage.processing_formal_text_title),
    (LeadPage.processing_formal_compact_desc),
]

result_text_fields_error_more = [
    (LeadPage.processing_result_title, 25),
    (LeadPage.processing_result_desc, 160),
]

settings_text_fields_error_more = [
    (LeadPage.processing_settings_full_name, 255),
    (LeadPage.processing_settings_address, 255),
    (LeadPage.processing_settings_inn, 32),
]

settings_text_fields_error_empty = [
    (LeadPage.processing_settings_full_name),
    (LeadPage.processing_settings_address),
]


class TestLead(BaseCase):
    @pytest.mark.parametrize("text_field,max_len", formal_text_fields_error_more)
    def test_lead_processing_formal_fields_error_more(self, lead_page: LeadPage, text_field: CallableTextInput,
                                                      max_len: int):
        lead_page.open_create_lead()
        has_error, error = text_field(
            lead_page).fill_and_get_error("a" * (max_len + 1))
        assert has_error and error == lead_page.locators.ERROR_FIELD_MAX_LENGTH_LIMIT
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_FORMAL_STAGE_BAD

    @pytest.mark.parametrize("text_field", formal_text_fields_error_empty)
    def test_lead_processing_formal_fields_error_empty(self, lead_page: LeadPage, text_field: CallableTextInput):
        lead_page.open_create_lead()
        has_error, error = text_field(lead_page).fill_and_get_error("")
        assert has_error and error == lead_page.locators.ERROR_FIELD_REQUIRED
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_FORMAL_STAGE_BAD

    def test_lead_processing_formal_logo_error(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.click_processing_next()

        assert lead_page.has_processing_formal_logo_error()
        assert lead_page.get_processing_formal_logo_error(
        ) == lead_page.locators.ERROR_FIELD_REQUIRED
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_FORMAL_STAGE_BAD

    def test_lead_processing_formal_good(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_title().fill("title")
        lead_page.processing_formal_select_logo()
        lead_page.processing_formal_company().fill("company")
        lead_page.processing_formal_text_title().fill("text_title")
        lead_page.processing_formal_compact_desc().fill("desc")
        lead_page.click_processing_next()

        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_QUESTION_STAGE_GOOD

    def test_lead_processing_question_empty_good(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()

        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_RESULT_STAGE_GOOD

    def test_lead_processing_question_title_and_answers_error(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()

        lead_page.processing_question_add_question()
        lead_page.click_processing_next()

        assert lead_page.processing_question_has_error()
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_QUESTION_STAGE_BAD

    def test_lead_processing_question_title_error(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()

        lead_page.processing_question_add_question()
        lead_page.processing_question_fill_answer(1, 1, "a 1 1")
        lead_page.processing_question_fill_answer(1, 2, "a 1 2")
        lead_page.click_processing_next()

        assert lead_page.processing_question_has_error()
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_QUESTION_STAGE_BAD

    def test_lead_processing_question_answers_error(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()

        lead_page.processing_question_add_question()
        lead_page.processing_question_fill_title(1, "q_title")
        lead_page.click_processing_next()

        assert lead_page.processing_question_has_error()
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_QUESTION_STAGE_BAD

    def test_lead_processing_question_filled_good(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()

        lead_page.processing_question_add_question()
        lead_page.processing_question_fill_title(1, "q_title")
        lead_page.processing_question_fill_answer(1, 1, "a 1 1")
        lead_page.processing_question_fill_answer(1, 2, "a 1 2")
        lead_page.click_processing_next()

        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_RESULT_STAGE_GOOD

    @pytest.mark.parametrize("text_field,max_len", result_text_fields_error_more)
    def test_lead_processing_result_fields_error_more(self, lead_page: LeadPage, text_field: CallableTextInput,
                                                      max_len: int):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()

        has_error, error = text_field(
            lead_page).fill_and_get_error("a" * (max_len + 1))
        assert has_error and error == lead_page.locators.ERROR_FIELD_MAX_LENGTH_LIMIT
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_RESULT_STAGE_BAD

    def test_lead_processing_result_fields_error_empty(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()

        has_error, error = lead_page.processing_result_title().fill_and_get_error("")
        assert has_error and error == lead_page.locators.ERROR_FIELD_REQUIRED
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_RESULT_STAGE_BAD

    def test_lead_processing_result_default_good(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()
        lead_page.click_processing_next()
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_SETTINGS_STAGE_GOOD

    def test_lead_processing_result_desc_empty_good(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()

        lead_page.processing_result_title().fill("result title")
        lead_page.processing_result_desc().fill("")
        lead_page.click_processing_next()

        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_SETTINGS_STAGE_GOOD

    def test_lead_processing_result_filled_good(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()

        lead_page.processing_result_title().fill("result title")
        lead_page.processing_result_desc().fill("result desc")
        lead_page.click_processing_next()

        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_SETTINGS_STAGE_GOOD

    @pytest.mark.parametrize("text_field,max_len", settings_text_fields_error_more)
    def test_lead_processing_settings_fields_error_more(self, lead_page: LeadPage, text_field: CallableTextInput,
                                                        max_len: int):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()
        lead_page.click_processing_next()

        has_error, error = text_field(
            lead_page).fill_and_get_error("a" * (max_len + 1))
        assert has_error and error == lead_page.locators.ERROR_FIELD_MAX_LENGTH_LIMIT
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_SETTINGS_STAGE_BAD

    @pytest.mark.parametrize("text_field", settings_text_fields_error_empty)
    def test_lead_processing_settings_fields_error_empty(self, lead_page: LeadPage, text_field: CallableTextInput):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()
        lead_page.click_processing_next()

        has_error, error = text_field(lead_page).fill_and_get_error("")
        assert has_error and error == lead_page.locators.ERROR_FIELD_REQUIRED
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_SETTINGS_STAGE_BAD

    def test_lead_processing_settings_email_error_more(self, lead_page: LeadPage):
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next()
        lead_page.click_processing_next()
        lead_page.click_processing_next()

        has_error, error = lead_page.processing_settings_email(
        ).fill_and_get_error("a" * 66 + "@mail.ru")
        assert has_error and error == lead_page.locators.ERROR_FIELD_WRONG_EMAIL
        assert lead_page.get_processing_stage(
        ) == lead_page.locators.LEAD_PROCESSING_SETTINGS_STAGE_BAD

    def test_lead_processing_settings_good(self, lead_page: LeadPage):
        title = "test_form"
        assert lead_page.get_leads_count() == 0
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next(title)
        lead_page.click_processing_next()
        lead_page.click_processing_next()

        lead_page.processing_settings_full_name().fill("Лат Ми Ан")
        lead_page.processing_settings_address().fill("ул Пушкина дом")
        lead_page.click_processing_save()

        assert lead_page.get_leads_count() == 1

        lead_page.delete(title)

    def test_lead_delete(self, lead_page: LeadPage):
        title = "test_form"
        assert lead_page.get_leads_count() == 0
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next(title)
        lead_page.click_processing_next()
        lead_page.click_processing_next()
        lead_page.processing_settings_and_save()

        assert lead_page.get_leads_count() == 1

        lead_page.delete(title)

    def test_lead_search(self, lead_page: LeadPage):
        title = "test_form"
        lead_page.open_create_lead()
        lead_page.processing_formal_and_go_next(title)
        lead_page.click_processing_next()
        lead_page.click_processing_next()
        lead_page.processing_settings_and_save()

        lead_page.search(title)

        assert lead_page.get_leads_count() == 1

        lead_page.delete(title)
