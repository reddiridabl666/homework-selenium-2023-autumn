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
            # for cookie in request.getfixturevalue('cookies'):
            #     self.driver.add_cookie(cookie)

            # self.driver.refresh()


@pytest.fixture(scope='session')
def credentials():
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))


# @pytest.fixture(scope='session')
# def cookies(credentials, config):
#     driver = get_driver(config['browser'])
#     driver.get(config['url'])

#     LoginPage(driver).login(*credentials)
#     cookies = driver.get_cookies()

#     driver.quit()
#     return cookies
