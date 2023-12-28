import time
from typing import List

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from ui.wait_conditions import element_in_viewport
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators import basic_locators
from ui.wait_conditions import element_in_viewport, elements_count_changed
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
import os


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.startswith(self.url):
                return True
        raise PageNotOpenedExeption(
            f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver
        self.is_opened()

        self.close_cookie_banner()

    def close_cookie_banner(self):
        try:
            self.click(self.locators.COOKIE_BANNER_BUTTON)
        except:
            pass

    def wait(self, timeout: float | None = None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_until_element_not_visible(self, locator, timeout: float | None = None):
        return self.wait(timeout).until(EC.invisibility_of_element_located(locator))

    def is_visible(self, locator, timeout: float | None = None):
        try:
            elem = self.find(locator, timeout)
            elem.location_once_scrolled_into_view
            return True
        except:
            return False

    def is_not_visible(self, locator, timeout: float | None = None):
        try:
            self.wait(timeout).until(EC.invisibility_of_element(locator))
            return True
        except:
            return False

    def find(self, locator, timeout: float | None = None, cond=EC.visibility_of_element_located) -> WebElement:
        return self.wait(timeout).until(cond(locator))

    def find_invisible(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_multiple(self, locator, timeout: float | None = None, cond=EC.visibility_of_all_elements_located) -> List[WebElement]:
        return self.wait(timeout).until(cond(locator))

    def find_from(self, parent, locator, timeout: float | None = None) -> WebElement:
        def wait_cond(_):
            elem = parent.find_element(*locator)
            if elem.is_displayed():
                return elem
            return False

        return self.wait(timeout).until(wait_cond)

    def find_multiple_from(self, parent, locator, timeout: float | None = None) -> List[WebElement]:
        def wait_cond(_):
            elems = parent.find_elements(*locator)
            if all([elem.is_displayed() for elem in elems]):
                return elems
            return False

        return self.wait(timeout).until(wait_cond)

    def get_element(self, locator, timeout: float | None = None, cond=EC.visibility_of_all_elements_located) -> WebElement:
        try:
            return self.find(locator, timeout)
        except TimeoutException:
            return None

    def get_new_count(self, locator, start_size, timeout: float | None = None):
        elems = self.wait(timeout).until(
            elements_count_changed(locator, start_size))
        return len(elems)

    def wait_for_count_of_elements(self, locator, count, timeout: float | None = None):
        self.wait(timeout).until(lambda _: len(
            self.find_multiple(locator)) == count)

    def switch_to_new_tab(self):
        assert len(self.driver.window_handles) > 1
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_initial_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step('Click')
    def click(self, locator, timeout: float | None = None) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))

        elem.click()

        return elem

    @allure.step('Scroll click')
    def scroll_click(self, locator, timeout=5) -> WebElement:
        elem = self.find(locator, timeout=timeout)

        self.wait(timeout).until(EC.visibility_of_element_located(locator))
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))

        elem.location_once_scrolled_into_view

        self.wait(timeout).until(element_in_viewport(locator))

        elem.click()

        return elem

    def click_may_be_stale(self, locator, timeout: float | None = None):
        if timeout is None:
            timeout = 5

        start = time.time()
        try:
            self.click(locator, timeout)
        except StaleElementReferenceException:
            new_timeout = timeout + start - time.time()
            if new_timeout < 0:
                return
            self.click_may_be_stale(locator, new_timeout)

    def clear(self, locator, timeout: float | None = None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()

        if elem.get_attribute('value') != '':
            size = len(elem.get_attribute('value'))
            elem.send_keys(size * Keys.BACKSPACE)

        return elem

    @allure.step('Scroll click')
    def scroll_click(self, locator, timeout: float | None = None) -> WebElement:
        self.find(locator, timeout)

        self.wait(timeout).until(EC.visibility_of_element_located(locator))
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))

        elem.location_once_scrolled_into_view

        self.wait(timeout).until(element_in_viewport(locator))

        elem.click()

        return elem

    def is_disabled(self, locator, timeout=None):
        self.wait(timeout).until(
            EC.element_attribute_to_include(locator, 'disabled'))
        return True

    @allure.step('Fill in')
    def fill_in(self, locator, query: str, timeout: float | None = None) -> WebElement:
        elem = self.clear(locator, timeout)
        elem.send_keys(query)
        return elem

    def press_enter(self, elem):
        elem.send_keys(Keys.RETURN)

    def press_tab(self, elem):
        elem.send_keys(Keys.TAB)

    def get_selected_value(self, locator):
        select = Select(self.find(locator))
        return select.all_selected_options[0]

    def select_value(self, locator, value):
        select = Select(self.find(locator))
        select.select_by_visible_text(value)

    @allure.step('Check if enabled')
    def is_enabled(self, locator, timeout=5) -> bool:
        elem = self.find(locator, timeout=timeout)
        return elem.is_enabled()

    def wait_for_redirect(self, timeout: float | None = None):
        self.wait(timeout).until(EC.url_changes(self.driver.current_url))

    def form_error(self, locator, error) -> WebElement:
        try:
            error_container = self.find(self.locators.ERROR)
            self.find_from(error_container, locator)
            error = self.find_from(
                error_container, self.locators.BY_TEXT(error))
            return error
        except TimeoutException:
            return None

    def hover(self, locator, cond=EC.presence_of_element_located):
        elem = self.wait().until(cond(locator))
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()

    def upload_file(self, locator, file_path):
        absolute_file_path = os.path.abspath(file_path)

        elem = self.find_invisible(locator)
        elem.send_keys(absolute_file_path)

        return elem
