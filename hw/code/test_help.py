from base import BaseCase
from ui.fixtures import help_page
import pytest


class TestHelp(BaseCase):
    def test_authorize_redirect(self, help_page):
        help_page.click_authorize_link()
        assert help_page.is_url_open(
            "ads.vk.com/help/categories/authorization")

    def test_how_to_tune_redirect(self, help_page):
        help_page.click_how_to_tune_link()
        assert help_page.is_url_open("ads.vk.com/help/categories/general")

    def test_tools_redirect(self, help_page):
        help_page.click_tools_link()
        assert help_page.is_url_open("ads.vk.com/help/categories/features")

    def test_statistics_and_finance_redirect(self, help_page):
        help_page.click_statistics_and_finance_link()
        assert help_page.is_url_open("ads.vk.com/help/categories/statistics")

    def test_documents_redirect(self, help_page):
        help_page.click_documents_link()
        assert help_page.is_url_open("ads.vk.com/help/categories/documents")

    def test_simplified_redirect(self, help_page):
        help_page.click_simplified_link()
        assert help_page.is_url_open("ads.vk.com/help/categories/mini_ads")

    def test_faq_redirect(self, help_page):
        help_page.click_faq_link()
        assert help_page.is_url_open("ads.vk.com/help/categories/faq")

    def test_partner_cabinet_redirect(self, help_page):
        help_page.click_partner_cabinet_link()
        assert help_page.is_url_open("ads.vk.com/help/categories/partner")

    def test_search_clues(self, help_page):
        help_page.fill_search("создание")
        help_page.check_search_suggestions()

    def test_search_clues_disappear(self, help_page):
        help_page.fill_search("создание")
        help_page.check_search_suggestions()
        help_page.unfocus_search()
        help_page.check_search_suggestions_invisible()
