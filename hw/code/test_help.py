from base import BaseCase
from ui.pages.help_page import HelpPage
from ui.fixtures import help_page
import pytest


class TestHelp(BaseCase):
    SEARCH_QUERY = "создание"


    def test_authorize_redirect(self, help_page: HelpPage):
        help_page.click_authorize_link()
        assert self.is_url_open(
            "ads.vk.com/help/categories/authorization")

    def test_how_to_tune_redirect(self, help_page: HelpPage):
        help_page.click_how_to_tune_link()
        assert self.is_url_open("ads.vk.com/help/categories/general")

    def test_tools_redirect(self, help_page: HelpPage):
        help_page.click_tools_link()
        assert self.is_url_open("ads.vk.com/help/categories/features")

    def test_statistics_and_finance_redirect(self, help_page: HelpPage):
        help_page.click_statistics_and_finance_link()
        assert self.is_url_open("ads.vk.com/help/categories/statistics")

    def test_documents_redirect(self, help_page: HelpPage):
        help_page.click_documents_link()
        assert self.is_url_open("ads.vk.com/help/categories/documents")

    def test_simplified_redirect(self, help_page: HelpPage):
        help_page.click_simplified_link()
        assert self.is_url_open("ads.vk.com/help/categories/mini_ads")

    def test_faq_redirect(self, help_page: HelpPage):
        help_page.click_faq_link()
        assert self.is_url_open("ads.vk.com/help/categories/faq")

    def test_partner_cabinet_redirect(self, help_page: HelpPage):
        help_page.click_partner_cabinet_link()
        assert self.is_url_open("ads.vk.com/help/categories/partner")

    def test_search_clues(self, help_page: HelpPage):
        help_page.fill_search(self.SEARCH_QUERY)
        clues = help_page.get_search_suggestions()

        assert clues is not None
        assert clues.is_displayed()

    def test_search_clues_disappear(self, help_page: HelpPage):
        help_page.fill_search(self.SEARCH_QUERY)

        help_page.get_search_suggestions()
        help_page.unfocus_search()
        help_page.wait_until_search_suggestion_disappear()

        clues = help_page.get_search_suggestions(timeout=1)
        assert clues is None
