import pytest
from selenium import webdriver
from config import URL
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.list_of_orders_page import  ListOfOrdersPage
def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    return chrome_options

@pytest.fixture(scope="function")
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.maximize_window()
    yield chrome
    chrome.quit()
@pytest.fixture
def navigate(driver):
    driver.get(URL)
    yield driver
@pytest.fixture(autouse=True)
def setup_method(driver):
    main = MainPage(driver)
    account = AccountPage(driver)
    list = ListOfOrdersPage(driver)
    return main, account, list
@pytest.fixture
def login(driver,navigate,setup_method):
    main, account, list = setup_method
    main.click_log_in_button()
    account.log_in()
    yield driver

