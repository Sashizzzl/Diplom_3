import allure
from pages.base_page import BasePage
from locators.account_page_locators import Locators
from data import Data

class AccountPage(BasePage):
    @allure.step('Ввести данные в поле Емейл окна входа в аккаунт')
    def fill_in_email_log_in_window(self):
        self.enter_text(Locators.EMAIL_LOG_IN, Data.email)
    @allure.step('Ввести данные в поле пароля окна входа в аккаунт')
    def fill_in_password_log_in_window(self):
        self.enter_text(Locators.PASSWORD_LOG_IN, Data.password)
    @allure.step('Кликаем на кнопку "Войти"')
    def click_log_in_button(self):
        self.click_element(Locators.LOG_IN_BUTTON)
    @allure.step('Войти в аккаунт')
    def log_in(self):
        self.fill_in_email_log_in_window()
        self.fill_in_password_log_in_window()
        self.click_log_in_button()
    @allure.step('Кликаем на кнопку "Восстановить пароль"')
    def click_restore_password_button(self):
        self.click_element(Locators.RESTORE_PASSWORD_BUTTON)
    @allure.step('Получить текст заголовка "Восстановление пароля"')
    def get_text_of_restore_password_window(self):
        return self.get_text_of_element(Locators.RESTORE_PASSWORD_WINDOW_TEXT)
    @allure.step('Ввести данные в поле Емейл окна восстановления пароля')
    def fill_in_email_restore_window(self):
        self.enter_text(Locators.EMAIL_FIELD_RESTORE_PASSWORD,Data.email)
    @allure.step('Кликаем на кнопку "Восстановить"')
    def click_restore_button(self):
        self.click_element(Locators.RESTORE_BUTTON)
    @allure.step('Восстановление пароля')
    def restore_password(self):
        self.click_restore_password_button()
        self.fill_in_email_restore_window()
        self.click_restore_button()
    @allure.step('Получить текст поля "Введите код из письма"')
    def get_text_of_enter_code_from_the_letter_field(self):
        return self.get_text_of_element(Locators.ENTER_CODE_FROM_THE_LETTER_FIELD)
    @allure.step('Получить текст неактивного поля "Пароль"')
    def get_text_of_inactive_password_field(self):
        return self.get_text_of_element(Locators.PASSWORD_FIELD_INACTIVE)
    @allure.step('Кликаем на кнопку показать/скрыть пароль')
    def click_show_password_button(self):
        self.click_element(Locators.SHOW_PASSWORD_BUTTON)
    @allure.step('Получить текст активного поля "Пароль"')
    def get_text_of_active_password_field(self):
        return self.get_text_of_element(Locators.PASSWORD_FIELD_ACTIVE)
    @allure.step('Кликаем на кнопку "История заказов"')
    def click_orders_history_button(self):
        self.click_element(Locators.HISTORY_OF_ORDERS_BUTTON)
    @allure.step('Получить текст активной кнопки "История заказов"')
    def get_text_of_active_orders_history_button(self):
        return self.get_text_of_element(Locators.HISTORY_OF_ORDERS_ACTIVE_BUTTON)
    @allure.step('Кликаем на кнопку "Выход"')
    def click_log_out_button(self):
        self.click_element(Locators.LOG_OUT_BUTTON)
    @allure.step('Получить текст кнопки "Войти"')
    def get_text_of_log_in_button(self):
        return self.get_text_of_element(Locators.LOG_IN_BUTTON)
    @allure.step('Прокрутить поле с заказами в истории заказов до последнего заказа')
    def scroll_to_last_order_in_order_history(self):
        self.scroll_list(Locators.HISTORY_OF_ORDERS_FIELD,Locators.LAST_ORDER_NUMBER_IN_HISTORY)
    @allure.step('Получить номер последнего заказа в истории заказов')
    def get_number_of_last_order_in_order_history(self):
        return self.get_text_of_element(Locators.LAST_ORDER_NUMBER_IN_HISTORY)
    @allure.step('Прокрутить поле заказов и получить номер последнего заказа в истории заказов')
    def get_number_of_last_order_in_order_history_with_scroll(self):
        self.scroll_to_last_order_in_order_history()
        return self.get_number_of_last_order_in_order_history()
    @allure.step('Получить текст надписи "В этом разделе вы можете изменить свои персональные данные"')
    def get_text_of_account_info(self):
        return self.get_text_of_element(Locators.ACCOUNT_INFO_TEXT)





