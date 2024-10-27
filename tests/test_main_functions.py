import allure
from helpers import ExpectedMessage
class TestMainFunctions:
    @allure.title('Проверка успешного перехода по клику на «Конструктор»')
    def test_click_consructor_button_redirects_to_create_order_page(self, driver, navigate, setup_method):
        main, account, list = setup_method
        main.click_account_button()
        main.click_constructor_button()
        expected_text_of_create_burger_title = main.get_text_of_constructor_title()
        assert expected_text_of_create_burger_title == ExpectedMessage.MAKE_BURGER
    @allure.title('Проверка успешного перехода по клику на «Лента заказов»')
    def test_click_orders_list_button_redirects_to_orders_list_page(self, driver, navigate, setup_method):
        main, account, list = setup_method
        main.click_list_of_orders_button()
        expected_text_of_create_burger_title = list.get_text_of_list_of_orders_title()
        assert expected_text_of_create_burger_title == ExpectedMessage.ORDERS_LIST
    @allure.title('Проверка появления всплывающего окна с деталями после клика на ингредиент')
    def test_click_ingredient_shows_ingredient_info(self, driver, navigate, setup_method):
        main, account, list = setup_method
        main.click_on_ingredient()
        expected_text_ingredients_detail_pop_up_title = main.get_text_of_pop_up_ingredient_info_title()
        assert expected_text_ingredients_detail_pop_up_title == ExpectedMessage.INGREDIENT_DETAILS
    @allure.title('Проверка всплывающее окно с деталями ингредиента закрывается кликом по крестику')
    def test_click_ingredient_shows_ingredient_info(self, driver, navigate, setup_method):
        main, account, list = setup_method
        main.click_on_ingredient()
        expected_text_ingredients_detail_pop_up_title = main.get_text_of_pop_up_ingredient_info_title()
        assert expected_text_ingredients_detail_pop_up_title == ExpectedMessage.INGREDIENT_DETAILS
        main.click_close_window()
        main.ingredient_pop_up_info_is_visible()
        assert not main.ingredient_pop_up_info_is_visible()
    @allure.title('Проверка увеличения каунтера  ингредиента при добавлении его в заказ')
    def test_after_adding_ingredient_counter_adds_up(self, driver, navigate, setup_method):
        main, account, list = setup_method
        counter_number_before_choosing_ingredient = main.get_text_of_bun_1_counter()
        main.move_chosen_ingredient_to_making_burger_field()
        counter_number_after_choosing_ingredient = main.get_text_of_bun_1_counter()
        assert int(counter_number_after_choosing_ingredient) - int(counter_number_before_choosing_ingredient) == 2
    @allure.title('Проверка успешного оформления заказа залогиненным пользователем')
    def test_authorized_user_create_order_order_created(self, driver, navigate, setup_method,login):
        main, account, list = setup_method
        main.create_order()
        expected_text_created_order_number = main.get_text_of_pop_up_created_order_title()
        assert expected_text_created_order_number != None and expected_text_created_order_number != ExpectedMessage.DEFAULT_ORDER_NUMBER


