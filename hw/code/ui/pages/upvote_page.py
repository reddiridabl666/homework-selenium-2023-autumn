from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class UpvotePage(BasePage):
    url = 'https://ads.vk.com/upvote'
    locators = basic_locators.UpvotePageLocators()

    def fill_search(self, text: str):
        self.fill_in(self.locators.SEARCH_FIELD, text)

    def get_ideas_count(self):
        return len(self.find_multiple(self.locators.IDEAS_COUNT))

    def wait_for_count_of_ideas(self, count: int):
        self.wait_for_count_of_elements(self.locators.IDEAS_COUNT, count)

    def select_idea_theme(self, theme: str):
        self.click(self.locators.IDEA_THEME_SELECT)
        self.click(self.locators.VK_UI_SELECT_ELEM(theme))

    def select_idea_status(self, status: str):
        self.click(self.locators.IDEA_STATUS_SELECT)
        self.click(self.locators.VK_UI_SELECT_ELEM(status))

    def get_idea_title(self):
        return self.find(self.locators.IDEA_TITLE).text

    def go_to_idea(self, title: str):
        self.scroll_click(self.locators.IDEA_LINK(title))
