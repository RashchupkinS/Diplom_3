import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.constructor_page import ConstructorPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.feed_of_orders_page import FeedOfOrdersPage
from urls import Urls
from helper import Generator
import requests
import allure




# фикстура запускает браузеры Chrome, Firefox и закрывает их завершению теста
# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#
#     HEADLESS = False  # *** ЕСЛИ НУЖЕН --headless поменять на True
#
#     if request.param == "chrome":
#         options = ChromeOptions()
#         options.add_argument("--window-size=1920,1080")
#         if HEADLESS:
#             options.add_argument("--headless=new")
#         driver = webdriver.Chrome(options=options)
#
#     elif request.param == "firefox":
#         options = FirefoxOptions()
#         if HEADLESS:
#             options.add_argument("--headless")
#         driver = webdriver.Firefox(options=options)
#         driver.set_window_size(width=1920, height=1080)
#
#     yield driver
#     driver.quit()

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
#        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
#        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()



# фикстура создаёт объект класса ConstructorPage
@pytest.fixture(scope='function')
def constructor_page(driver):
    return ConstructorPage(driver)


# фикстура создаёт объект класса LoginPage
@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)


# фикстура создаёт объект класса ForgotPasswordPage
@pytest.fixture(scope='function')
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


# фикстура создаёт объект класса PersonalAccountPage
@pytest.fixture(scope='function')
def personal_account_page(driver):
    return PersonalAccountPage(driver)


# фикстура создаёт объект класса FeedOfOrdersPage
@pytest.fixture(scope='function')
def feed_of_orders_page(driver):
    return FeedOfOrdersPage(driver)


# фикстура создаёт и регистрирует нового пользователя через API и удаляет его после теста
@pytest.fixture(scope='function')
def registered_user_data():
    payload = Generator.random_user_data()
    email = payload["email"]
    password = payload["password"]
    with allure.step("Создание пользователя через API"):
        response = requests.post(url=Urls.CREATE_USER, json=payload)
        if response.status_code == 200:
            access_token = response.json().get("access_token")
            yield email, password
            with allure.step("Удаление пользователя через API"):
                header = {'Authorization': access_token}
                requests.delete(Urls.DELETE_USER, headers=header)
        else:
            pytest.skip(f"Не удалось создать пользователя. Код ответа: {response.status_code}")


