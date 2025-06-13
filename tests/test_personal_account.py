import allure
from urls import Urls




class TestPersonalAccount:

    # проверка: переход по клику на «Личный кабинет»
    allure.title("Переход по клику на кнопку «Личный кабинет» в хедере на главной странице")
    def test_transition_to_login_page_by_button_personal_account_from_constructor_page(self, constructor_page, login_page):
        constructor_page.open_constructor_page()
        constructor_page.click_button_personal_account_in_header()
        login_page.wait_for_login_page()
        current_url = login_page.get_current_url()
        assert current_url == Urls.URL_LOGIN_PAGE, (f"Ожидалась страница '{Urls.URL_LOGIN_PAGE}', "
                                                    f"получена страница '{current_url}'")


    # проверка: переход в раздел «История заказов»
    allure.title("Переход на страницу «История заказов» по клику кнопки 'История заказов' в личном кабинете")
    def test_transition_to_orders_history_from_personal_account(self, login_page,
                                                                personal_account_page, registered_user_data):
        email, password = registered_user_data
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        personal_account_page.wait_for_constructor_page()
        personal_account_page.click_button_personal_account_in_header()
        personal_account_page.wait_for_button_orders_history()
        personal_account_page.click_orders_history_button()
        current_url = personal_account_page.get_current_url()
        assert current_url == Urls.URL_ORDERS_HISTORY_PAGE, (f"Ожидалась страница '{Urls.URL_ORDERS_HISTORY_PAGE}', "
                                                             f"получена страница '{current_url}'")


    # проверка: выход по кнопке «Выйти» в личном кабинете
    allure.title("Выход по кнопке «Выйти» в личном кабинете и переход на страницу авторизации")
    def test_logout_from_personal_account(self, login_page, personal_account_page, registered_user_data):
        email, password = registered_user_data
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        personal_account_page.wait_for_constructor_page()
        personal_account_page.click_button_personal_account_in_header()
        personal_account_page.click_exit_button()
        personal_account_page.wait_for_login_page()
        current_url = personal_account_page.get_current_url()
        assert current_url == Urls.URL_LOGIN_PAGE, (f"Ожидалась страница '{Urls.URL_LOGIN_PAGE}', "
                                                    f"получена страница '{current_url}'")


