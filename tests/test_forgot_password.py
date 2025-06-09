import allure


from data import email_for_test, password_for_test

from urls import Urls
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from locators.login_page_locators import LoginPageLocators as LPL
from locators.forgot_password_page_locators import ForgotPasswordPageLocators as FPPL



import os
import time


class TestForgotPassword:

    # проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль»
    allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_transition_to_recover_password_page_by_button_recover_password(self, login_page):
        login_page.open_page(Urls.URL_LOGIN_PAGE)
        login_page.click_to_element(LPL.BUTTON_RECOVER_PASSWORD_LOGIN_PAGE_LOCATOR)
        login_page.wait_for_clickable_element(FPPL.BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR)
        current_url = login_page.get_current_url()
        assert current_url == Urls.URL_FORGOT_PASSWORD_PAGE, "Нет перехода на страницу «Восстановить пароль»"


    # проверка: ввод почты и клик по кнопке «Восстановить»
    allure.title("Переход на страницу восстановления пароля после ввода почты и клика по кнопке «Восстановить»")
    def test_transition_to_recover_password_page_by_enter_email_and_click_on_button_recover(self, forgot_password_page):
        forgot_password_page.open_page(Urls.URL_FORGOT_PASSWORD_PAGE)
        forgot_password_page.click_to_element(FPPL.INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR)
        forgot_password_page.set_text(locator=FPPL.INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR, text=email_for_test)
        forgot_password_page.click_to_element(FPPL.BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR)
        forgot_password_page.wait_for_clickable_element(FPPL.BUTTON_SAVE_RESET_PASSWORD_PAGE_LOCATOR)
        current_url = forgot_password_page.get_current_url()
        assert current_url == Urls.URL_RESET_PASSWORD_PAGE, "Нет перехода на страницу «Сбросить пароль»"


    # проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
    allure.title("Клик по кнопке показать/скрыть пароль делает поле ввода пароля активным, подсвечивает его")
    def test_click_on_icon_in_reset_password_window_show_or_hide_password(self, forgot_password_page):
        forgot_password_page.open_page(Urls.URL_FORGOT_PASSWORD_PAGE)
        # ввод email и переход к странице сброса пароля
        forgot_password_page.click_to_element_by_js(FPPL.INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR)
        forgot_password_page.set_text(locator=FPPL.INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR, text=email_for_test)
        forgot_password_page.click_to_element_by_js(FPPL.BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR)
        # ввод нового пароля
        forgot_password_page.click_to_element(FPPL.INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        forgot_password_page.set_text(locator=FPPL.INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR, text=password_for_test)
        # клик по иконке скрыть/показать пароль и проверка, что поле подсветилось и активно
        forgot_password_page.click_to_element(FPPL.ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        forgot_password_page.click_to_element(FPPL.ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        forgot_password_page.click_to_element(FPPL.ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        forgot_password_page.click_to_element(FPPL.ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        forgot_password_page.click_to_element(FPPL.ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        field_in_focus = forgot_password_page.find_element(FPPL.FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        field_is_active = forgot_password_page.find_element(FPPL.FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        assert "input__placeholder-focused" in field_in_focus.get_attribute("class"),"Поле не подсветилось после клика по иконке показать/скрыть пароль"
        assert field_is_active.is_enabled(), "Поле для ввода пароля не активно"


