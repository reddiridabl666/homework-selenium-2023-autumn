import time
from typing import List

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time


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

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def is_visible(self, locator):
        self.find(locator)
        return True

    def is_not_visible(self, locator, timeout=None):
        self.wait(timeout).until(EC.invisibility_of_element(locator))

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_multiple(self, locator, timeout=None) -> List[WebElement]:
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    def find_from(self, parent, locator, timeout=None) -> WebElement:
        def wait_cond(_):
            elem = parent.find_element(*locator)
            if elem.is_displayed():
                return elem
            return False

        return self.wait(timeout).until(wait_cond)

    def find_multiple_from(self, parent, locator, timeout=None) -> List[WebElement]:
        def wait_cond(_):
            elems = parent.find_elements(*locator)
            if all([elem.is_displayed() for elem in elems]):
                return elems
            return False

        return self.wait(timeout).until(wait_cond)

    def switch_to_new_tab(self):
        assert len(self.driver.window_handles) > 1
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_initial_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
        return elem

    def click_may_be_stale(self, locator, timeout=None):
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

    def clear(self, locator, timeout=None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()

        if elem.get_attribute('value') != '':
            size = len(elem.get_attribute('value'))
            elem.send_keys(size * Keys.BACKSPACE)

        return elem

    def is_disabled(self, locator,  timeout=None):
        self.wait(timeout).until(
            EC.element_attribute_to_include(locator, 'disabled'))
        return True

    @allure.step('Fill in')
    def fill_in(self, locator, query, timeout=None) -> WebElement:
        elem = self.clear(locator, timeout)
        elem.send_keys(query)
        return elem

    def press_enter(self, elem):
        elem.send_keys(Keys.RETURN)

    def get_selected_value(self, locator):
        select = Select(self.find(locator))
        return select.all_selected_options[0]

    def select_value(self, locator, value):
        select = Select(self.find(locator))
        select.select_by_visible_text(value)

    @allure.step('Check url')
    def assert_url(self, url, timeout=None):
        if timeout is None:
            timeout = 5
        try:
            self.wait(timeout).until(EC.url_matches(url))
        except:
            raise PageNotOpenedExeption(
                f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait_for_redirect(self, timeout=None):
        self.wait(timeout).until(EC.url_changes(self.driver.current_url))

    def has_error(self, locator, error='Обязательное поле'):
        elem = self.find(self.locators.ERROR)
        self.find_from(elem, locator)
        self.find_from(elem, self.locators.BY_TEXT(error))

    def hover(self, locator):
        elem = self.wait().until(EC.presence_of_element_located(locator))
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()
