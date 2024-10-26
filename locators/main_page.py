class Locators:
    log_in_button = ".//button[text()='Войти в аккаунт']" #кнопка Войти в аккаунт
    personal_account_button = ".//p[text()='Личный Кабинет']"  #кнопка "Личный кабинет" на главной странице

    #оформление заказа
    bun_1 = ".//img[@alt='Флюоресцентная булка R2-D3']" #ингридиент Флюоресцентная булка R2-D3
    upper_bun_field = ".//span[contains(text(), 'верх')]" #поле верхней булочки
    counter_bun_1 = ".//img[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::div/p"  # каунтер  ингредиента Флюоресцентная булка R2-D3
    make_order_button = ".//button[text()='Оформить заказ']"  #кнопка "Оформить заказ

    order_number_title_in_pop_up = ".//p[text()='идентификатор заказа']"  # надпись "идентификатор заказа" во всплывающем окне после оформления заказа
    order_number_in_pop_up = ".//h2[contains(@class,'digits')]"  # номер оформленного заказа во всплывающем окне после оформления заказа

    ingredient_details_window_title = ".//h2[text()='Детали ингредиента']" #надпись "Детали ингредиента" во всплывающем окне о деталях ингредиента
    close_ingredient_info_window = ".//section[contains(@class,'opened')]//button[contains(@class,'close')]/*" #крестик

    constructor_button = ".//p[text() = 'Конструктор']" #элемент Конструктор
    make_burger_title = ".//h1[text()='Соберите бургер']" #надпись "Соберите бургер"
    list_of_orders_button = ".//a[@href='/feed']" #кнопка Лента заказов




