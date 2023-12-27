from base import BaseCase
from ui.fixtures import sites_page
import pytest


class TestSites(BaseCase):
    SITE_URL = "wild-spirits.test"

    def test_add_pixel_modal(self, sites_page):
        sites_page.open_add_pixel_modal()
        
        modal = sites_page.get_pixel_modal()
        assert modal.is_displayed()

        sites_page.close_add_pixel_modal()
        sites_page.wait_for_pixel_modal_close()

        modal = sites_page.get_pixel_modal(timeout=1)
        assert modal is None

    def test_add_pixel_modal_submit_btn(self, sites_page):
        sites_page.open_add_pixel_modal()

        submit_btn = sites_page.get_submit_btn()
        assert not submit_btn.is_enabled()

        sites_page.fill_domain_input(self.SITE_URL)

        submit_btn = sites_page.get_submit_btn()
        assert submit_btn.is_enabled()

        sites_page.click_submit_btn()

        modal = sites_page.get_pixel_created_modal()
        assert modal.is_displayed()
