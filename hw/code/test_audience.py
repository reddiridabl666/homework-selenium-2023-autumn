from base import BaseCase
from ui.fixtures import audience_page, credentials
import pytest


class TestAudience(BaseCase):
    def test_long_audience_name(self, audience_page):
        audience_page.create_audience()
