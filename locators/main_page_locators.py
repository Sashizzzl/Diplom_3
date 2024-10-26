class Locators:
    LOG_IN_BUTTON = ".//button[text()='Войти в аккаунт']" #кнопка Войти в аккаунт
    PERSONAL_ACCOUNT_BUTTON = ".//p[text()='Личный Кабинет']"  #кнопка "Личный кабинет" на главной странице
    MAKE_ORDER_BUTTON = ".//button[text()='Оформить заказ']"  # кнопка "Оформить заказ
    #оформление заказа
    BUN_1 = ".//img[@alt='Флюоресцентная булка R2-D3']" #ингридиент Флюоресцентная булка R2-D3
    UPPER_BUN_FIELD = ".//span[contains(text(), 'верх')]" #поле верхней булочки
    COUNTER_BUN_1 = ".//img[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::div/p"  # каунтер  ингредиента Флюоресцентная булка R2-D3

    ORDER_NUMBER_TITLE_IN_POP_UP = ".//p[text()='идентификатор заказа']"  #надпись "идентификатор заказа" во всплывающем окне после оформления заказа
    ORDER_NUMBER_IN_POP_UP = ".//h2[contains(@class,'digits')]"  #номер оформленного заказа во всплывающем окне после оформления заказа

    INGREDIENT_DETAILS_WINDOW_TITLE = ".//h2[text()='Детали ингредиента']" #надпись "Детали ингредиента" во всплывающем окне о деталях ингредиента
    CLOSE_INGREDIENT_INFO_WINDOW = ".//section[contains(@class,'opened')]//button[contains(@class,'close')]/*" #крестик

    CONSTRUCTOR_BUTTON = ".//p[text() = 'Конструктор']" #элемент Конструктор
    MAKE_BURGER_TITLE = ".//h1[text()='Соберите бургер']" #надпись "Соберите бургер"
    LIST_OF_ORDERS_BUTTON = ".//a[@href='/feed']" #кнопка Лента заказов




