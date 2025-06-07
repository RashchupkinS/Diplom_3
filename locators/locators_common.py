from selenium.webdriver.common.by import By




class TestLocators:

# Локаторы раздела - "Регистрация"
    # поле "Имя"
    INPUT_NAME_LOCATOR = By.XPATH, "//fieldset[1]//input"
    # поле "Email"
    INPUT_EMAIL_LOCATOR = By.XPATH, "//fieldset[2]//input"
    # поле "Пароль"
    INPUT_PASSWORD_LOCATOR = By.XPATH, "//fieldset[3]//input"
    # кнопка "Зарегистрироваться"
    BUTTON_REGISTRATION_LOCATOR = By.XPATH, "//button[contains(@class, 'button_type_primary')]"
    # ошибка "Некорректный пароль"
    ERROR_INCORRECT_PASSWORD_LOCATOR = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"
    # кнопка "Войти"
    BUTTON_LOGIN_LOCATOR = By.XPATH, ".//button[text()='Войти']"

# Локаторы - "Войти в аккаунт"
    # кнопка "Войти в аккаунт" на главной страницу
    BUTTON_LOGIN_ACCOUNT_MAIN_PAGE_LOCATOR = By.XPATH, "//button[text()='Войти в аккаунт']"

    # ссылка "Войти" на странице регистрации
    LINK_LOGIN_ACCOUNT_REGISTRATION_PAGE_LOCATOR = By.XPATH, "//a[text()='Войти']"
    # ссылка "Войти" на странице восстановления пароля
    LINK_LOGIN_ACCOUNT_FORGOT_PASSWORD_PAGE_LOCATOR = By.XPATH, "//a[text()='Войти']"

# Локаторы раздела - "Вход"
    # поле "Email"
    INPUT_EMAIL_LOGIN_PAGE_LOCATOR = By.XPATH, "//fieldset[1]//input"
    # поле "Пароль"
    INPUT_PASSWORD_LOGIN_PAGE_LOCATOR = By.XPATH, "//fieldset[2]//input"
    # кнопка "Войти"
    BUTTON_LOGIN_LOGIN_PAGE_LOCATOR = By.XPATH, ".//button[text()='Войти']"

# Локаторы раздела - "Личный Кабинет"
    # поле "Email"
    EMAIL_PERSONAL_ACCOUNT_PAGE_LOCATOR = By.XPATH, "//li[2]//input"
    # кнопка "Выход"
    BUTTON_EXIT_ACCOUNT_PAGE_LOCATOR = By.XPATH, "//button[text()='Выход']"
    # ссылка "Конструктор" в хедере
    PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR = By.XPATH, "//p[text()='Конструктор']"

# Локаторы раздела - "Конструктор"
    # локатор раздела "Конструктор" - Булки
    BREAD_LOCATOR = By.XPATH, "//span[text()='Булки']"
    # локатор раздела "Конструктор" - Соусы
    SAUCES_LOCATOR = By.XPATH, "//span[text()='Соусы']"
    # локатор раздела "Конструктор" - Начинки
    FILLINGS_LOCATOR = By.XPATH, "//span[text()='Начинки']"
    # локатор раздела "Конструктор" - выбранный раздел помечен tab_tab_type_current
    CURRENT_TAB_CONSTRUCTOR_LOCATOR = By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"
    # кнопка "Оформить заказ"
    BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//button[text()='Оформить заказ']"

# Локаторы в хедере
    # локатор Stellar Burgers
    LOGO_STELLAR_BURGERS_HEADER_LOCATOR = By.XPATH, "//div[contains(@class, 'header__logo')]"