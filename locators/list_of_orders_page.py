class Locators:
    list_of_orders_title = ".//h1[text()='Лента заказов']"  # заголовок "Лента заказов"
    @staticmethod
    def order_number_in_list_of_orders_locator(order_number):
        for_search_in_list_of_orders = f".//div[contains(@class,'Box')]/child::p[contains(text(),'{order_number}')]"  # для поиска в ленте заказов
    # чтобы потом испоьзовать это в тесте, сделай так locator = Locators.order_number_locator(order_number)

    list_of_orders_field = ".//ul[contains(@class,'Feed_list')]"  # область для прокрутки списка заказов в Ленте заказов
    first_order_in_list_of_orders = ".//li[1]/a[contains(@class,'History')]"  # первый заказ в Ленте заказов
    number_of_first_order_list_of_orders = ".//li[1]//div[contains(@class,'Box')]/child::p[contains(@class,'digits')]"  # номер первого заказа в Ленте заказов
    content_title_in_order_info_window = ".//p[contains(@class,'mb-8')]"  # надпись "Состав" в окне информации о заказе

    all_completed_orders_counter = ".//p[text()='Выполнено за все время:']/following-sibling::p"  # значение счетчика Выполнено за всё время
    today_completed_orders_counter = ".//p[text()='Выполнено за сегодня:']/following-sibling::p "  # значение счетчика Выполнено за сегодня
    list_of_orders_in_progress = ".//ul[contains(@class,'Ready')]/li"  # список заказов в работе

    close_ingredient_info_window = ".//section[contains(@class,'opened')]//button[contains(@class,'close')]/*"  # крестик