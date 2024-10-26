class Locators:
    RESTORE_PASSWORD_BUTTON = ".//a[text()='Восстановить пароль']"  #кнопка восстановления пароля
    RESTORE_PASSWORD_TEXT = ".//h2[text()='Восстановление пароля']" #надпись "Восстановление пароля"
    EMAIL_FIELD_RESTORE_PASSWORD = ".//label[text() = 'Email']/following-sibling::input" # Поле емейл в окне восстановления пароля
    RESTORE_BUTTON = ".//button[text()='Восстановить']"  # кнопка Восстановить
    ENTER_CODE_FROM_THE_LETTER_FIELD = ".//label[text() = 'Введите код из письма']" #поле "Введите код из письма"
    SHOW_PASSWORD_BUTTON = ".//div[contains(@class,'action')]/*" #кнопка  показать/скрыть пароль
    PASSWORD_FIELD_INACTIVE = ".//div[contains(@class ,'default') and contains(@class,'password')]/input[@name='Введите новый пароль']" #неактивное поле "Пароль"
    password_fIeld_active = ".//div[contains(@class,'active')]/input[@name='Введите новый пароль']" #активное поле "Пароль"
    LOG_OFF_BUTTON = ".//button[text()='Выход']"  # кнопка "Выход" в личном кабинете

    EMAIL_LOG_IN = ".//label[text() = 'Email']/following-sibling::input"  # Поле емейл в окне входа
    PASSWORD_LOG_IN = ".//label[text() = 'Пароль']/following-sibling::input"  # Поле пароль в окне входа
    LOG_IN_BUTTON = ".//button[text()='Войти']" #кнопка войти

    HISTORY_OF_ORDERS_BUTTON = ".//a[text()='История заказов']"  # кнопка "История заказов" в личном кабинете
    FIRST_ORDER_IN_HISTORY = ".//li[1]/a[contains(@class,'History')]"  # первый заказ в Истории заказов
    SECOND_ORDER_IN_HISTORY = ".//li[2]/a[contains(@class,'History')]"  # второй заказ в Истории заказов
    LAST_BUT_ONE_ORDER_IN_HISTORY = ".//li[last()-1]/a[contains(@class,'History')]"  # предпоследний заказ в Истории заказов
    LAST_ORDER_IN_HISTORY = ".//li[last()]/a[contains(@class,'History')]"  # последний заказ в Истории заказов
    HISTORY_OF_ORDERS_FIELD = ".//ul[contains(@class,'History_list')]"  # область для прокрутки списка заказов в Истории заказов