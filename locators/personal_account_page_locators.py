from selenium.webdriver.common.by import By




# кнопка "Выход"
BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR = By.XPATH, "//button[text()='Выход']"
# кнопка "История заказов"
BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR = By.XPATH, "//a[text()='История заказов']"


ORDER_ITEMS = By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r.mb-6"

ORDER_HISTORY_SCROLL_CONTAINER = By.CSS_SELECTOR, "div.Account_contentBox__2CPm3"

ORDER_ID = By.XPATH, "//p[contains(@class, 'text_type_digits-default') and starts-with(text(), '#')]"

ORDER_ITEMS_IN_FEED_HISTORY_IN_PERSONAL_ACCOUNT_PAGE_LOCATOR = By.CLASS_NAME, "OrderHistory_link__1iNby"



