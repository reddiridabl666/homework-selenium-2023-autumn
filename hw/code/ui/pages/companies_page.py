from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.hq_page import HqPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CompaniesPage(HqPage):
    url = 'https://ads.vk.com/hq/dashboard/ads'
    locators = basic_locators.CompaniesLocators

    TARGET_SITE = 'event-radar.ru'

    def click_create_btn(self):
        self.find((By.NAME, 'Создать')).click()

    def select_site_target(self):
        self.find((By.XPATH, "//div[@data-testid='audience-item-menu']"))

    def input_site_value(self, url):
        input = self.find((By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/section[3]/div[1]/form/div/div/div/div[1]/span/input'))
        input.click()
        input.send_keys(url)
        input.send_keys(Keys.RETURN)

    def input_money_value(self, money_value):
        input = self.find((By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/section[3]/div[1]/form/div/div[7]/div/span[1]/input'))
        input.click()
        input.send_keys(money_value)
        input.send_keys(Keys.RETURN)

    def click_contitnue_btn(self):
        self.find((By.NAME, 'Продолжить')).click()

    def create_company(self, url, money):
        self.click_create_btn()
        self.select_site_target()
        self.input_site_value(url)
        self.input_money_value(money)
        self.click_contitnue_btn()

    def select_mobileapp_target(self):
        self.find((By.XPATH, "//div[@data-id='mobapps']")).click()

    def has_target_input(self):
        try:
            elem = self.find((By.CLASS_NAME, 'SiteObject_formItemWrapper__4pPhN'))
            return True
        except NoSuchElementException:
            return False

    def has_mobile_target_input(self):
        try:
            elem = self.find((By.XPATH, "//span[@data-testid='mob-app-select']"))
            return True
        except NoSuchElementException:
            return False
        
    def go_to_root(self):
        self.find((By.XPATH, '//*[@id="root"]/div/div[1]/header/div/div[1]/button')).click()
    
    def click_drafts_btn(self):
        self.find((By.XPATH, '//*[@id="dashboardV2"]/div/div[1]/div/div[1]/div[1]/button')).click()

    def input_search_query(self, query):
        input = self.find((By.XPATH, '//*[@id="dashboardV2"]/div/div[1]/div/div/div[1]/div[2]/div/div/div/label/input'))
        input.click()
        input.send_keys(query)
        