from selenium.webdriver.common.by import By




# Локаторы раздела - "Восстановление пароля"
# поле "Email"
INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR = By.XPATH, "//input[@type='text' and contains(@class, 'input__textfield')]"
# кнопка "Восстановить"
BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR = By.XPATH, ".//button[text()='Восстановить']"


