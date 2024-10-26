import pytest
from selenium import webdriver
from config import URL
from pages.base_page import BasePage
from locators.main_page_locators import Locators
from locators.account_page_locators import Locators
from pages.account_page import AccountPage
def browser_settings():
    firefox_options = webdriver.FirefoxOptions()
    return firefox_options

@pytest.fixture
def driver():
    firefox = webdriver.Firefox(options=browser_settings())
    firefox.maximize_window()
    yield firefox
    firefox.quit()
@pytest.fixture
def navigate(driver):
    driver.get(URL)
    yield driver
@pytest.fixture
def login(driver,navigate):
    BasePage.click_element(Locators.LOG_IN_BUTTON)
    AccountPage.log_in()
    yield driver

