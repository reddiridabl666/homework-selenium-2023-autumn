import time
from ui.pages.hq_page import HqPage
from ui.pages.base_page import BasePage
from ui.locators import basic_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AdGroupCreationPage(BasePage):
    url = 'https://ads.vk.com/hq/new_create/ad_plan'
    locators = basic_locators.AdGroupCreationPageLocators

    def select_regions(self, regions):
        if len(self.selected_regions()) > 0:
            self.clear_region_selection()

        for region in regions:
            self.select_region(region)

    def select_region(self, region):
        self.click_may_be_stale(self.locators.REGION_SEARCH_ITEM(region))

    def selected_regions(self):
        try:
            return [elem.text for elem in self.find_multiple(self.locators.REGION_LIST_ITEMS, timeout=1)]
        except:
            return []

    def shown_regions(self):
        try:
            return [elem.text for elem in self.find_multiple(self.locators.REGION_SEARCH_ITEMS, timeout=1)]
        except:
            return []

    def clear_region_selection(self):
        self.click(self.locators.CLEAR_REGION_LIST)

    def remove_region_from_selection(self, region):
        self.click(self.locators.REGION_LIST_REMOVE_ITEM(region))

    def search_regions(self, query):
        self.fill_in(self.locators.REGION_SEARCH, query)

    def add_by_list(self, regions):
        self.click(self.locators.ADD_REGIONS_BY_LIST)
        self.fill_in(self.locators.REGION_LIST_INPUT, ','.join(regions))
        self.click(self.locators.SUBMIT_REGIONS_BY_LIST)

    def add_by_list_status(self):
        return self.find(self.locators.REGION_LIST_ADD_STATUS).text

    def close_list_add_modal(self):
        self.click(self.locators.REGION_LIST_ADD_CLOSE_MODAL)

    def toggle_devices_section(self):
        self.find(self.locators.DEVICES).location_once_scrolled_into_view
        self.click(self.locators.DEVICES)

    def toggle_device_mobile(self):
        self.click(self.locators.DEVICES_MOBILE)

    def toggle_device_desktop(self):
        self.click(self.locators.DEVICES_DESKTOP)

    def is_device_mobile_disabled(self):
        return self.is_disabled(self.locators.DEVICES_MOBILE)

    def is_device_desktop_disabled(self):
        return self.is_disabled(self.locators.DEVICES_DESKTOP)

    def show_placement_options(self):
        self.find(self.locators.PLACEMENT).location_once_scrolled_into_view
        self.click(self.locators.PLACEMENT)
        self.click(self.locators.PLACEMENT_AUTO_CHOICE_TOGGLE)

    def get_placement_options(self):
        return [elem.text for elem in self.find_multiple(self.locators.PLACEMENT_CHOICE_ITEM)]

    def toggle_demography_section(self):
        self.find(self.locators.DEMOGRAPHY).location_once_scrolled_into_view
        self.click(self.locators.DEMOGRAPHY)

    def select_min_age(self, age):
        self.click(self.locators.MIN_AGE_SELECT)
        self.click(self.locators.VK_UI_SELECT_ELEM(age))

    def select_max_age(self, age):
        self.click(self.locators.MAX_AGE_SELECT)
        self.click(self.locators.VK_UI_SELECT_ELEM(age))

    def available_min_age(self):
        self.click(self.locators.MIN_AGE_SELECT)
        return [int(elem.text) for elem in self.find_multiple(self.locators.VK_UI_SELECT_ELEMS, cond=EC.presence_of_all_elements_located)]

    def available_max_age(self):
        self.click(self.locators.MAX_AGE_SELECT)
        return [int(elem.text) for elem in self.find_multiple(self.locators.VK_UI_SELECT_ELEMS, cond=EC.presence_of_all_elements_located)]

    def toggle_audience_section(self):
        self.find(self.locators.AUDIENCE).location_once_scrolled_into_view
        self.click(self.locators.AUDIENCE)

    def suggested_audiences(self):
        self.click(self.locators.AUDIENCE_SEARCH_VISIBLE)
        return [elem.text for elem in self.find_multiple(self.locators.VK_UI_SELECT_ELEMS)]

    def selected_audiences(self):
        return [elem.text for elem in self.find_multiple(self.locators.SELECTED_AUDIENCES)]

    def edit_audience(self, audience_name):
        self.click(self.locators.AUDIENCE_SEARCH_VISIBLE)
        self.click(self.locators.EDIT_AUDIENCE(audience_name))

    def select_audience(self, audience_name):
        self.click(self.locators.AUDIENCE_SEARCH_VISIBLE)
        self.click(self.locators.VK_UI_SELECT_ELEM(audience_name))

    def show_negative_audience_search(self):
        self.click(self.locators.AUDIENCE_NEG_SHOW)

    def hide_negative_audience_search(self):
        self.click(self.locators.AUDIENCE_NEG_CLOSE)

    def is_negative_audience_search_shown(self):
        return self.is_visible(self.locators.AUDIENCE_NEG_SEARCH_VISIBLE)

    def is_negative_audience_toggle_shown(self):
        return self.is_visible(self.locators.AUDIENCE_NEG_SHOW)


class AdGroupsPage(HqPage):
    url = 'https://ads.vk.com/hq/dashboard/ad_groups'
    ad_plan_drafts_url = 'https://ads.vk.com/hq/dashboard/ad_plans?mode=drafts'

    locators = basic_locators.AdGroupsPageLocators

    def go_to_drafts(self):
        self.driver.get(self.ad_group_drafts_url)

    def go_to_creation(self) -> AdGroupCreationPage:
        self.close_help()

        self.click(self.locators.CREATE)
        self.click(self.locators.SITE_CONVERSIONS)

        site_name = self.fill_in(self.locators.SITE_NAME, 'example.org')
        self.press_enter(site_name)

        self.fill_in(self.locators.TARGET_PRICE, '100')

        self.click(self.locators.NEXT)

        try:
            self.wait_for_redirect(timeout=0.1)
        except:
            self.is_not_visible(self.locators.ERROR_TOOLTIP)
            self.click(self.locators.NEXT)

        self.wait().until(EC.text_to_be_present_in_element(
            self.locators.DRAFT_STATUS, 'Изменения сохранены'))

        return AdGroupCreationPage(self.driver)

    def clear_drafts(self):
        self.driver.get(self.ad_plan_drafts_url)
        self.click(self.locators.SELECT_ALL)
        self.click(self.locators.DELETE)
        self.click(self.locators.CONFIRM_DELETE)
        self.is_not_visible(self.locators.DELETION_MODAL)


class AdGroupDraftsPage(AdGroupsPage):
    url = 'https://ads.vk.com/hq/dashboard/ad_groups?mode=drafts'
    locators = basic_locators.AdGroupDraftsPageLocators

    def edit_ad_group_draft(self, ad_group_id):
        self.hover(self.locators.DRAFT_ENTRY(ad_group_id))
        self.click(self.locators.EDIT_DRAFT(ad_group_id))

    def remove_table_field(self, field):
        pass

    def shown_table_fields(self):
        pass

    def select_ad_group_draft(self, ad_group_id):
        self.click(self.locators.SELECT_DRAFT(ad_group_id))

    def deselect_all_drafts(self):
        self.click(self.locators.DESELECT_DRAFTS)

    def open_deletion_modal(self, ad_group_id):
        self.select_ad_group_draft(ad_group_id)
        self.click(self.locators.DELETE)

    def close_deletion_modal_cancel(self):
        self.click(self.locators.CANCEL_DELETION)

    def close_deletion_modal_cross(self):
        self.click(self.locators.CLOSE_DELETION_MODAL)

    def close_deletion_modal_click_outside(self):
        actions = ActionChains(self.driver)
        actions.move_by_offset(0, 0)
        actions.click()
        actions.perform()

    def delete_ad_group_draft(self, ad_group_id):
        self.open_deletion_modal(ad_group_id)
        self.click(self.locators.CONFIRM_DELETE)

    def get_ids(self, elems):
        return [int(elem.get_attribute('data-entityid').removesuffix('-AdGroupDraft')) for elem in elems]

    def shown_ad_group_ids(self, timeout=None):
        return self.get_ids(self.find_multiple(self.locators.DRAFT_ENTRIES, timeout))

    def selected_ad_group_ids(self, timeout=None):
        return self.get_ids(self.find_multiple(self.locators.SELECTED_DRAFTS, timeout))

    def additional_controls_present(self):
        return self.is_visible(self.locators.DELETE) and self.is_visible(self.locators.CHOSEN_DRAFT_NUM)

    def additional_controls_not_present(self):
        return self.is_not_visible(self.locators.DELETE) and self.is_not_visible(self.locators.CHOSEN_DRAFT_NUM)

    def no_selected_ad_groups(self):
        try:
            self.selected_ad_group_ids(0.1)
            return False
        except:
            return True

    def no_shown_ad_groups(self):
        return self.is_not_visible(self.locators.DRAFT_ENTRIES)

    def is_deletion_modal_closed(self):
        return self.is_not_visible(self.locators.DELETION_MODAL)
