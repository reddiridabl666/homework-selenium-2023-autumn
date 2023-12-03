from base import BaseCase
from ui.fixtures import main_page, cases_page
import pytest

tabs = [
    ('Новости', 'https://ads.vk.com/news'),
    ('Кейсы', 'https://ads.vk.com/cases'),
    ('Форум идей', 'https://ads.vk.com/upvote'),
]

education_dropdown_redirects = [
    ('Полезные материалы', 'https://ads.vk.com/insights'),
    ('Мероприятия', 'https://ads.vk.com/events'),
]

education_dropdown_new_tabs = [
    ('Видеокурсы', 'https://expert.vk.com/catalog/courses/'),
    ('Сертификация', 'https://expert.vk.com/certification/'),
]


class TestNavbar(BaseCase):
    def test_logo_redirect(self, cases_page):
        cases_page.click_logo()

    def test_account_redirect(self, main_page):
        main_page.click_account()
        main_page.assert_url("https://id.vk.com")

    def test_help_redirect(self, main_page):
        main_page.click_help()
        main_page.assert_url('https://ads.vk.com/help')

    @pytest.mark.parametrize("tab,url", tabs)
    def test_tab_redirects(self, main_page, tab, url):
        main_page.click_tab(tab)
        main_page.assert_url(url)

    def test_monetization_redirect(self, main_page):
        main_page.click_tab('Монетизация')
        main_page.switch_to_new_tab()
        main_page.assert_url('https://ads.vk.com/partner')

    def test_education_dropdown_hover(self, main_page):
        main_page.open_education_dropdown()
        assert main_page.is_education_dropdown_visible()

    @pytest.mark.parametrize("element,url", education_dropdown_redirects)
    def test_education_dropdown_redirects(self, main_page, element, url):
        main_page.open_education_dropdown()
        main_page.click_tab(element)
        main_page.assert_url(url)

    @pytest.mark.parametrize("element,url", education_dropdown_new_tabs)
    def test_education_dropdown_redirects_new_page(self, main_page, element, url):
        main_page.open_education_dropdown()
        main_page.click_tab(element)
        main_page.switch_to_new_tab()
        main_page.assert_url(url)

    def test_mobile_ui(self, main_page):
        self.driver.set_window_size(1024, 1080)
        assert main_page.is_side_menu_hamburger_visible()
