from locators.feed_of_orders_page_locators import FeedOfOrdersPageLocators as FOOL



# класс содержит сверяемые данные для тестов
class CheckData:
    FIELD_IN_FOCUS_CONTAINS_ATTRIBUTE = "input__placeholder-focused"
    INGREDIENTS_WINDOW_TITLE = "Детали ингредиента"
    HEADER_ASSEMBLE_BURGER = "Соберите бургер"
    BUN_R2_D3_IN_BURGER = "Флюоресцентная булка R2-D3 (верх)"
    HEADER_ID_ORDER_TITLE = "идентификатор заказа"
    HEADER_ORDER_DETAIL_TITLE = "Cостав"


# параметры теста test_counter_increases_after_created_new_order
counter_parameters = [
    (FOOL.TOTAL_ORDERS_FOR_ALL_TIME_COUNTER_FEED_OF_ORDERS_PAGE_LOCATOR, "Выполнено за всё время"),
    (FOOL.TOTAL_ORDERS_FOR_TODAY_COUNTER_FEED_OF_ORDERS_PAGE_LOCATOR, "Выполнено за сегодня"),
]


