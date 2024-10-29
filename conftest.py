import pytest
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from config import URL
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.list_of_orders_page import  ListOfOrdersPage
import random
from config import URL_REGISTER

@pytest.fixture(params=["chrome","firefox"])
def driver(request):
    browser_name = request.param
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.maximize_window()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        browser.maximize_window()
    else:
        ValueError("Can't create instance for this browser params")
    yield browser
    browser.quit()
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
@allure.title('Создаем и в конце удаляем нового пользователя с помощью АПИ')
@pytest.fixture
def create_new_user_api():
    payload = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": random.randint(100000, 999999), "name": f'Sasha{random.randint(1000, 9999)}'}
    response = requests.post(URL_REGISTER, data=payload)
    access_token = response.json()['accessToken']
    yield payload
    requests.delete(URL_REGISTER,headers={'Authorization': access_token})
@allure.title('Вход в аккаунт')
@pytest.fixture
def login(driver,navigate,setup_method,create_new_user_api):
    main, account, list = setup_method
    main.click_log_in_button()
    account.log_in(create_new_user_api)
    yield driver

