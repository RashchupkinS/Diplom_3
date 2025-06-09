from selenium.webdriver.common.by import By




# Локаторы - "Войти в аккаунт"
class LoginPageLocators:
    # поле "Email"
    INPUT_EMAIL_LOGIN_PAGE_LOCATOR = By.XPATH, "//fieldset[1]//input"
    # поле "Пароль"
    INPUT_PASSWORD_LOGIN_PAGE_LOCATOR = By.XPATH, "//fieldset[2]//input"
    # кнопка "Войти"
    BUTTON_LOGIN_LOGIN_PAGE_LOCATOR = By.XPATH, ".//button[text()='Войти']"
    # кнопка "Восстановить пароль"
    BUTTON_RECOVER_PASSWORD_LOGIN_PAGE_LOCATOR = By.XPATH, ".//a[text()='Восстановить пароль']"





