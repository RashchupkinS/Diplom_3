import allure
from pages.base_page import BasePage
from urls import Urls
from locators.login_page_locators import LoginPageLocators as LPL




class LoginPage(BasePage):

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_page(Urls.URL_LOGIN_PAGE)


    @allure.step('Заполнить поле "email" на странице авторизации')
    def fill_email_field(self, email):
        self.click_to_element_by_script(LPL.INPUT_EMAIL_LOGIN_PAGE_LOCATOR)
        self.set_text_in_element(locator=LPL.INPUT_EMAIL_LOGIN_PAGE_LOCATOR, text=email)


    @allure.step('Заполнить поле "Пароль" на странице авторизации')
    def fill_password_field(self, password):
        self.click_to_element_by_script(LPL.INPUT_PASSWORD_LOGIN_PAGE_LOCATOR)
        self.set_text_in_element(locator=LPL.INPUT_PASSWORD_LOGIN_PAGE_LOCATOR, text=password)


    @allure.step('Кликнуть кнопку "Войти" на странице авторизации')
    def click_login_button(self):
        self.click_to_element_by_script(LPL.BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)


    @allure.step('Кликнуть кнопку "Восстановить пароль" на странице авторизации')
    def click_recovery_password_button(self):
        self.click_to_element_by_script(LPL.BUTTON_RECOVER_PASSWORD_LOGIN_PAGE_LOCATOR)


    @allure.step('Заполнить поле "email", "Пароль" и кликнуть кнопку "Войти" на странице авторизации')
    def fill_authorize_form_and_click_enter(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_login_button()
        self.wait_for_constructor_page()


