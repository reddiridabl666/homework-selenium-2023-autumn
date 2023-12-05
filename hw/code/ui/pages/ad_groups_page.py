import time
from ui.pages.hq_page import HqPage
from ui.pages.base_page import BasePage
from ui.locators import basic_locators


class AdGroupCreationPage(BasePage):
    url = 'https://ads.vk.com/hq/new_create/ad_plan'
    locators = basic_locators.AdGroupCreationPageLocators

    def select_regions(self, regions):
        if len(self.selected_regions()) > 0:
            self.clear_region_selection()

        for region in regions:
            self.click(self.locators.REGION_SEARCH_ITEM(region))

    def selected_regions(self):
        try:
            return [elem.text for elem in self.find_multiple(self.locators.REGION_LIST_ITEMS, timeout=0.5)]
        except:
            return []

    def shown_regions(self):
        try:
            return [elem.text for elem in self.find_multiple(self.locators.REGION_SEARCH_ITEMS, timeout=0.5)]
        except:
            return []

    def clear_region_selection(self):
        self.click(self.locators.CLEAR_REGION_LIST)

    def remove_region_from_selection(self, region):
        self.click(self.locators.REGION_LIST_REMOVE_ITEM(region))

    def search_regions(self, query):
        self.fill_in(self.locators.REGION_SEARCH, query)


class AdGroupsPage(HqPage):
    url = 'https://ads.vk.com/hq/ad_groups'
    locators = basic_locators.AdGroupsPageLocators

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

        return AdGroupCreationPage(self.driver)
