import allure
from helpers import ExpectedMessage
class TestRestorePassword:
    @allure.title('Проверка успешного перехода на страницу восстановления пароля после клика по кнопке "Восстановить пароль"')
    def test_click_restore_password_button_redirects_to_restore_password_page(self, driver,navigate,setup_method):
        main, account, list = setup_method
        main.click_log_in_button()
        account.click_restore_password_button()
        expected_text = account.get_text_of_restore_password_window()
        assert expected_text == ExpectedMessage.RESTORING_PASSWORD
    @allure.title('Проверка успешного ввода почты и клика по кнопке «Восстановить»')
    def test_click_restore_password_opens_page_with_code_from_letter_field(self, driver,navigate,setup_method):
        main, account, list = setup_method
        main.click_log_in_button()
        account.restore_password()
        expected_text = account.get_text_of_enter_code_from_the_letter_field()
        assert expected_text == ExpectedMessage.ENTER_CODE_FROM_LETTER
    @allure.title('Проверка успешного клика по кнопке показать/скрыть пароль - делает поле активным')
    def test_click_show_password_button_makes_password_field_active(self, driver,navigate,setup_method):
        main, account, list = setup_method
        main.click_log_in_button()
        account.restore_password()
        expected_text_inactive_field = account.get_text_of_inactive_password_field()
        assert expected_text_inactive_field == ExpectedMessage.PASSWORD
        account.click_show_password_button()
        expected_text_active_field = account.get_text_of_active_password_field()
        assert expected_text_active_field == ExpectedMessage.PASSWORD
