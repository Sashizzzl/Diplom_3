import allure
from helpers import ExpectedMessage
class TestAccount:
    @allure.title('Проверка успешного перехода по клику на «Личный кабинет»')
    def test_click_account_button_redirects_to_account_page(self, driver, navigate, setup_method, login):
        main, account, list = setup_method
        main.click_account_button()
        expected_text = account.get_text_of_account_info()
        assert expected_text == ExpectedMessage.ABLE_TO_CHOSE_PERSONAL_INFO
    @allure.title('Проверка успешного перехода в раздел «История заказов»')
    def test_click_history_button_shows_order_history(self, driver, navigate, setup_method, login):
        main, account, list = setup_method
        #создаем заказ, чтобы проверить переход в историю заказов
        main.create_order()
        main.wait_invisible_number_9999_in_created_order_window()
        main.click_close_window()
        main.click_account_button()
        account.click_orders_history_button()
        last_order_number = account.get_number_of_last_order_in_order_history()
        assert last_order_number != None
    @allure.title('Проверка успешного выхода из аккаунта')
    def test_log_out_click_log_out_button_log_in_button_appeared(self, driver, navigate, setup_method, login):
        main, account, list = setup_method
        main.click_account_button()
        account.click_log_out_button()
        expected_message_log_in_button = account.get_text_of_log_in_button()
        assert expected_message_log_in_button == ExpectedMessage.LOG_IN