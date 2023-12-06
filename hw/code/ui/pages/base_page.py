import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.wait_conditions import element_in_viewport


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    locators_main = basic_locators.MainPageLocators()
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
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
        self.wait().until(EC.visibility_of_element_located(locator))
        return True

    def has_disappeared(self, locator):
        self.wait().until(EC.invisibility_of_element_located(locator))
        return True
    
    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def switch_to_new_tab(self):
        assert len(self.driver.window_handles) > 1
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_initial_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])


    @allure.step('Click')
    def click(self, locator, timeout=5) -> WebElement:
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


    @allure.step('Fill in')
    def fill_in(self, locator, query, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        elem.clear()
        elem.send_keys(query)
        return elem

    @allure.step('Check url')
    def check_url(self, url, timeout=None):
        self.wait(timeout).until(EC.url_matches(url))

    @allure.step('Check if enabled')
    def is_enabled(self, locator, timeout=5) -> bool:
        elem = self.find(locator, timeout=timeout)

        return elem.is_enabled()
