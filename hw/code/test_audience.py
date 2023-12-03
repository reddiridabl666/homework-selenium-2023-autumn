from base import BaseCase
from ui.fixtures import audience_page, credentials
from ui.pages.audience_page import keywords_payload
import pytest


class TestAudience(BaseCase):
    def test_long_audience_name(self, audience_page):
        audience_page.set_audience_name('a'*256)
        audience_page.has_long_name_error()

    def test_create_keywords(self, audience_page):
        data = keywords_payload()
        audience_page.set_audience_name('Аудитория с ключевыми словами')
        audience_page.add_source('Ключевые фразы', data)
        assert audience_page.get_source(0) == data

    @pytest.mark.parametrize('days', ['31'])
    def test_create_keywords_invalid_days(self, audience_page, days):
        data = keywords_payload(days=days)
        audience_page.set_audience_name('Аудитория с ключевыми словами')
        audience_page.add_source('Ключевые фразы', data)
        assert audience_page.get_source(0)['days'] == '30'
