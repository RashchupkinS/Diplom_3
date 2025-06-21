from selenium.webdriver.common.by import By




class FeedOfOrdersPageLocators:
    # заголовок "Лента заказов" в хедере
    HEADER_FEED_OF_ORDERS_PAGE_LOCATOR = By.XPATH, "//h1[text()='Лента заказов']"
    # выполнено заказов за ВСЁ ВРЕМЯ
    TOTAL_ORDERS_FOR_ALL_TIME_COUNTER_FEED_OF_ORDERS_PAGE_LOCATOR = (By.XPATH,
                                "//div[p[text()='Выполнено за все время:']]/p[contains(@class, 'OrderFeed_number')]")
    # выполнено заказов за СЕГОДНЯ
    TOTAL_ORDERS_FOR_TODAY_COUNTER_FEED_OF_ORDERS_PAGE_LOCATOR = (By.XPATH,
                                "//div[p[text()='Выполнено за сегодня:']]/p[contains(@class, 'OrderFeed_number')]")
    # заказы выполняются сейчас
    ORDERS_IN_PROGRESS_FEED_OF_ORDERS_PAGE_LOCATOR = (By.XPATH,
                                "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'digits')]")
    # заказ из ленты заказов
    ORDER_ITEMS_IN_LIST_FEED_OF_ORDERS_PAGE_LOCATOR = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
    # заголовок "Состав" в модальном окне по заказу из ленты заказов
    HEADER_ORDERS_DETAIL_MODAL_WINDOW_FEED_OF_ORDERS_PAGE_LOCATOR = By.XPATH, "//p[contains(text(), 'Cостав')]"
    # модальное окно открыто
    MODAL_WINDOW_OPENED_FEED_OF_ORDERS_PAGE_LOCATOR = By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4"
    # лента заказов
    ORDER_NUMBERS_IN_FEED_FEED_OF_ORDERS_PAGE_LOCATOR = By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r.mb-6"


