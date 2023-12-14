from base import BaseCase
from ui.fixtures import main_page, cases_page
import pytest
from time import sleep

class TestCases(BaseCase):
    
    def test_click_redirect(self, cases_page):
        
        cases_page.get_case_card().click()
        cases_page.assert_url("https://ads.vk.com/cases/")
