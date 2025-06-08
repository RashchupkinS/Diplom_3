from selenium.webdriver.common.by import By




# ссылка "Личный кабинет" в хедере
PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR = By.XPATH, "//p[text()='Личный Кабинет']"
# ссылка "Лента заказов" в хедере
PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR = By.XPATH, "//p[text()='Лента Заказов']"
# ссылка "Конструктор" в хедере
PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR = By.XPATH, "//p[text()='Конструктор']"


MODAL_WINDOW_OPENED_NUMBER_OF_ORDER = By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]"




