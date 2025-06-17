import pytest
from selenium import webdriver
from urls import Urls
from helper import Generator
import requests
import allure




# фикстура запускает браузеры Chrome, Firefox и закрывает их завершению теста
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()


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


