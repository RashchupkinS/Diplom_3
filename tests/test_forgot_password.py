import allure
from data import email_for_test, password_for_test
from pages.base_page import BasePage
from urls import Urls
from locators.login_page_locators import BUTTON_RECOVER_PASSWORD_LOGIN_PAGE_LOCATOR
from locators.forgot_password_page_locators import BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR, \
    INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR
from locators.reset_password_page_locators import (BUTTON_SAVE_RESET_PASSWORD_PAGE_LOCATOR,
                                                   ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR,
                                                   INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR,
                                                   FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)




class TestForgotPassword:

# проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль»
    allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_transition_to_recover_password_page_by_button_recover_password(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_LOGIN_PAGE)
        page.click_to_element(BUTTON_RECOVER_PASSWORD_LOGIN_PAGE_LOCATOR)
        page.wait_for_clickable_element(BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR)
        assert Urls.URL_FORGOT_PASSWORD_PAGE == driver.current_url, "Нет перехода на страницу «Восстановить пароль»"


# проверка: ввод почты и клик по кнопке «Восстановить»
    allure.title("Переход на страницу восстановления пароля после ввода почты и клика по кнопке «Восстановить»")
    def test_enter_email_and_click_button_recover(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_FORGOT_PASSWORD_PAGE)
        page.click_to_element(INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR)
        page.set_text(locator=INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR, text=email_for_test)
        page.click_to_element(BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR)
        page.wait_for_clickable_element(BUTTON_SAVE_RESET_PASSWORD_PAGE_LOCATOR)
        actual_url = page.get_current_url()
        assert actual_url == Urls.URL_RESET_PASSWORD_PAGE, "Нет перехода на страницу «Сбросить пароль»"


# проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
    allure.title("Клик по кнопке показать/скрыть пароль делает поле ввода пароля активным, подсвечивает его")
    def test_click_by_icon_show_hide_password(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_FORGOT_PASSWORD_PAGE)
        # ввод email и переход к странице сброса пароля
        page.click_to_element(INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR)
        page.set_text(locator=INPUT_EMAIL_FORGOT_PASSWORD_PAGE_LOCATOR, text=email_for_test)
        page.click_to_element(BUTTON_RECOVER_FORGOT_PASSWORD_PAGE_LOCATOR)
        # ввод нового пароля
        page.wait_for_clickable_element(BUTTON_SAVE_RESET_PASSWORD_PAGE_LOCATOR)
        page.click_to_element(INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        page.set_text(locator=INPUT_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR, text=password_for_test)
        # клик по иконке скрыть/показать пароль и проверка, что поле подсветилось и активно
        page.click_to_element(ICON_SHOW_HIDE_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        field_in_focus = page.find_element(FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        field_is_active = page.find_element(FIELD_PASSWORD_RESET_PASSWORD_PAGE_LOCATOR)
        assert "input__placeholder-focused" in field_in_focus.get_attribute("class"),"Поле не подсветилось после клика по иконке показать/скрыть пароль"
        assert field_is_active.is_enabled(), "Поле для ввода пароля не активно"


