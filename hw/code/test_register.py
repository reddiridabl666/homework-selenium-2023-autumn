from base import BaseCase
from ui.fixtures import registration_main_page, no_cabinet_credentials, registration_page
from ui.pages.registration_page import RegistrationPage
import pytest


class TestRegistration(BaseCase):
    NO_FIELD_ERROR = 'Обязательное поле'
    INVALID_EMAIL_ERROR = 'Некорректный email адрес'

    def test_go_to_creation(self, registration_main_page, no_cabinet_credentials):
        registration_main_page.go_to_account_creation(*no_cabinet_credentials)
        assert self.is_url_open(RegistrationPage.url)

    def test_account_type_radio(self, registration_page):
        registration_page.choose_agency_account_type()
        assert registration_page.is_physical_type_not_visible()

    currency_test_args = [
        ('Беларусь', ('Доллар США (USD)', 'Евро (EUR)')),
        ('Россия', ('Российский рубль (RUB)',)),
    ]

    @pytest.mark.parametrize('country,currencies', currency_test_args)
    def test_currency_select(self, registration_page, country, currencies):
        registration_page.select_country(country)
        assert registration_page.available_currencies_after_country_change(
            currencies[0]) == currencies

    def test_no_email(self, registration_page):
        registration_page.fill_in_form('')
        assert registration_page.email_error(self.NO_FIELD_ERROR) is not None

    def test_no_terms(self, registration_page):
        example_mail = 'example@mail.ru'
        registration_page.fill_in_form(example_mail, terms_accepted=False)
        assert registration_page.terms_not_accepted_error() is not None

    def test_long_email(self, registration_page):
        long_email = f"{'a'*255}@mail.ru"
        registration_page.fill_in_form(long_email)
        assert registration_page.global_error() is not None

    bad_emails = [
        'abcmail.ru',
        'example@mail.r'
    ]

    @pytest.mark.parametrize('email', bad_emails)
    def test_bad_email_format(self, registration_page, email):
        registration_page.fill_in_form(email)
        assert registration_page.email_error(
            error=self.INVALID_EMAIL_ERROR) is not None
