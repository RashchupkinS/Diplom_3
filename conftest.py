import pytest
from selenium import webdriver




# фикстура запускает браузер Chrome и закрывает по завершению теста
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


