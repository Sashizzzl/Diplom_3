import allure
from pages.base_page import BasePage
from locators.list_of_orders_page_locators import Locators

class ListOfOrdersPage(BasePage):
    @allure.step('Получить текст заголовка "Лента заказов"')
    def get_text_of_list_of_orders_title(self):
        return self.get_text_of_element(Locators.LIST_OF_ORDERS_TITLE)
    @allure.step('Кликаем на первый заказ в списке заказов')
    def click_first_order_box(self):
        self.click_element(Locators.FIRST_ORDER_IN_LIST_OF_ORDERS)
    @allure.step('Получить текст надписи "Состав" в окне информации о заказе')
    def get_text_of_content_title(self):
        return self.get_text_of_element(Locators.CONTENT_TITLE_IN_ORDER_INFO_WINDOW)
    @allure.step('Кликаем на крестик, чтобы закрыть всплывающее окно')
    def click_close_window(self):
        self.click_element(Locators.CLOSE_ORDER_INFO_WINDOW)
    @allure.step('Прокрутить поле с заказами в ленте заказов до необходимого заказа')
    def scroll_to_specified_order_in_orders_list(self,order_number):
        self.scroll_list(Locators.LIST_OF_ORDERS_FIELD, Locators.order_number_in_list_of_orders_locator(order_number))
    @allure.step('Получить номер найденного заказа в ленте заказов')
    def get_number_of_specified_order_in_orders_list(self,order_number):
        return self.get_text_of_element(Locators.order_number_in_list_of_orders_locator(order_number))
    @allure.step('Найти конкретный заказ в ленте заказов и получить его номер')
    def get_number_of_specified_order_in_orders_list_and_scroll(self):
        self.scroll_to_specified_order_in_orders_list()
        return  self.get_number_of_specified_order_in_orders_list()
    @allure.step('Получить значение счетчика Выполнено за всё время')
    def get_text_of_all_completed_orders_counter(self):
        return self.get_text_of_element(Locators.ALL_COMPLETED_ORDERS_COUNTER)
    @allure.step('Получить значение счетчика Выполнено за сегодня')
    def get_text_of_today_completed_orders_counter(self):
        return self.get_text_of_element(Locators.TODAY_COMPLETED_ORDERS_COUNTER)
    @allure.step('Получить список заказов в работе')
    def get_orders_in_progress_number(self):
        self.get_text_of_element(Locators.LIST_OF_ORDERS_IN_PROGRESS)

