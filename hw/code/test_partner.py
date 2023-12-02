from base import BaseCase,  credentials
from ui.fixtures import partner_page
import pytest


class TestPartner(BaseCase):
    authorize = False

    @pytest.mark.skip()
    def test_account_redirect(self, partner_page):
        partner_page.click_account()
        partner_page.switch_to_new_tab()
        partner_page.check_url("https://id.vk.com")

    @pytest.mark.skip()
    def test_help_redirect(self, partner_page):
        partner_page.click_help()
        partner_page.switch_to_new_tab()
        partner_page.check_url('https://ads.vk.com/help')

    @pytest.mark.skip() 
    def test_mobile_tab(self, partner_page):
        formats = [
            "Баннер", "Нативный формат", "Полноэкранный блок", "Видео за вознаграждение"
        ]

        partner_page.click_mobile_tab()

        for format in formats:
            assert partner_page.check_format_presence(format)

    @pytest.mark.skip() 
    def test_site_tab(self, partner_page):
        formats = [
             "Баннер", "Instream", "Адаптивный блок", "InPage", "Полноэкранный блок", "Sticky-баннер"
        ]

        partner_page.click_mobile_tab()
        partner_page.click_site_tab()

        for format in formats:
            assert partner_page.check_format_presence(format)

    def test_submit_btn_disabled_by_default(self, partner_page):
        assert not partner_page.form_submit_btn_enabled()

    def test_submit_btn_enabled_when_form_filled(self, partner_page):
        partner_page.fill_form()

        assert partner_page.form_submit_btn_enabled()

