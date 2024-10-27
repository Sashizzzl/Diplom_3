import allure

class TestListOfOrders:
    @allure.title('Проверка успешного перехода по клику на «Личный кабинет»,')
    def test_click_account_button_redirects_to_account_page(self, driver, navigate, setup_method):
        main, account, list = setup_method
        