import allure
class TestListOfOrders:
    @allure.title('Проверка успешного открытия всплывающего окна с деталями, если кликнуть на заказ в ленте заказов')
    def test_click_order_in_list_of_order_opens_order_details_window(self, driver, navigate, setup_method):
        main, account, list = setup_method
        main.click_list_of_orders_button()
        list.click_first_order_box()
        expected_text_content_of_order = list.get_text_of_content_title()
        assert expected_text_content_of_order == 'Cостав'
    @allure.title('Проверка успешного увеличения счётчика "Выполнено за всё время" при создании нового заказа')
    def test_number_of_all_completed_orders_raises_after_creating_new_order(self, driver, navigate, setup_method,login):
        main, account, list = setup_method
        main.click_list_of_orders_button()
        number_of_orders_before_creating_order = list.get_number_of_all_completed_orders_counter()
        main.click_constructor_button()
        main.create_order()
        main.get_text_of_pop_up_ingredient_info_title()
        main.wait_invisible_number_9999_in_created_order_window()
        main.click_close_window()
        main.click_list_of_orders_button()
        number_of_orders_after_creating_order = list.get_number_of_all_completed_orders_counter()
        assert int(number_of_orders_after_creating_order) > int(number_of_orders_before_creating_order)
    @allure.title('Проверка успешного увеличения счётчика "Выполнено за сегодня" при создании нового заказа')
    def test_number_of_all_completed_today_orders_raises_after_creating_new_order(self, driver, navigate, setup_method, login):
        main, account, list = setup_method
        main.click_list_of_orders_button()
        number_of_orders_before_creating_order = list.get_number_of_today_completed_orders_counter()
        main.click_constructor_button()
        main.create_order()
        main.wait_invisible_number_9999_in_created_order_window()
        main.click_close_window()
        main.click_list_of_orders_button()
        number_of_orders_after_creating_order = list.get_number_of_today_completed_orders_counter()
        assert int(number_of_orders_after_creating_order) > int(number_of_orders_before_creating_order)
    @allure.title('Проверка успешного появления номера оформленного заказа в разделе "В работе"')
    def test_number_of_created_order_shown_in_orders_in_progress(self, driver, navigate, setup_method,login):
        main, account, list = setup_method
        main.create_order()
        main.wait_invisible_number_9999_in_created_order_window()
        number_of_created_order = main.get_number_of_created_order_in_pop_up()
        main.click_close_window()
        main.click_list_of_orders_button()
        list.wait_for_created_order_number_in_orders_in_progress_list(f'0{int(number_of_created_order)}')
        list_of_orders_in_progress = list.get_orders_in_progress_number()
        assert f'0{int(number_of_created_order)}' in list_of_orders_in_progress
    @allure.title('Проверка успешного отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    def test_users_orders_shown_in_list_of_orders(self, driver, navigate, setup_method,login):
        main, account, list = setup_method
        #так как в ленте заказов показывается последние 50 заказов, необходимо создать новый заказ
        main.create_order()
        main.wait_invisible_number_9999_in_created_order_window()
        main.click_close_window()
        main.click_account_button()
        account.click_orders_history_button()
        number_of_last_order_in_order_history = account.get_number_of_last_order_in_order_history()
        account.click_list_of_orders()
        expected_number_of_created_order_in_list = list.get_number_of_specified_order_in_orders_list_and_scroll(number_of_last_order_in_order_history)
        assert number_of_last_order_in_order_history == expected_number_of_created_order_in_list


        