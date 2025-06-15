import allure
from pages.base_page import BasePage
from urls import Urls
from locators.forgot_password_page_locators import ForgotPasswordPageLocators as FPPL




class ForgotPasswordPage(BasePage):

    @allure.step('Открыть страницу "Восстановить пароль"')
    def open_forgot_password_page(self):
        self.open_page(Urls.URL_FORGOT_PASSWORD_PAGE)


    @allure.step('Заполнить поле "email" на странице "Восстановить пароль"')
    def fill_email_field(self, email):
        self.click_to_element_by_script(FPPL.INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR)
        self.set_text_in_element(locator=FPPL.INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR, text=email)


    @allure.step('Заполнить поле "Пароль" на странице "Восстановление пароля"')
    def fill_password_field(self, password):
        self.click_to_element_by_script(FPPL.INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        self.set_text_in_element(locator=FPPL.INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR, text=password)


    @allure.step('Нажать кнопку "Восстановить" на странице "Восстановить пароль" и '
                 'дождаться появления страницы "Восстановление пароля"')
    def click_recovery_button(self):
        self.click_to_element_by_script(FPPL.BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR)
        self.wait_for_clickable_element(FPPL.INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)


    @allure.step('Нажать конку скрыть/показать пароль на странице "Восстановление пароля"')
    def click_show_hide_icon(self):
        self.click_to_element_by_script(FPPL.ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)


    @allure.step('Получить класс поля "Пароль"')
    def get_password_field_class(self):
        return self.find_element(FPPL.FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR).get_attribute("class")


    @allure.step('Проверить активность поля "Пароль"')
    def is_password_field_enabled(self):
        return self.find_element(FPPL.FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR).is_enabled()


