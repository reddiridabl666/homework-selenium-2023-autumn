import time
from base import BaseCase
from ui.pages.ad_groups_page import AdGroupCreationPage
from ui.fixtures import ad_groups_page, ad_group_creation_page, credentials
from test_audience import keyword_audience
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

    def test_min_age_less_than_max(self, ad_group_creation_page):
        ad_group_creation_page.toggle_demography_section()
        ad_group_creation_page.select_max_age(70)

        assert all(
            elem <= 70 for elem in ad_group_creation_page.available_min_age())

    def test_max_age_greater_than_min(self, ad_group_creation_page):
        ad_group_creation_page.toggle_demography_section()
        ad_group_creation_page.select_min_age(14)

        assert all(
            elem >= 14 for elem in ad_group_creation_page.available_max_age())

    def test_audience_negative_search_toggle(self, ad_group_creation_page):
        ad_group_creation_page.toggle_audience_section()

        ad_group_creation_page.show_negative_audience_search()
        ad_group_creation_page.is_negative_audience_search_shown()

        ad_group_creation_page.hide_negative_audience_search()
        ad_group_creation_page.is_negative_audience_toggle_shown()

    def test_select_audience(self, keyword_audience, ad_group_creation_page):
        ad_group_creation_page.toggle_audience_section()

        audiences = ad_group_creation_page.suggested_audiences()
        ad_group_creation_page.select_audience(audiences[0])

        assert ad_group_creation_page.selected_audiences() == [audiences[0]]

    @pytest.mark.skip
    def test_deselect_audience(self, keyword_audience, ad_group_creation_page):
        ad_group_creation_page.toggle_audience_section()

        audiences = ad_group_creation_page.suggested_audiences()
        ad_group_creation_page.select_audience(audiences[0])
        assert ad_group_creation_page.selected_audiences() == [audiences[0]]

        ad_group_creation_page.deselect_audience(audiences[0])
        assert ad_group_creation_page.no_selected_audiences()

    def test_edit_ad_group(self, ad_group_drafts_page):
        ids = ad_group_drafts_page.shown_ad_group_ids()
        ad_group_drafts_page.edit_ad_group_draft(ids[0])
        ad_group_drafts_page.check_url(AdGroupCreationPage.url)

    def test_select_ad_group(self, ad_group_drafts_page):
        ids = ad_group_drafts_page.shown_ad_group_ids()
        ad_group_drafts_page.select_ad_group_draft(ids[0])

        assert ad_group_drafts_page.selected_ad_group_ids() == [ids[0]]
        assert ad_group_drafts_page.additional_controls_present()

    def test_deselect_ad_groups(self, ad_group_drafts_page):
        ids = ad_group_drafts_page.shown_ad_group_ids()
        ad_group_drafts_page.select_ad_group_draft(ids[0])

        ad_group_drafts_page.deselect_all_drafts()

        assert ad_group_drafts_page.no_selected_ad_groups()
        assert ad_group_drafts_page.additional_controls_not_present()

    def test_delete_ad_group(self, ad_group_drafts_page):
        ids = ad_group_drafts_page.shown_ad_group_ids()
        ad_group_drafts_page.delete_ad_group_draft(ids[0])
        assert ad_group_drafts_page.no_shown_ad_groups()

    def test_close_deletion_modal_cancel(self, ad_group_drafts_page):
        ids = ad_group_drafts_page.shown_ad_group_ids()

        ad_group_drafts_page.open_deletion_modal(ids[0])
        ad_group_drafts_page.close_deletion_modal_cancel()

        assert ad_group_drafts_page.is_deletion_modal_closed()

    def test_close_deletion_modal_cross(self, ad_group_drafts_page):
        ids = ad_group_drafts_page.shown_ad_group_ids()

        ad_group_drafts_page.open_deletion_modal(ids[0])
        ad_group_drafts_page.close_deletion_modal_cross()

        assert ad_group_drafts_page.is_deletion_modal_closed()

    def test_close_deletion_modal_click_outside(self, ad_group_drafts_page):
        ids = ad_group_drafts_page.shown_ad_group_ids()

        ad_group_drafts_page.open_deletion_modal(ids[0])
        ad_group_drafts_page.close_deletion_modal_click_outside()

        assert ad_group_drafts_page.is_deletion_modal_closed()
