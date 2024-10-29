from selenium.webdriver.common.by import By
class Locators:
    LOG_IN_BUTTON = [By.XPATH,".//button[text()='Войти в аккаунт']"] #кнопка Войти в аккаунт
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH,".//p[text()='Личный Кабинет']"]  #кнопка "Личный кабинет" на главной странице
    MAKE_ORDER_BUTTON = [By.XPATH,".//button[text()='Оформить заказ']"]  # кнопка "Оформить заказ
    #оформление заказа
    BUN_1 = [By.XPATH,".//img[@alt='Флюоресцентная булка R2-D3']"] #ингридиент Флюоресцентная булка R2-D3
    BUN_DRAGGABLE = [By.XPATH,".//a[(@href='/ingredient/61c0c5a71d1f82001bdaaa6d')]"] #перетаскиваемая область булки1
    UPPER_BUN_FIELD = [By.XPATH,".//div[contains(@class, 'constructor-element_pos_top')]"] #поле верхней булочки
    COUNTER_BUN_1 = [By.XPATH,".//img[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::div/p"]  # каунтер  ингредиента Флюоресцентная булка R2-D3
    BUN_ADDED_TO_BURGER = [By.XPATH,".//span[contains(text(),'D3 (верх)')]"] #добавленная булка в бургер

    ORDER_NUMBER_TITLE_IN_POP_UP = [By.XPATH,".//p[text()='идентификатор заказа']"]  #надпись "идентификатор заказа" во всплывающем окне после оформления заказа
    ORDER_NUMBER_IN_POP_UP = [By.XPATH,".//h2[contains(@class,'digits')]"]  #номер оформленного заказа во всплывающем окне после оформления заказа
    ORDER_NUMBER_9999 = [By.XPATH,".//h2[text()='9999']"] #номер заказа 9999
    INGREDIENT_DETAILS_WINDOW_TITLE = [By.XPATH,".//h2[text()='Детали ингредиента']"] #надпись "Детали ингредиента" во всплывающем окне о деталях ингредиента
    CLOSE_INGREDIENT_INFO_WINDOW = [By.XPATH,".//section[contains(@class,'opened')]//button[contains(@class,'close')]/*"] #крестик

    CONSTRUCTOR_BUTTON = [By.XPATH,".//p[text() = 'Конструктор']"] #элемент Конструктор
    MAKE_BURGER_TITLE = [By.XPATH,".//h1[text()='Соберите бургер']"] #надпись "Соберите бургер"
    LIST_OF_ORDERS_BUTTON = [By.XPATH,".//a[@href='/feed']"] #кнопка Лента заказов
    INGREDIENT_POP_UP = [By.XPATH,".//div[contains(@class,'pb-15')]/parent::div[contains(@class,'container__Wo2l_')]"] #окно с деталями ингредиента