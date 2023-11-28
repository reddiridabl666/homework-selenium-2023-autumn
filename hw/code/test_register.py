import time
from base import BaseCase,  credentials
from ui.fixtures import registration_main_page, registration_page, account_selection_cookies
import pytest


class TestRegistration(BaseCase):
    authorize = False

    def test_go_to_creation(self, registration_main_page, credentials):
        registration_main_page.go_to_account_creation(*credentials)

    def test_dummy(self, registration_page, account_selection_cookies):
        self.add_cookies(account_selection_cookies)
        self.driver.get(registration_page.url)

        self.print_cookies()

        time.sleep(1)

        self.print_cookies()

        registration_page.assert_url(registration_page.url)
