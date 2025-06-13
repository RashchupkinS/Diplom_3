from selenium.webdriver.common.by import By




class PersonalAccountPageLocators:
    # кнопка "Выход"
    BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR = By.XPATH, ".//button[text()='Выход']"
    # кнопка "История заказов"
    BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR = By.XPATH, "//a[text()='История заказов']"
    # список заказов в "Истории заказов"
    ORDER_ITEMS_IN_FEED_HISTORY_IN_PERSONAL_ACCOUNT_PAGE_LOCATOR = By.CLASS_NAME, "OrderHistory_link__1iNby"


