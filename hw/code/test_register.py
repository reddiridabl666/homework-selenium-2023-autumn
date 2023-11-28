import time
from base import BaseCase,  credentials
from ui.fixtures import registration_main_page, registration_page, account_selection_cookies
import pytest


class TestRegistration(BaseCase):
    authorize = False

    def test_go_to_creation(self, registration_main_page, credentials):
        registration_main_page.go_to_account_creation(*credentials)

    def test_account_type_radio(self, registration_page):
        registration_page.is_visible(registration_page.locators.PHYSICAL)
        registration_page.click(registration_page.locators.AGENCY)
        registration_page.is_not_visible(registration_page.locators.PHYSICAL)

    currency_test_args = [
        ('Беларусь', ('Доллар США (USD)', 'Евро (EUR)')),
        ('Россия', ('Российский рубль (RUB)',)),
    ]

    @pytest.mark.parametrize('country,currencies', currency_test_args)
    def test_currency_select(self, registration_page, country, currencies):
        registration_page.select_country(country)
        assert registration_page.available_currencies() == currencies

    def test_no_email(self, registration_page):
        registration_page.fill_in_form('')
        registration_page.has_email_error()

    def test_no_terms(self, registration_page):
        registration_page.fill_in_form('example@mail.ru', terms_accepted=False)
        registration_page.has_terms_error()

    def test_long_email(self, registration_page):
        long_email = f"{'a'*255}@mail.ru"
        registration_page.fill_in_form(long_email)
        registration_page.has_global_error()

    bad_emails = [
        'abcmail.ru',
        'example@mail.r'
    ]

    @pytest.mark.parametrize('email', bad_emails)
    def test_bad_email_format(self, registration_page, email):
        registration_page.fill_in_form(email)
        registration_page.has_email_error(error='Некорректный email адрес')

    def test_ok(self, registration_page):
        registration_page.fill_in_form('example@mail.org')
        registration_page.assert_url('https://ads.vk.com/hq/dashboard')
