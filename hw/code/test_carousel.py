from base import BaseCase
from ui.fixtures import main_page, cases_page
import pytest
from time import sleep


class TestCarousel(BaseCase):    
    def test_timeout_switch(self, main_page):
        first_bullet = main_page.get_bullets()[0]

        assert main_page.ACTIVE_BULLET_CLASS in first_bullet.get_attribute("class")

        main_page.wait_until_bullet_becomes_inactive(0)

        first_bullet = main_page.get_bullets()[0]
        second_bullet = main_page.get_bullets()[1]

        assert main_page.ACTIVE_BULLET_CLASS not in first_bullet.get_attribute("class")
        assert main_page.ACTIVE_BULLET_CLASS in second_bullet.get_attribute("class")

        
    def test_click_switch(self, main_page):
        start_value = main_page.get_carousel_active_img()
        main_page.click_nonactive_tab()
        assert(start_value != main_page.get_carousel_active_img)

    
