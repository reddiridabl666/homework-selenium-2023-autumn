from base import BaseCase,  credentials
from ui.fixtures import registration_main_page, registration_page
import pytest


class TestNavbar(BaseCase):
    authorize = False

    def test_go_to_creation(self, registration_main_page):
        registration_main_page.click_registration()
