import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from urls import Urls





# # фикстура запускает браузер Chrome и закрывает по завершению теста
# @pytest.fixture(scope='function')
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


# фикстура запускает браузер Chrome и закрывает по завершению теста
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#         driver.set_window_size(1920, 1080)
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#         driver.set_window_size(1920, 1080)
#     yield driver
#     driver.quit()


# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#     HEADLESS = False  # Меняй на True, если нужен headless
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
#         driver.set_window_size(1920, 1080)
#
#     yield driver
#     driver.quit()


@pytest.fixture(scope='function')
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture(scope='function')
def forgot_password_page(driver):
    page = ForgotPasswordPage(driver)
    return page
