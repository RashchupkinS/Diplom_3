from selenium.webdriver.common.by import By




class ForgotPasswordPageLocators:
    # поле "Email"
    INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR = By.XPATH, "//input[@type='text' and contains(@class, 'input__textfield')]"
    # кнопка "Восстановить"
    BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR = By.XPATH, ".//button[text()='Восстановить']"
    # поле "Пароль"
    INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, "//input[@type='password']"
    # поле "Пароль", для проверки активности поля
    FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, "//label[contains(@class, 'input__placeholder') and text()='Пароль']"
    # кнопка "Сохранить"
    BUTTON_SAVE_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, ".//button[text()='Сохранить']"
    # иконка "скрыть/показать пароль"
    ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.CSS_SELECTOR, ".input__icon.input__icon-action"


