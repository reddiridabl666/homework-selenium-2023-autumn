import time
from base import BaseCase
from ui.fixtures import ad_groups_page, ad_group_creation_page, credentials
import pytest


class TestAdGroups(BaseCase):
    @pytest.mark.parametrize('region', ('Россия',))
    def test_select_region(self, ad_group_creation_page, region):
        ad_group_creation_page.search_regions(region)

        ad_group_creation_page.select_region(region)
        assert ad_group_creation_page.selected_regions() == [region]

    def test_clear_regions_selection(self, ad_group_creation_page):
        regions = ['Россия', 'Европа']
        for region in regions:
            ad_group_creation_page.search_regions(region)
            ad_group_creation_page.select_region(region)

        assert ad_group_creation_page.selected_regions() == regions

        ad_group_creation_page.clear_region_selection()
        assert ad_group_creation_page.selected_regions() == []

    def test_search_regions(self, ad_group_creation_page):
        ad_group_creation_page.search_regions('роСс')
        shown = ad_group_creation_page.shown_regions()

        assert 'Россия' in shown
        assert any('Новороссийск' in elem for elem in shown)

    def test_remove_region_from_selection(self, ad_group_creation_page):
        regions = ['Россия', 'Европа']
        for region in regions:
            ad_group_creation_page.search_regions(region)
            ad_group_creation_page.select_region(region)

        assert ad_group_creation_page.selected_regions() == regions

        ad_group_creation_page.remove_region_from_selection('Европа')
        assert ad_group_creation_page.selected_regions() == ['Россия']

    def test_add_regions_by_list(self, ad_group_creation_page):
        regions = ['Россия', 'Москва', '468']
        ad_group_creation_page.add_by_list(regions)

        assert ad_group_creation_page.add_by_list_status() == 'Добавлены 3 региона'
        ad_group_creation_page.close_list_add_modal()

        selected_regions = ad_group_creation_page.selected_regions()

        assert 'Москва' in selected_regions
        assert 'Республика Крым' in selected_regions
        assert 'Россия' in selected_regions

    def test_must_choose_at_least_one_device(self, ad_group_creation_page):
        ad_group_creation_page.toggle_devices_section()

        ad_group_creation_page.toggle_device_mobile()
        assert ad_group_creation_page.is_device_desktop_disabled()

        ad_group_creation_page.toggle_device_mobile()
        ad_group_creation_page.toggle_device_desktop()
        assert ad_group_creation_page.is_device_mobile_disabled()

    def test_placements_shown_when_auto_disabled(self, ad_group_creation_page):
        ad_group_creation_page.show_placement_options()
        placement_options = ad_group_creation_page.get_placement_options()

        assert 'ВКонтакте' in placement_options
        assert 'Одноклассники' in placement_options
        assert 'Проекты VK' in placement_options
        assert 'Рекламная сеть' in placement_options
