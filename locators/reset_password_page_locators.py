from selenium.webdriver.common.by import By




# Локаторы раздела - "Сбросить пароль"
# поле "Пароль"
FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, "//label[contains(@class, 'input__placeholder') and text()='Пароль']"
# поле ввода пароля
INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.NAME, "Введите новый пароль"
# кнопка "Сохранить"
BUTTON_SAVE_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, ".//button[text()='Сохранить']"
# иконка "Скрыть/Показать пароль"
ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR = By.XPATH, "//div[contains(@class, 'input__icon-action')]"