import allure
from data import CheckData
from urls import Urls
from helper import Generator




class TestForgotPassword:

    # проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль»
    allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль" на странице "Авторизации"')
    def test_transition_to_forgot_password_page_by_button_recover_password(self, login_page):
        login_page.open_login_page()
        login_page.click_recovery_password_button()
        current_url = login_page.get_current_url()
        assert current_url == Urls.URL_FORGOT_PASSWORD_PAGE, (f"Ожидалась страница '{Urls.URL_FORGOT_PASSWORD_PAGE}', "
                                                              f"получена страница '{current_url}'")


    # проверка: ввод почты и клик по кнопке «Восстановить»
    allure.title('Переход на страницу восстановления пароля после ввода почты и клика '
                 'по кнопке "Восстановить" на странице "Восстановить пароль"')
    def test_transition_to_reset_password_page_by_enter_email_and_click_on_button_recover(self, forgot_password_page):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(Generator.random_user_data()["email"])
        forgot_password_page.click_recovery_button()
        forgot_password_page.wait_for_password_field()
        current_url = forgot_password_page.get_current_url()
        assert current_url == Urls.URL_RESET_PASSWORD_PAGE, (f"Ожидалась страница '{Urls.URL_RESET_PASSWORD_PAGE}', "
                                                             f"получена страница '{current_url}'")


    # проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
    allure.title('Клик по кнопке показать/скрыть пароль делает поле ввода пароля активным, подсвечивает его')
    def test_click_on_icon_on_reset_password_page_makes_field_active(self, forgot_password_page):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(Generator.random_user_data()["email"])
        forgot_password_page.click_recovery_button()
        forgot_password_page.wait_for_password_field()
        forgot_password_page.fill_password_field(Generator.random_user_data()["password"])
        forgot_password_page.click_show_hide_icon()
        field_class = forgot_password_page.get_password_field_class()
        assert CheckData.FIELD_IN_FOCUS_CONTAINS_ATTRIBUTE in field_class, (f"Ожидалась подсветка поля 'Пароль' "
                                        f"в фокусе после клика по иконке показать/скрыть пароль, поле не в фокусе")
        assert forgot_password_page.is_password_field_enabled(), "Поле ввода пароля не активно"


