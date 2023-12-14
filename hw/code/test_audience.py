from base import BaseCase
from ui.fixtures import audience_page, credentials
from ui.pages.audience_page import keywords_payload
import pytest


@pytest.fixture
def keyword_audience(audience_page):
    audience_page.create_audience(
        TestAudience.keywords_name, data=keywords_payload())
    audience_page.creation_modal_closed()
    yield
    audience_page.driver.get(audience_page.url)
    audience_page.delete_audience(TestAudience.keywords_name)


@pytest.fixture()
def audience_based_on_other(audience_page):
    audience_page.create_audience(
        TestAudience.based_on_other_name, source=audience_page.OTHER_AUDIENCE, data=TestAudience.keywords_name)
    audience_page.creation_modal_closed()
    yield
    audience_page.driver.get(audience_page.url)
    audience_page.delete_audience(TestAudience.based_on_other_name)


class TestAudience(BaseCase):
    keywords_name = 'Аудитория с ключевыми словами'
    based_on_other_name = 'Аудитория на основе старой'

    RULE_AND = 'и'
    RULE_OR = 'или'

    def test_long_audience_name(self, audience_page):
        audience_page.set_audience_name('a'*256)
        audience_page.has_long_name_error()

    def test_create_keywords(self, audience_page):
        data = keywords_payload()
        audience_page.set_audience_name(self.keywords_name)
        audience_page.add_source(audience_page.KEYWORDS, data)
        assert audience_page.get_source(0) == data

    @pytest.mark.parametrize('days', ['31'])
    def test_create_keywords_invalid_days(self, audience_page, days):
        data = keywords_payload(days=days)
        audience_page.set_audience_name(self.keywords_name)
        audience_page.add_source(audience_page.KEYWORDS, data)
        assert audience_page.get_source(0)['days'] == '30'

    def test_edit_audience(self, audience_page):
        name = self.keywords_name
        audience_page.create_audience(name, data=keywords_payload())
        audience_page.open_edit_modal(name)
        audience_page.save_audience()
        audience_page.delete_audience(name)

    def test_boolean_rule(self, audience_page):
        audience_page.set_audience_name(self.keywords_name)

        first_source_name = 'Условие 1'
        second_source_name = 'Условие 1'

        audience_page.add_source(data=keywords_payload(name=first_source_name))
        audience_page.add_source(
            data=keywords_payload(name=second_source_name))

        audience_page.set_rule(self.RULE_AND)
        assert audience_page.get_rule() == self.RULE_AND

        audience_page.set_rule(self.RULE_OR)
        assert audience_page.get_rule() == self.RULE_OR

    def test_create_from_other(self, keyword_audience, audience_based_on_other):
        pass

    def test_filter_audience(self, keyword_audience, audience_based_on_other, audience_page):
        audience_page.filter_audiences(shown=[audience_page.KEYWORDS])
        assert audience_page.get_audience_names() == [self.keywords_name]

        audience_page.filter_audiences(
            shown=[audience_page.OTHER_AUDIENCE, audience_page.KEYWORDS])

        assert audience_page.get_audience_names(
        ) == [self.based_on_other_name, self.keywords_name]
