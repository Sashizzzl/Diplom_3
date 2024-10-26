class Locators:
    LIST_OF_ORDERS_TITLE = ".//h1[text()='Лента заказов']"  # заголовок "Лента заказов"
    @staticmethod
    def order_number_in_list_of_orders_locator(order_number):
        return f".//div[contains(@class,'Box')]/child::p[contains(text(),'{order_number}')]"  # для поиска в ленте заказов

    LIST_OF_ORDERS_FIELD = ".//ul[contains(@class,'Feed_list')]"  # область для прокрутки списка заказов в Ленте заказов
    FIRST_ORDER_IN_LIST_OF_ORDERS = ".//li[1]/a[contains(@class,'History')]"  # первый заказ в Ленте заказов
    #NUMBER_OF_FIRST_ORDER_LIST_OF_ORDERS = ".//li[1]//div[contains(@class,'Box')]/child::p[contains(@class,'digits')]"  # номер первого заказа в Ленте заказов
    CONTENT_TITLE_IN_ORDER_INFO_WINDOW = ".//p[contains(@class,'mb-8')]"  # надпись "Состав" в окне информации о заказе

    ALL_COMPLETED_ORDERS_COUNTER = ".//p[text()='Выполнено за все время:']/following-sibling::p"  # значение счетчика Выполнено за всё время
    TODAY_COMPLETED_ORDERS_COUNTER = ".//p[text()='Выполнено за сегодня:']/following-sibling::p "  # значение счетчика Выполнено за сегодня
    LIST_OF_ORDERS_IN_PROGRESS = ".//ul[contains(@class,'Ready')]/li"  # список заказов в работе

    CLOSE_ORDER_INFO_WINDOW = ".//section[contains(@class,'opened')]//button[contains(@class,'close')]/*"  # крестик