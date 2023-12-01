import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.hq_page import HqPage
from ui.pages.cases_page import CasesPage
from ui.pages.registration_page import RegistrationMainPage
from ui.pages.audience_page import AudiencePage


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def cases_page(driver):
    driver.get(CasesPage.url)
    return CasesPage(driver=driver)


@pytest.fixture
def registration_main_page(driver):
    driver.get(RegistrationMainPage.url)
    return RegistrationMainPage(driver=driver)


@pytest.fixture(scope='session')
def credentials():
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))


@pytest.fixture(scope='session')
def no_cabinet_credentials():
    return (os.getenv("NO_CABINET_LOGIN"), os.getenv("NO_CABINET_PASSWORD"))


@pytest.fixture
def registration_page(registration_main_page, no_cabinet_credentials):
    page = registration_main_page.go_to_account_creation(
        *no_cabinet_credentials, auth_method='mail')
    yield page
    # page.driver.quit()


@pytest.fixture(scope='session')
def create_account(config, credentials):
    driver = get_driver(config['browser'])

    driver.get(RegistrationMainPage.url)
    page = RegistrationMainPage(driver)

    acc_creation_page = page.go_to_account_creation(*credentials)
    acc_creation_page.fill_in_form('example@mail.org')

    page = HqPage(driver)
    driver.quit()

    yield page

    driver = get_driver(config['browser'])

    driver.get(RegistrationMainPage.url)
    RegistrationMainPage(driver).login(*credentials)

    page = HqPage(driver)
    page.delete_account()
    driver.quit()


@pytest.fixture(scope='session')
def delete_account(create_account, credentials, config):
    driver = get_driver(config['browser'])

    driver.get(RegistrationMainPage.url)
    RegistrationMainPage(driver).login(*credentials)

    page = HqPage(driver)
    page.delete_account()
    driver.quit()


@pytest.fixture
def hq_page(create_account, registration_main_page, credentials):
    registration_main_page.login(*credentials)
    return HqPage(registration_main_page.driver)


@pytest.fixture
def audience_page(hq_page):
    hq_page.driver.get(AudiencePage.url)
    return AudiencePage(driver=hq_page.driver)
