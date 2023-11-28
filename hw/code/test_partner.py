from base import BaseCase,  credentials
from ui.fixtures import partner_page
import logging


class TestPartner(BaseCase):
    authorize = False

    def test_account_redirect(self, partner_page):
        partner_page.click_account()
        partner_page.switch_to_new_tab()
        partner_page.check_url("https://id.vk.com")

    def test_help_redirect(self, partner_page):
        partner_page.click_help()
        partner_page.switch_to_new_tab()
        partner_page.check_url('https://ads.vk.com/help')

    def test_site_tab(self, partner_page):
        formats = [
            "Баннер", "Instream", "Адаптивный блок", "InPage", "Полноэкранный блок", "Sticky-баннер"
        ]

        partner_page.click_mobile_tab()
