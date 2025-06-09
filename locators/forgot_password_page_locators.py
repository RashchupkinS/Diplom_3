from selenium.webdriver.common.by import By




# Локаторы раздела - "Восстановление пароля"
class ForgotPasswordPageLocators:
    # поле "Email"
    INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR = By.XPATH, "//input[@type='text' and contains(@class, 'input__textfield')]"
    # кнопка "Восстановить"
    BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR = By.XPATH, ".//button[text()='Восстановить']"



    # Локаторы раздела - "Сбросить пароль"
    # поле "Пароль"
    FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, "//label[contains(@class, 'input__placeholder') and text()='Пароль']"
    # поле ввода пароля
    INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.NAME, "Введите новый пароль"
 #   INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, ".//input[@type='password']"
    # кнопка "Сохранить"
    BUTTON_SAVE_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, ".//button[text()='Сохранить']"
    # иконка "Скрыть/Показать пароль"
    ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.CSS_SELECTOR, ".input__icon svg"