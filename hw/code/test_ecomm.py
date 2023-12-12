from base import BaseCase
from ui.fixtures import ecomm_page
import pytest

class TestEcomm(BaseCase):
    @pytest.mark.skip()
    def test_create_catalog_modal_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()
        ecomm_page.check_catalog_btn_visible()

    @pytest.mark.skip()
    def test_create_catalog_modal_feed_opnes(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_feed_btn()
        ecomm_page.create_catalog_modal.check_feed()

    @pytest.mark.skip()
    def test_create_catalog_modal_marketplace_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_marketplace_btn()
        ecomm_page.create_catalog_modal.check_marketplace()

    @pytest.mark.skip()
    def test_create_catalog_modal_manual_opens(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_manual_btn()
        ecomm_page.create_catalog_modal.check_manual()

    @pytest.mark.skip()
    def test_manual_catalog_creation(self, ecomm_page):
        ecomm_page.click_create_catalog_btn()

        ecomm_page.create_catalog_modal.click_manual_btn()
        ecomm_page.create_catalog_modal.create_catalog_from_file()

        ecomm_page.create_catalog_modal.check_loading_started()
        ecomm_page.create_catalog_modal.check_loading_finished()

    def test_catalog_redirect(self, ecomm_page):
        ecomm_page.click_catalog()

        ecomm_page.check_url('https://ads.vk.com/hq/ecomm/catalogs/335256')