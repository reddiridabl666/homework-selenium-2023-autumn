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
