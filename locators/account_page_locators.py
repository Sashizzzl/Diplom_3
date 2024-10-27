from selenium.webdriver.common.by import By
class Locators:
    RESTORE_PASSWORD_BUTTON = [By.XPATH,".//a[text()='Восстановить пароль']"]  #кнопка восстановления пароля
    RESTORE_PASSWORD_WINDOW_TEXT = [By.XPATH,".//h2[text()='Восстановление пароля']"] #надпись "Восстановление пароля"
    EMAIL_FIELD_RESTORE_PASSWORD = [By.XPATH,".//label[text() = 'Email']/following-sibling::input"] #поле емейл в окне восстановления пароля
    RESTORE_BUTTON = [By.XPATH,".//button[text()='Восстановить']"]  #кнопка Восстановить
    ENTER_CODE_FROM_THE_LETTER_FIELD = [By.XPATH,".//label[text() = 'Введите код из письма']"] #поле "Введите код из письма"

    SHOW_PASSWORD_BUTTON = [By.XPATH,".//div[contains(@class,'action')]/*"] #кнопка  показать/скрыть пароль
    PASSWORD_FIELD_INACTIVE = [By.XPATH,".//div[contains(@class ,'default') and contains(@class,'password')]/label"] #неактивное поле "Пароль"
    PASSWORD_FIELD_ACTIVE = [By.XPATH,".//div[contains(@class,'active')]/label"] #активное поле "Пароль"
    LOG_OUT_BUTTON = [By.XPATH,".//button[text()='Выход']"]  # кнопка "Выход" в личном кабинете

    EMAIL_LOG_IN = [By.XPATH,".//label[text() = 'Email']/following-sibling::input"]  # Поле емейл в окне входа
    PASSWORD_LOG_IN = [By.XPATH,".//label[text() = 'Пароль']/following-sibling::input"]  # Поле пароль в окне входа
    LOG_IN_BUTTON = [By.XPATH,".//button[text()='Войти']"] #кнопка войти

    HISTORY_OF_ORDERS_BUTTON = [By.XPATH,".//a[text()='История заказов']"]  # кнопка "История заказов" в личном кабинете
    HISTORY_OF_ORDERS_ACTIVE_BUTTON = [By.XPATH,".//a[contains(@class,'link_active') and text()='История заказов']"] #активная кнопка "История заказов"
    #FIRST_ORDER_IN_HISTORY = [By.XPATH,".//li[1]/a[contains(@class,'History')]"]  # первый заказ в Истории заказов
    #SECOND_ORDER_IN_HISTORY = [By.XPATH,".//li[2]/a[contains(@class,'History')]"]  # второй заказ в Истории заказов
    #LAST_BUT_ONE_ORDER_IN_HISTORY = [By.XPATH,".//li[last()-1]//div[contains(@class,'Box')]/p[contains(@class,'digits')]"]  # предпоследний заказ в Истории заказов
    LAST_ORDER_NUMBER_IN_HISTORY = [By.XPATH,".//li[last()]//div[contains(@class,'Box')]/p[contains(@class,'digits')]"]  #номер последнего заказа в Истории заказов
    HISTORY_OF_ORDERS_FIELD = [By.XPATH,".//div[contains(@class,'orderHistory')]"]  # область для прокрутки списка заказов в Истории заказов

    ACCOUNT_INFO_TEXT = [By.XPATH,".//p[contains(text(),'данные')]"] #надпись "В этом разделе вы можете изменить свои персональные данные"
    LIST_OF_ORDERS_BUTTON = [By.XPATH, ".//a[@href='/feed']"]  # кнопка Лента заказов