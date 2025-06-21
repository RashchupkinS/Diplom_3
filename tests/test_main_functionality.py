import allure
from data import CheckData
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from urls import Urls




class TestMainFunctionality:

    # проверка: переход по клику на «Конструктор»
    @allure.title('Переход на страницу "Конструктор" по клику на кнопку «Конструктор» в хедере')
    def test_transition_from_login_page_to_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_button_constructor_in_header()
        current_url = login_page.get_current_url()
        with allure.step('Сравнить url открывшейся страницы с ожидаемым'):
            assert current_url == Urls.URL_MAIN_PAGE, (f"Ожидалась страница '{Urls.URL_MAIN_PAGE}', "
                                                        f"получена страница '{current_url}'")


    # проверка: переход по клику на «Лента заказов»
    @allure.title('Переход на страницу «Лента заказов» по клику кнопки "Лента заказов" в хедере')
    def test_transition_from_constructor_to_feed_of_orders(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_button_feed_of_orders_in_header()
        current_url = constructor_page.get_current_url()
        with allure.step('Сравнить url открывшейся страницы с ожидаемым'):
            assert current_url == Urls.URL_FEED_OF_ORDERS_PAGE, (f"Ожидалась страница '{Urls.URL_FEED_OF_ORDERS_PAGE}', "
                                                        f"получена страница '{current_url}'")


    # проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями
    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_window_with_ingredient_details(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_on_r2_d3_bun()
        ingredient_title = constructor_page.get_title_ingredient_details()
        with allure.step('Проверить открытие окна и соответствие заголовка ожидаемому'):
            assert constructor_page.is_displayed_opened_modal_window() , "Окно не открылось"
            assert ingredient_title == CheckData.INGREDIENTS_WINDOW_TITLE, \
                                                            (f"Ожидался заголовок '{CheckData.INGREDIENTS_WINDOW_TITLE}', "
                                                            f"получен заголовок '{ingredient_title}'")


    # проверка: всплывающее окно закрывается кликом по крестику
    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_window_with_ingredient_details_by_clicking_on_cross(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_on_r2_d3_bun()
        constructor_page.click_on_cross_in_ingredients_window()
        constructor_page_title = constructor_page.get_title_header_assemble_burger()
        with allure.step('Проверить закрытие окна и соответствие заголовка ожидаемому'):
            assert constructor_page.is_displayed_closed_modal_window(), "Окно не закрылось"
            assert constructor_page_title == CheckData.HEADER_ASSEMBLE_BURGER, \
                                                            (f"Ожидался заголовок '{CheckData.HEADER_ASSEMBLE_BURGER}', "
                                                            f"получен заголовок '{constructor_page_title}'")



    # проверка: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
    @allure.title('При добавлении ингредиента в корзину, увеличивается счётчик данного ингредиента')
    def test_ingredient_counter_increases_when_ingredient_is_added_to_basket(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        counter_ingredient_before_add = constructor_page.get_ingredient_r2_d3_counter_value()
        constructor_page.drag_and_drop_r2_d3_bun_to_burger()
        ingredient_in_burger_title = constructor_page.get_title_ingredient_r2_d3_in_basket()
        counter_ingredient_after_add = constructor_page.get_ingredient_r2_d3_counter_value()
        with allure.step('Проверить добавление нужного ингредиента в корзину и увеличение счётчика ингредиента'):
            assert ingredient_in_burger_title == CheckData.BUN_R2_D3_IN_BURGER, \
                                                                (f"Ожидался заголовок '{CheckData.BUN_R2_D3_IN_BURGER}', "
                                                                f"получен заголовок '{ingredient_in_burger_title}'")
            assert counter_ingredient_after_add > counter_ingredient_before_add


    # проверка: залогиненный пользователь может оформить заказ
    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_logged_user_can_place_an_order(self, driver, registered_user_data):
        email, password = registered_user_data
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        login_page.click_button_constructor_in_header()
        constructor_page = ConstructorPage(driver)
        constructor_page.drag_and_drop_r2_d3_bun_to_burger()
        constructor_page.click_on_create_order_button()
        order_window_title = constructor_page.get_title_id_order()
        with allure.step('Проверить открытие окна и соответствие заголовка ожидаемому'):
            assert constructor_page.is_displayed_opened_modal_window(), "Окно не открылось"
            assert order_window_title == CheckData.HEADER_ID_ORDER_TITLE,  \
                                                                (f"Ожидался заголовок '{CheckData.HEADER_ID_ORDER_TITLE}', "
                                                                f"получен заголовок '{order_window_title}'")



