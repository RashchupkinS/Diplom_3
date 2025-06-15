import allure
from data import CheckData, counter_parameters
import pytest




class TestFeedOfOrders:

    # проверка: если кликнуть на заказ, откроется всплывающее окно с деталями
    @allure.title('Если кликнуть на заказ в ленте заказов, откроется всплывающее окно с деталями')
    def test_click_on_order_open_popup_window_with_details(self, feed_of_orders_page):
        feed_of_orders_page.open_feed_of_orders_page()
        feed_of_orders_page.click_on_order()
        order_details_title = feed_of_orders_page.get_title_order_details()
        with allure.step('Проверить открытие окна и соответствие заголовка ожидаемому'):
            assert feed_of_orders_page.is_displayed_opened_modal_window, "Окно не закрылось"
            assert order_details_title == CheckData.HEADER_ORDER_DETAIL_TITLE,  \
                                                                (f"Ожидался заголовок '{CheckData.HEADER_ORDER_DETAIL_TITLE}', "
                                                                f"получен заголовок '{order_details_title}'")


    # проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_users_orders_displayed_in_order_history_and_on_order_feed_pages(self, login_page, constructor_page,
                                                    feed_of_orders_page, personal_account_page, registered_user_data):
        email, password = registered_user_data
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        constructor_page.drag_and_drop_r2_d3_bun_to_burger()
        constructor_page.click_on_create_order_button()
        constructor_page.click_on_cross_in_ingredients_window()
        constructor_page.click_button_personal_account_in_header_authorized_user()
        personal_account_page.click_orders_history_button()
        personal_account_page.wait_for_visible_feed_with_orders()
        order_number = personal_account_page.get_last_order_number()
        personal_account_page.click_button_feed_of_orders_in_header()
        orders_in_feed = feed_of_orders_page.get_order_numbers_in_feed_of_orders()
        with allure.step('Проверить, что номер созданного заказа есть в ленте заказов'):
            assert order_number in orders_in_feed, 'Новый заказ не отображается на странице "Лента заказов"'


    @pytest.mark.parametrize("counter_locator, counter_name", counter_parameters)
    @allure.title('При создании нового заказа счётчик "{counter_name}" увеличивается')
    def test_counter_increases_after_created_new_order(self, feed_of_orders_page, login_page, constructor_page,
                                                       registered_user_data, counter_locator, counter_name):
        email, password = registered_user_data
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        login_page.click_button_feed_of_orders_in_header()
        counter_before = feed_of_orders_page.get_counter_by_locator(counter_locator)
        constructor_page.click_button_constructor_in_header()
        constructor_page.drag_and_drop_r2_d3_bun_to_burger()
        constructor_page.click_on_create_order_button()
        constructor_page.click_on_cross_in_ingredients_window()
        constructor_page.click_button_feed_of_orders_in_header()
        feed_of_orders_page.refresh_feed_of_orders_page_and_wait()
        counter_after = feed_of_orders_page.get_counter_by_locator(counter_locator)
        with allure.step('Сравнить значения счётчиков ДО и ПОСЛЕ оформления заказа, счётчик ПОСЛЕ должен увеличиться'):
            assert counter_before < counter_after, "Счётчик {counter_name} не увеличился после создания нового заказа"


    # проверка: после оформления заказа его номер появляется в разделе В работе
    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_after_placing_order_its_number_appears_in_progress_section(self, feed_of_orders_page, login_page,
                                                                        constructor_page, registered_user_data):
        email, password = registered_user_data
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        constructor_page.drag_and_drop_r2_d3_bun_to_burger()
        constructor_page.click_on_create_order_button()
        number_of_order = constructor_page.get_number_of_order()
        constructor_page.click_on_cross_in_ingredients_window()
        constructor_page.click_button_feed_of_orders_in_header()
        feed_of_orders_page.refresh_feed_of_orders_page_and_wait()
        orders_in_progress_list = feed_of_orders_page.get_all_orders_number_in_progress_list()
        with allure.step('Проверить, что новый заказ появляется в разделе "В работе"'):
            assert number_of_order in orders_in_progress_list, 'Новый заказ не отображается в разделе "В работе"'


