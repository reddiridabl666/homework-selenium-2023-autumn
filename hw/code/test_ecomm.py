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
    PROMOTE_URL = "https://ads.vk.com/hq/new_create/ad_plan*"
    CATALOG_URL = "https://ads.vk.com/hq/ecomm/catalogs/[0-9]*"


    def test_create_catalog_modal_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()
        assert ecomm_page.is_catalog_btn_visible()

    def test_create_catalog_modal_feed_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_feed_btn()
        assert ecomm_page.create_catalog_modal.is_feed_visible()

    def test_create_catalog_modal_marketplace_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_marketplace_btn()
        assert ecomm_page.create_catalog_modal.is_marketplace_visible()

    def test_create_catalog_modal_manual_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_manual_btn()
        assert ecomm_page.create_catalog_modal.is_manual_visible()

    def test_manual_catalog_creation(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_manual_btn()
        ecomm_page.create_catalog_modal.create_catalog_from_file()

        assert ecomm_page.create_catalog_modal.has_loading_started()
        assert ecomm_page.create_catalog_modal.has_loading_finished()

    def test_catalog_redirect(self, ecomm_page):
        ecomm_page.click_catalog()
        assert self.is_url_open(self.CATALOG_URL)

    def test_catalog_settings(self, ecomm_page):
        ecomm_page.click_catalog()
        ecomm_page.open_catalog_options()
        assert ecomm_page.is_catalog_options_modal_open()

    @pytest.mark.parametrize("tab,url", tabs)
    def test_catalog_redirects(self, ecomm_page, tab, url):
        ecomm_page.click_catalog()

        if (tab != tabs[0][0]):
            ecomm_page.click_tab(tab)
        
        assert self.is_url_open(
            f"https://ads.vk.com/hq/ecomm/catalogs/[0-9]*{url}")

    def test_add_goods_modal(self, ecomm_page):
        ecomm_page.click_catalog()
        ecomm_page.click_add_goods_btn()
        assert ecomm_page.is_catalog_options_modal_open()

    def test_promote_redirect(self, ecomm_page):
        ecomm_page.click_catalog()
        ecomm_page.click_promote_btn()
        assert self.is_url_open(self.PROMOTE_URL)
