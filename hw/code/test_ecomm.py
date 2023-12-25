from base import BaseCase
from ui.fixtures import ecomm_page
import pytest

tabs = [
    ("Товары", ""),
    ("Группы", "/groups"),
    ("Диагностика", "/diagnostics"),
    ("События", "/event"),
    ("История загрузок", "/history"),
]


class TestEcomm(BaseCase):
    def test_create_catalog_modal_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()
        ecomm_page.check_catalog_btn_visible()

    def test_create_catalog_modal_feed_opnes(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_feed_btn()
        ecomm_page.create_catalog_modal.check_feed()

    def test_create_catalog_modal_marketplace_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_marketplace_btn()
        ecomm_page.create_catalog_modal.check_marketplace()

    def test_create_catalog_modal_manual_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_manual_btn()
        ecomm_page.create_catalog_modal.check_manual()

    def test_manual_catalog_creation(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_manual_btn()
        ecomm_page.create_catalog_modal.create_catalog_from_file()

        ecomm_page.create_catalog_modal.check_loading_started()
        ecomm_page.create_catalog_modal.check_loading_finished()

    def test_catalog_redirect(self, ecomm_page):
        ecomm_page.click_catalog()
        assert self.is_url_open("https://ads.vk.com/hq/ecomm/catalogs/[0-9]*")

    def test_catalog_settings(self, ecomm_page):
        ecomm_page.click_catalog()
        ecomm_page.open_catalog_options()
        ecomm_page.check_catalog_options_modal()

    @pytest.mark.parametrize("tab,url", tabs)
    def test_catalog_redirects(self, ecomm_page, tab, url):
        ecomm_page.click_catalog()
        ecomm_page.click_tab(tab)
        assert self.is_url_open(
            f"https://ads.vk.com/hq/ecomm/catalogs/[0-9]*{url}")

    def test_add_goods_modal(self, ecomm_page):
        ecomm_page.click_catalog()
        ecomm_page.click_add_goods_btn()
        ecomm_page.check_catalog_options_modal()

    def test_promote_redirect(self, ecomm_page):
        ecomm_page.click_catalog()
        ecomm_page.click_promote_btn()
        assert self.is_url_open(
            "https://ads.vk.com/hq/new_create/ad_plan*")
