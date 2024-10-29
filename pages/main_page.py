import allure
from pages.base_page import BasePage
from locators.main_page_locators import Locators

class MainPage(BasePage):
    @allure.step('Кликаем на кнопку "Войти в аккаунт"')
    def click_log_in_button(self):
        self.click_element(Locators.LOG_IN_BUTTON)
    @allure.step('Кликаем на кнопку «Личный кабинет»')
    def click_account_button(self):
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
    @allure.step('Кликаем на кнопку «Конструктор»')
    def click_constructor_button(self):
        self.click_element(Locators.CONSTRUCTOR_BUTTON)
    @allure.step('Кликаем на кнопку «Лента заказов»')
    def click_list_of_orders_button(self):
        self.click_element(Locators.LIST_OF_ORDERS_BUTTON)
    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.click_element(Locators.BUN_1)
    @allure.step('Проверяем видимость окна с детялями ингредиента')
    def ingredient_pop_up_info_is_visible(self):
        if self.find_element(Locators.INGREDIENT_POP_UP).is_displayed():
            return True
        return False
    @allure.step('Кликаем на крестик, чтобы закрыть всплывающее окно')
    def click_close_window(self):
        self.click_element(Locators.CLOSE_INGREDIENT_INFO_WINDOW)
        self.invisible_element(Locators.INGREDIENT_POP_UP)
    @allure.step('Перетаскиваем выбранный ингредиент в зону формирования бургера')
    def move_chosen_ingredient_to_making_burger_field(self):
        self.move_element(locator_source=Locators.BUN_DRAGGABLE, locator_target=Locators.UPPER_BUN_FIELD)
    @allure.step('Кликаем на кнопку оформления заказа')
    def click_make_order(self):
        self.click_element(Locators.MAKE_ORDER_BUTTON)
    @allure.step('Оформить заказ')
    def create_order(self):
        self.move_chosen_ingredient_to_making_burger_field()
        self.click_make_order()
    @allure.step('Получаем значение каунтера первого ингредиента булки')
    def get_text_of_bun_1_counter(self):
        return self.get_text_of_element(Locators.COUNTER_BUN_1)
    @allure.step('Получаем номер оформленного заказа из всплывающего окна после оформления заказа')
    def get_number_of_created_order_in_pop_up(self):
        return self.get_text_of_element(Locators.ORDER_NUMBER_IN_POP_UP)
    @allure.step('Получаем текст надписи "Соберите бургер"')
    def get_text_of_constructor_title(self):
        return self.get_text_of_element(Locators.MAKE_BURGER_TITLE)
    @allure.step('Получаем текст надписи "Идентификатор заказа" в окне после создания заказа')
    def get_text_of_pop_up_created_order_title(self):
        return self.get_text_of_element(Locators.ORDER_NUMBER_TITLE_IN_POP_UP)
    @allure.step('Получаем текст надписи "Детали ингредиента" в окне информации об ингредиенте')
    def get_text_of_pop_up_ingredient_info_title(self):
        return self.get_text_of_element(Locators.INGREDIENT_DETAILS_WINDOW_TITLE)
    @allure.step('Ожидание на отсуствие номера заказа 9999 в окне после создания заказа')
    def wait_invisible_number_9999_in_created_order_window(self):
        self.invisible_element(Locators.ORDER_NUMBER_9999)






