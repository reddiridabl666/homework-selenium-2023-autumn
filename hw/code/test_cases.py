from base import BaseCase
from ui.fixtures import main_page, cases_page


class TestCases(BaseCase):

    def test_click_redirect(self, cases_page):
        cases_page.get_case_card().click()
        assert self.is_url_open("https://ads.vk.com/cases/")
