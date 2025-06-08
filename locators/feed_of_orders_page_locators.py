from selenium.webdriver.common.by import By



# заголовок "Лента заказов" в хедере
HEADER_FEED_OF_ORDERS_PAGE_LOCATOR = By.XPATH, "//h1[text()='Лента заказов']"

ORDER_ITEMS_IN_LIST_FEED_OF_ORDERS_PAGE_LOCATOR = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")


ORDER_FEED_CONTAINER = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59")

# FEED_CONTAINER_LOCATOR = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59")
# FEED_ORDER_ITEM_LOCATOR = (By.XPATH, f".//*[contains(text(), '{order_number}')]")

ORDER_ITEMS_2 = By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r.mb-6"

TOTAL_ORDERS_FOR_ALL_TIME_COUNTER = By.XPATH, "//div[p[text()='Выполнено за все время:']]/p[contains(@class, 'OrderFeed_number')]"
TOTAL_ORDERS_FOR_TODAY_COUNTER = By.XPATH, "//div[p[text()='Выполнено за сегодня:']]/p[contains(@class, 'OrderFeed_number')]"


ORDERS_IN_PROGRESS = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'digits')]"

