from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    # ссылка "Личный кабинет" в хедере
    PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR = By.XPATH, "//p[text()='Личный Кабинет']"
    # ссылка "Лента заказов" в хедере
    PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR = By.XPATH, "//p[text()='Лента Заказов']"
    # ссылка "Конструктор" в хедере
    PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR = By.XPATH, "//p[text()='Конструктор']"

    MODAL_WINDOW_OPENED_NUMBER_OF_ORDER = By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]"

    OVERLAY_LOCATOR = By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr"

    # заголовок "Соберите бургер"
    HEADER_ASSEMBLE_BURGER_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//h1[text()='Соберите бургер']"

    # заголовок ""
    INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, "img[alt='Флюоресцентная булка R2-D3']"
    # INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, 'a[href="/ingredient/61c0c5a71d1f82001bdaaa6d"] p.counter_counter__num__3nue1'
    # счётчик ""
    # INGREDIENT_COUNTER_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, '//a[contains(@href, "61c0c5a71d1f82001bdaaa6d") and @draggable="true"]'

    INGREDIENT_COUNTER_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]"

    INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and text()='Детали ингредиента']"

    # иконка "крестик" модального окна "Детали ингредиента
    ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]"

    MODAL_WINDOW_CLOSED_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, "section.Modal_modal__P3_V5"

    MODAL_WINDOW_OPENED_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4"

    BURGER_BUN_ON_TOP_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7'

    # INGREDIENT_R2_D2_BUN_ON_BURGER_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//span[@class='constructor-element__text' and text()='Флюоресцентная булка R2-D3 (верх)']"

    # INGREDIENT_R2_D2_BUN_ON_BURGER_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_"

    INGREDIENT_R2_D2_BUN_ON_BURGER_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//span[contains(@class, 'constructor-element__text') and contains(text(), 'Флюоресцентная булка R2-D3 (верх)')]"

    BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//button[text()='Оформить заказ']"

    MODAL_WINDOW_ID_ORDER_OPENED_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, "div.Modal_modal__container__Wo2l_"

    MODAL_WINDOW_ID_ORDER_CLOSED_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, "section.Modal_modal__P3_V5"

    MODAL_ORDER_ID_LOCATOR = By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]"
    MODAL_ORDER_ID_LABEL_LOCATOR = By.XPATH, "//p[contains(text(), 'идентификатор заказа')]"
    MODAL_CLOSE_BUTTON_LOCATOR = By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS"




