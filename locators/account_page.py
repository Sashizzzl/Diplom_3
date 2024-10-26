class Locators:
    restore_password_button = ".//a[text()='Восстановить пароль']"  #кнопка восстановления пароля
    restore_password_text = ".//h2[text()='Восстановление пароля']" #надпись "Восстановление пароля"
    email_field_restore_password = ".//label[text() = 'Email']/following-sibling::input" # Поле емейл в окне восстановления пароля
    restore_button = ".//button[text()='Восстановить']"  # кнопка Восстановить
    enter_code_from_the_letter_field = ".//label[text() = 'Введите код из письма']" #поле "Введите код из письма"
    show_password_button = ".//div[contains(@class,'action')]/*" #кнопка  показать/скрыть пароль
    password_field_inactive = ".//div[contains(@class ,'default') and contains(@class,'password')]/input[@name='Введите новый пароль']" #неактивное поле "Пароль"
    password_field_active = ".//div[contains(@class,'active')]/input[@name='Введите новый пароль']" #активное поле "Пароль"
    log_off_button = ".//button[text()='Выход']"  # кнопка "Выход" в личном кабинете

    emeil_log_in = ".//label[text() = 'Email']/following-sibling::input"  # Поле емейл в окне входа
    password_log_in = ".//label[text() = 'Пароль']/following-sibling::input"  # Поле пароль в окне входа

    history_of_orders_button = ".//a[text()='История заказов']"  # кнопка "История заказов" в личном кабинете
    first_order_in_history = ".//li[1]/a[contains(@class,'History')]"  # первый заказ в Истории заказов
    second_order_in_history = ".//li[2]/a[contains(@class,'History')]"  # второй заказ в Истории заказов
    last_but_one_order_in_history = ".//li[last()-1]/a[contains(@class,'History')]"  # предпоследний заказ в Истории заказов
    last_order_in_history = ".//li[last()]/a[contains(@class,'History')]"  # последний заказ в Истории заказов
    history_of_orders_field = ".//ul[contains(@class,'History_list')]"  # область для прокрутки списка заказов в Истории заказов