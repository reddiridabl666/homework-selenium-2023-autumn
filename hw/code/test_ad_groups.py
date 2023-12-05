import time
from base import BaseCase
from ui.fixtures import ad_groups_page, ad_group_creation_page, credentials
import pytest


class TestAudience(BaseCase):
    @pytest.mark.parametrize('regions', (('Россия', 'Европа'),))
    def test_select_regions(self, ad_group_creation_page, regions):
        ad_group_creation_page.select_regions(regions)

        time.sleep(2)
        assert ad_group_creation_page.selected_regions() == regions

    def test_clear_regions_selection(self, ad_group_creation_page):
        regions = ('Россия', 'Европа')

        ad_group_creation_page.select_regions(regions)
        assert ad_group_creation_page.selected_regions() == regions

        ad_group_creation_page.clear_region_selection()
        assert ad_group_creation_page.selected_regions() == []

    def test_search_regions(self, ad_group_creation_page):
        ad_group_creation_page.search_regions('роСс')
        shown = ad_group_creation_page.shown_regions()

        assert 'Россия' in shown
        assert 'Новороссийск' in shown

    def test_remove_region_from_selection(self, ad_group_creation_page):
        regions = ('Россия', 'Европа')

        ad_group_creation_page.select_regions(regions)
        assert ad_group_creation_page.selected_regions() == regions

        ad_group_creation_page.remove_region_from_selection('Европа')
        assert ad_group_creation_page.selected_regions() == ['Россия']
