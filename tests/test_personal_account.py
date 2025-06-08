import allure
from pages.base_page import BasePage
from urls import Urls
from locators.main_page_locators import PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR
from locators.login_page_locators import (BUTTON_LOGIN_LOGIN_PAGE_LOCATOR,
                                          INPUT_EMAIL_LOGIN_PAGE_LOCATOR,
                                          INPUT_PASSWORD_LOGIN_PAGE_LOCATOR)
from locators.personal_account_page_locators import (BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR,
                                                     BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR)
from data import email_for_test, password_for_test




class TestPersonalAccount:

# проверка: переход по клику на «Личный кабинет»
    allure.title("Переход по клику на «Личный кабинет» в хедере на главной странице")
    def test_transition_to_login_page_by_button_personal_account_from_main_page(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_MAIN_PAGE)
        page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        page.wait_for_clickable_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        actual_url = page.get_current_url()
        assert actual_url == Urls.URL_LOGIN_PAGE, "Нет перехода на страницу «Войти в аккаунт»"


# проверка: переход в раздел «История заказов»
    allure.title("Переход в раздел «История заказов» по клику кнопки 'История заказов' в личном кабинете")
    def test_transition_from_personal_account_to_orders_history(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_LOGIN_PAGE)
        page.wait_for_clickable_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        page.click_to_element(INPUT_EMAIL_LOGIN_PAGE_LOCATOR)
        page.set_text(locator=INPUT_EMAIL_LOGIN_PAGE_LOCATOR, text=email_for_test)
        page.click_to_element(INPUT_PASSWORD_LOGIN_PAGE_LOCATOR)
        page.set_text(locator=INPUT_PASSWORD_LOGIN_PAGE_LOCATOR, text=password_for_test)
        page.click_to_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        page.wait_for_clickable_element(BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR)
        page.click_to_element(BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR)
        actual_url = page.get_current_url()
        assert actual_url == Urls.URL_ORDERS_HISTORY_PAGE, ("Не произведён выход со страницы "
                                                            "'Личный кабинет' на страницу 'История заказов'")


# проверка: выход по кнопке «Выйти» в личном кабинете
    allure.title("Выход по кнопке «Выйти» в личном кабинете и переход на страницу авторизации")
    def test_logout_from_account(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_MAIN_PAGE)
        page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        page.wait_for_clickable_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        page.click_to_element(INPUT_EMAIL_LOGIN_PAGE_LOCATOR)
        page.set_text(locator=INPUT_EMAIL_LOGIN_PAGE_LOCATOR, text=email_for_test)
        page.click_to_element(INPUT_PASSWORD_LOGIN_PAGE_LOCATOR)
        page.set_text(locator=INPUT_PASSWORD_LOGIN_PAGE_LOCATOR, text=password_for_test)
        page.click_to_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        page.wait_for_clickable_element(BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR)
        page.click_to_element(BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR)
        page.wait_for_clickable_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        actual_url = page.get_current_url()
        assert actual_url == Urls.URL_LOGIN_PAGE, "Не произведён выход со страницы 'Личный кабинет'"


