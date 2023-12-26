import pytest
from base import BaseCase
from ui.pages.main_page import MainPage

tabs = [
    ('Новости', 'https://ads.vk.com/news', False),
    ('Полезные материалы', 'https://ads.vk.com/insights', False),
    ('Мероприятия', 'https://ads.vk.com/events', False),
    ('Документы', 'https://ads.vk.com/documents', False),
    ('Обучение для бизнеса', 'https://expert.vk.com/', True),
    ('Кейсы', 'https://ads.vk.com/cases', False),
    ('Помощь', 'https://ads.vk.com/help', False),
    ('Монетизация', 'https://ads.vk.com/partner', True),
]

groups = [("https://vk.com/vk_ads"), ("https://ok.ru/group/64279825940712"), ("https://t.me/vk_ads")]


class TestFooter(BaseCase):
    @pytest.mark.parametrize("tab,url,need_switch_tab", tabs)
    def test_footer_tab_redirects(self, main_page: MainPage, tab: str, url: str, need_switch_tab: bool):
        main_page.click_footer_tab(tab)
        if need_switch_tab:
            main_page.switch_to_new_tab()
        assert self.is_url_open(url)

    def test_footer_account_redirect(self, main_page: MainPage):
        main_page.click_footer_account()
        assert self.is_url_open("https://id.vk.com")

    def test_footer_business_redirect(self, main_page: MainPage):
        main_page.click_footer_business()
        main_page.switch_to_new_tab()
        assert self.is_url_open("https://vk.company/ru/company/business")

    @pytest.mark.parametrize("url", groups)
    def test_footer_group_redirect(self, main_page: MainPage, url: str):
        main_page.click_footer_group(url)
        main_page.switch_to_new_tab()
        assert self.is_url_open(url)

    def test_footer_language(self, main_page: MainPage):
        assert main_page.get_footer_language() == main_page.LANG_RU

        main_page.select_language(main_page.LANG_SELECT_EN)
        assert main_page.get_footer_language() == main_page.LANG_EN

        main_page.select_language(main_page.LANG_SELECT_RU)
        assert main_page.get_footer_language() == main_page.LANG_RU

    def test_footer_about(self, main_page: MainPage):
        main_page.click_footer_about()
        main_page.switch_to_new_tab()
        assert self.is_url_open("https://vk.company")
