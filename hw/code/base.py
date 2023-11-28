from contextlib import contextmanager

import pytest
from _pytest.fixtures import FixtureRequest
from ui.fixtures import get_driver
import os


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        if self.authorize:
            pass

    def add_cookies(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def print_cookies(self):
        print(f"\nCurrent url: {self.driver.current_url}")
        for cookie in self.driver.get_cookies():
            print(f"{cookie['name']} : {cookie['value']}")


@pytest.fixture(scope='session')
def credentials():
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))
