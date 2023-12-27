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
        btn = ecomm_page.get_catalog_btn()
        assert btn.is_displayed()

    def test_create_catalog_modal_feed_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_feed_btn()
        feed = ecomm_page.create_catalog_modal.get_feed()
        assert feed.is_displayed()

    def test_create_catalog_modal_marketplace_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_marketplace_btn()
        marketplace = ecomm_page.create_catalog_modal.get_marketplace()

        assert marketplace.is_displayed()

    def test_create_catalog_modal_manual_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_manual_btn()

        manual = ecomm_page.create_catalog_modal.get_manual()
        assert manual.is_displayed()

    def test_manual_catalog_creation(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_manual_btn()
        ecomm_page.create_catalog_modal.create_catalog_from_file()

        loading = ecomm_page.create_catalog_modal.get_loading_animation()
        assert loading.is_displayed()

        ecomm_page.create_catalog_modal.wait_for_loading_end()
        loading = ecomm_page.create_catalog_modal.get_loading_animation()
        assert loading is None

    def test_catalog_redirect(self, ecomm_page):
        ecomm_page.click_catalog()
        assert self.is_url_open(self.CATALOG_URL)

    def test_catalog_settings(self, ecomm_page):
        ecomm_page.click_catalog()
        ecomm_page.open_catalog_options()
        catalog_options_modal = ecomm_page.get_catalog_options_modal()
        assert catalog_options_modal.is_displayed()

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
        catalog_options_modal = ecomm_page.get_catalog_options_modal()
        assert catalog_options_modal.is_displayed()

    def test_promote_redirect(self, ecomm_page):
        ecomm_page.click_catalog()
        ecomm_page.click_promote_btn()
        assert self.is_url_open(self.PROMOTE_URL)
