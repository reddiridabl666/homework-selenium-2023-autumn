from base import BaseCase
from ui.fixtures import main_page, cases_page
import pytest
from time import sleep


class TestCarousel(BaseCase):    
    def test_timeout_switch(self, main_page):
        start_value = main_page.get_carousel_active_img()
        sleep(7)
        assert(start_value != main_page.get_carousel_active_img)
        
    def test_click_switch(self, main_page):
        start_value = main_page.get_carousel_active_img()
        main_page.click_nonactive_tab()
        assert(start_value != main_page.get_carousel_active_img)

    
