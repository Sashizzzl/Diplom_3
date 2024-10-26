import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #@allure.step('Переход на нужный URL и открытие браузера на весь экран')
    #def navigate(self,url):
        #self.driver.get(url)
        #self.driver.fullscreen_window()

    @allure.step('Находим элемент')
    def find_element(self, locator,timeout=10):
        try:
            return WebDriverWait(self.driver,timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден за {timeout} секунд.')
            return None

    @allure.step('Кликаем на элемент')
    def click_element(self, locator,timeout=10):
        element = self.find_element(locator,timeout)
        if element:
            element.click()
        else:
            pytest.fail(f'Не получилось кликнуть на элемент с локатором {locator}')

    @allure.step('Вводим текст в поле')
    def enter_text(self,locator,text,timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Не получилость ввести текст в элемент с локатором {locator}')
    @allure.step('Возвращаем текст на элементе')
    def get_text_of_element(self,locator,timeout=10):
        element = self.find_element(locator, timeout)
        return element.text
    @allure.step('Прокручиваем страницу до нужного элемента')
    def scroll_to_element(self,locator,timeout=10):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator,timeout))
    @allure.step('Ожидаем видимость элемента')
    def wait_for_element_visible(self,locator,timeout=10):
        try:
            return WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            print (f'Элемент с локатором {locator} не видим на протяжении {timeout} секунд.')
            return None
    @allure.step('Ожидаем присуствие элемента на странице')
    def element_is_present(self,locator,timeout=10):
        try:
            WebDriverWait(self.driver,timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    @allure.step('Переключаемся на вкладку')
    def switch_to_another_window(self,number):
        self.driver.switch_to.window(self.driver.window_handles[number])
    @allure.step('Ожидаем загрузки страницы')
    def wait_for_browsing_url(self,url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Перетаскиваем выбранный элемент в нужное поле на странице')
    def move_element(self, locator_source, locator_target,  timeout=10):
        source_element= self.find_element(locator_source, timeout)
        target_element = self.find_element(locator_target, timeout)
        if source_element and target_element:
            actions = ActionChains(self.driver)
            actions.click_and_hold(source_element).move_to_element(target_element).release()
        else:
            print(f'Не получилость перетащить элемент с локатором {locator_source}')