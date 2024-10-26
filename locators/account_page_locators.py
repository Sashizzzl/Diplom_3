class Locators:
    RESTORE_PASSWORD_BUTTON = ".//a[text()='Восстановить пароль']"  #кнопка восстановления пароля
    RESTORE_PASSWORD_WINDOW_TEXT = ".//h2[text()='Восстановление пароля']" #надпись "Восстановление пароля"
    EMAIL_FIELD_RESTORE_PASSWORD = ".//label[text() = 'Email']/following-sibling::input" #поле емейл в окне восстановления пароля
    RESTORE_BUTTON = ".//button[text()='Восстановить']"  #кнопка Восстановить
    ENTER_CODE_FROM_THE_LETTER_FIELD = ".//label[text() = 'Введите код из письма']" #поле "Введите код из письма"
    SHOW_PASSWORD_BUTTON = ".//div[contains(@class,'action')]/*" #кнопка  показать/скрыть пароль
    PASSWORD_FIELD_INACTIVE = ".//div[contains(@class ,'default') and contains(@class,'password')]/input[@name='Введите новый пароль']" #неактивное поле "Пароль"
    PASSWORD_FIELD_ACTIVE = ".//div[contains(@class,'active')]/input[@name='Введите новый пароль']" #активное поле "Пароль"
    LOG_OUT_BUTTON = ".//button[text()='Выход']"  # кнопка "Выход" в личном кабинете

    EMAIL_LOG_IN = ".//label[text() = 'Email']/following-sibling::input"  # Поле емейл в окне входа
    PASSWORD_LOG_IN = ".//label[text() = 'Пароль']/following-sibling::input"  # Поле пароль в окне входа
    LOG_IN_BUTTON = ".//button[text()='Войти']" #кнопка войти

    HISTORY_OF_ORDERS_BUTTON = ".//a[text()='История заказов']"  # кнопка "История заказов" в личном кабинете
    HISTORY_OF_ORDERS_ACTIVE_BUTTON = ".//a[contains(@class,'link_active') and text()='История заказов']" #активная кнопка "История заказов"
    #FIRST_ORDER_IN_HISTORY = ".//li[1]/a[contains(@class,'History')]"  # первый заказ в Истории заказов
    #SECOND_ORDER_IN_HISTORY = ".//li[2]/a[contains(@class,'History')]"  # второй заказ в Истории заказов
    #LAST_BUT_ONE_ORDER_IN_HISTORY = ".//li[last()-1]//div[contains(@class,'Box')]/p[contains(@class,'digits')]"  # предпоследний заказ в Истории заказов
    LAST_ORDER_NUMBER_IN_HISTORY = ".//li[last()]//div[contains(@class,'Box')]/p[contains(@class,'digits')]"  #номер последнего заказа в Истории заказов
    HISTORY_OF_ORDERS_FIELD = ".//div[contains(@class,'orderHistory')]"  # область для прокрутки списка заказов в Истории заказов