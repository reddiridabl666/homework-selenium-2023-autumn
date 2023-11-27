import time
from base import BaseCase,  credentials
from ui.fixtures import registration_main_page, registration_page, get_driver
import pytest


class TestRegistration(BaseCase):
    authorize = False

    @pytest.mark.skip()
    def test_go_to_creation(self, registration_main_page, credentials):
        registration_main_page.go_to_account_creation(*credentials)

    def test_dummy(self, registration_page):
        registration_page.go()
        registration_page.check_url(registration_page.url)
