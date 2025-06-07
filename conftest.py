import pytest
from data import *
from locators import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




# фикструра запускает браузер Chrome и закрывает по завершению теста
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# фикстура открывает заданную страницу и проверяет, что страница открыта по доступности поля "Имя"
@pytest.fixture(scope='function')
def open_page(driver):
    def _open(url):
        driver.get(url)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(TestLocators.PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        )
    return _open


# фикстура вводит данные авторизованного пользователя,
# переходит в "Личный кабинет" и проверяет, что вход в кабинет осуществлен
@pytest.fixture(scope='function')
def login_registered_user(driver):
    def _login(email, password):
        # очистка поля и ввод "Email"
        driver.find_element(*TestLocators.INPUT_EMAIL_LOGIN_PAGE_LOCATOR).clear()
        driver.find_element(*TestLocators.INPUT_EMAIL_LOGIN_PAGE_LOCATOR).send_keys(email)
        # очистка поля и ввод "Пароля"
        driver.find_element(*TestLocators.INPUT_PASSWORD_LOGIN_PAGE_LOCATOR).clear()
        driver.find_element(*TestLocators.INPUT_PASSWORD_LOGIN_PAGE_LOCATOR).send_keys(password)
        # клик по кнопке "Войти"
        driver.find_element(*TestLocators.BUTTON_LOGIN_LOGIN_PAGE_LOCATOR).click()
        # переход в Личный кабинет
        driver.find_element(*TestLocators.PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR).click()
        # ожидание, чтобы убедится что страница "Личный кабинет" загружена
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.EMAIL_PERSONAL_ACCOUNT_PAGE_LOCATOR)
        )
    return _login


# фикструра для генерации регистрационных данных
@pytest.fixture
def registration_data():
    generator = GenerateRegistrationData()
    return generator.generate_data()