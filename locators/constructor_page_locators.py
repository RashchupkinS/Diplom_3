from selenium.webdriver.common.by import By




class ConstructorPageLocators:
# Кнопки в хедере
    # ссылка "Личный кабинет" в хедере
    BUTTON_PERSONAL_ACCOUNT_IN_HEADER_LOCATOR = By.XPATH, '//*[@id="root"]/div/header//p[contains(text(), "Личный Кабинет")]'
    # ссылка "Лента заказов" в хедере
    BUTTON_FEED_OF_ORDERS_IN_HEADER_LOCATOR = By.XPATH, '//*[@id="root"]/div/header//p[contains(text(), "Лента Заказов")]'
    # ссылка "Конструктор" в хедере
    BUTTON_CONSTRUCTOR_IN_HEADER_LOCATOR = By.XPATH, '//*[@id="root"]/div/header//p[contains(text(), "Конструктор")]'

# Заголовки, кнопки, элементы страницы "Конструктор"
    # заголовок "Соберите бургер"
    HEADER_ASSEMBLE_BURGER_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//h1[text()='Соберите бургер']"
    # кнопка "Оформить заказ"
    BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, ".//button[text()='Оформить заказ']"
    # ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_R2_D3_BUN_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']/ancestor::a//p"
    # счётчик ингредиента "Флюоресцентная булка R2-D3"
    INGREDIENT_COUNTER_R2_D3_BUN_CONSTRUCTOR_PAGE_LOCATOR = (By.XPATH,
                "//img[@alt='Флюоресцентная булка R2-D3']/ancestor::a//p[contains(@class, 'counter_counter__num__')]")
    # корзина для создания бургера
    BURGER_BASKET_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7'
    # ингредиент "Флюоресцентная булка R2-D3" в корзине бургера
    INGREDIENT_R2_D3_BUN_IN_BASKET_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, '//span[text()="Флюоресцентная булка R2-D3 (верх)"]'

# Элементы отображаемые в модальном окне
    # модальное окно открыто
    MODAL_WINDOW_OPENED_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4"
    # модальное окно закрыто
    MODAL_WINDOW_CLOSED_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, "section.Modal_modal__P3_V5"
    # иконка "крестик" модального окна "Детали ингредиента
    ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR = (By.XPATH,
                "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    # заголовок "Детали ингредиента" в модальном окне
    HEADER_INGREDIENT_DETAILS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR = (By.XPATH,
                                    "//h2[contains(@class, 'Modal_modal__title') and text()='Детали ингредиента']")
    # заголовок "идентификатор заказа" в модальном окне
    HEADER_ORDER_ID_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//p[contains(text(), 'идентификатор заказа')]"
    # номер заказа в модальном окне
    HEADER_NUMBER_OF_ORDER_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR = (By.CSS_SELECTOR,
                    "h2.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")


