from selenium.webdriver.common.by import By




class LoginPageLocators:
    # поле "Email"
    INPUT_EMAIL_LOGIN_PAGE_LOCATOR = By.XPATH, "//input[@type='text' and contains(@class, 'input__textfield')]"
    # поле "Пароль"
    INPUT_PASSWORD_LOGIN_PAGE_LOCATOR = By.XPATH, "//input[@type='password' and contains(@class, 'input__textfield')]"
    # кнопка "Войти"
    BUTTON_LOGIN_LOGIN_PAGE_LOCATOR = By.XPATH, ".//button[text()='Войти']"
    # кнопка "Восстановить пароль"
    BUTTON_RECOVER_PASSWORD_LOGIN_PAGE_LOCATOR = By.XPATH, ".//a[text()='Восстановить пароль']"
    # заголовок "Вход"
    HEADER_LOGIN_LOGIN_PAGE_LOCATOR = By.XPATH, "//h2[text()='Вход']"


