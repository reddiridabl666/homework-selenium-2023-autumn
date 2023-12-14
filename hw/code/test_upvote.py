import pytest
from base import BaseCase
from ui.pages.upvote_page import UpvotePage

idea_themes = [("Сайты", 1), ("Сообщества", 4)]

idea_statuses = [("Уже в работе", 2), ("Реализована", 1)]

idea_card = [("Создать Библиотеку Рекламы", 48), ("Получить ссылку на созданную лид-форму", 9)]


class TestUpvote(BaseCase):
    def test_upvote_search_by_title(self, upvote_page: UpvotePage):
        upvote_page.fill_search("Получить")
        upvote_page.wait_for_count_of_ideas(1)

    def test_upvote_search_by_id(self, upvote_page: UpvotePage):
        upvote_page.fill_search("10")
        upvote_page.wait_for_count_of_ideas(1)

    @pytest.mark.parametrize("theme_name,ideas_count", idea_themes)
    def test_upvote_select_theme(self, upvote_page: UpvotePage, theme_name: str, ideas_count: int):
        upvote_page.select_idea_theme(theme_name)
        upvote_page.wait_for_count_of_ideas(ideas_count)

    @pytest.mark.parametrize("status_name,ideas_count", idea_statuses)
    def test_upvote_select_status(self, upvote_page: UpvotePage, status_name: str, ideas_count: int):
        upvote_page.select_idea_status(status_name)
        upvote_page.wait_for_count_of_ideas(ideas_count)

    @pytest.mark.parametrize("title,id", idea_card)
    def test_upvote_go_to_page(self, upvote_page: UpvotePage, title: str, id: int):
        upvote_page.go_to_idea(title)
        upvote_page.assert_url(f"https://ads.vk.com/upvote/{id}")
        assert upvote_page.get_idea_title() == title
