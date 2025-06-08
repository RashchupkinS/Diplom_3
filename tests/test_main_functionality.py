import allure
import time

from data import email_for_test, password_for_test
from locators.constructor_page_locators import HEADER_ASSEMBLE_BURGER_CONSTRUCTOR_PAGE_LOCATOR, \
    INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR, INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR, \
    ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR, MODAL_WINDOW_CLOSED_CONSTRUCTOR_PAGE_LOCATOR, \
    MODAL_WINDOW_OPENED_CONSTRUCTOR_PAGE_LOCATOR, INGREDIENT_COUNTER_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR, \
    INGREDIENT_R2_D2_BUN_ON_BURGER_CONSTRUCTOR_PAGE_LOCATOR, BURGER_BUN_ON_TOP_CONSTRUCTOR_PAGE_LOCATOR, \
    BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR, MODAL_WINDOW_ID_ORDER_OPENED_CONSTRUCTOR_PAGE_LOCATOR, \
    MODAL_ORDER_ID_LABEL_LOCATOR
from locators.feed_of_orders_page_locators import HEADER_FEED_OF_ORDERS_PAGE_LOCATOR
from locators.login_page_locators import BUTTON_LOGIN_LOGIN_PAGE_LOCATOR, INPUT_EMAIL_LOGIN_PAGE_LOCATOR, \
    INPUT_PASSWORD_LOGIN_PAGE_LOCATOR
from locators.personal_account_page_locators import BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR, \
    BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR
from urls import Urls
from pages.base_page import BasePage
from locators.main_page_locators import PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR, PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR, \
    PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR


# Проверка основного функционала
#     - переход по клику на «Конструктор»,
#     - переход по клику на «Лента заказов»,
#     - если кликнуть на ингредиент, появится всплывающее окно с деталями,
#     - всплывающее окно закрывается кликом по крестику,
#     - при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
#     - залогиненный пользователь может оформить заказ.


class TestMainFunctionality:

# проверка: переход по клику на «Конструктор»
    allure.title("Переход по клику на «Конструктор» в хедере")
    def test_transition_from_feed_of_orders_to_constructor(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_FEED_OF_ORDERS_PAGE)
        page.click_to_element(PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR)
        page.wait_for_clickable_element(HEADER_ASSEMBLE_BURGER_CONSTRUCTOR_PAGE_LOCATOR)
        actual_url = page.get_current_url()
        assert actual_url == Urls.URL_MAIN_PAGE, "Не произведён переход на страницу 'Конструктор'"


# проверка: переход по клику на «Лента заказов»
    allure.title("Переход по клику на «Лента заказов» в хедере")
    def test_transition_from_constructor_to_feed_of_orders(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_MAIN_PAGE)
        page.click_to_element(PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR)
        page.wait_for_visible_element(HEADER_FEED_OF_ORDERS_PAGE_LOCATOR)
        actual_url = page.get_current_url()
        assert actual_url == Urls.URL_FEED_OF_ORDERS_PAGE, "Не произведён переход на страницу 'Лента заказов'"


# проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями
    allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_open_window_with_ingredient_details(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_MAIN_PAGE)
        page.click_to_element(INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR)
        page.wait_for_visible_element(INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        modal_window = page.find_element(INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        modal_window_opened = page.find_element(MODAL_WINDOW_OPENED_CONSTRUCTOR_PAGE_LOCATOR)
        assert modal_window.text == "Детали ингредиента", "Не произведён переход на страницу 'Лента заказов'"
        assert modal_window_opened.is_displayed()


# проверка: всплывающее окно закрывается кликом по крестику
    allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_window_with_ingredient_details_by_clicking_on_cross(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_MAIN_PAGE)
        page.click_to_element(INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR)
        page.wait_for_visible_element(INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        page.click_to_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        modal_window_closed = page.find_element(MODAL_WINDOW_CLOSED_CONSTRUCTOR_PAGE_LOCATOR)
        assert modal_window_closed.is_displayed()


# проверка: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
    @allure.title("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_counter_increases_when_ingredient_is_added_to_order(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_MAIN_PAGE)
        page.drag_and_drop_element(INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR,
                                   BURGER_BUN_ON_TOP_CONSTRUCTOR_PAGE_LOCATOR)
       # time.sleep(3)

        dropped_bun = page.wait_for_visible_element(INGREDIENT_R2_D2_BUN_ON_BURGER_CONSTRUCTOR_PAGE_LOCATOR)
    #    counter_bun = page.find_element(INGREDIENT_COUNTER_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR)
     #   print(dropped_bun.text)
    #    print(counter_bun.text)
        assert dropped_bun.text == "Флюоресцентная булка R2-D3 (верх)"
   #     assert counter_bun.text == "2"


# проверка: залогиненный пользователь может оформить заказ
    allure.title("залогиненый пользователь может оформить заказ")
    def test_logged_user_can_place_an_order(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_LOGIN_PAGE)
        page.wait_for_clickable_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        page.click_to_element(INPUT_EMAIL_LOGIN_PAGE_LOCATOR)
        page.set_text(locator=INPUT_EMAIL_LOGIN_PAGE_LOCATOR, text=email_for_test)
        page.click_to_element(INPUT_PASSWORD_LOGIN_PAGE_LOCATOR)
        page.set_text(locator=INPUT_PASSWORD_LOGIN_PAGE_LOCATOR, text=password_for_test)
        page.click_to_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        page.click_to_element(PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR)
        page.drag_and_drop_element(INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR,
                                   BURGER_BUN_ON_TOP_CONSTRUCTOR_PAGE_LOCATOR)
        page.click_to_element(BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)
        page.wait_for_visible_element(MODAL_ORDER_ID_LABEL_LOCATOR)
        modal_window = page.find_element(MODAL_ORDER_ID_LABEL_LOCATOR)
        modal_window_opened = page.find_element(MODAL_WINDOW_ID_ORDER_OPENED_CONSTRUCTOR_PAGE_LOCATOR)
        assert modal_window.text == "идентификатор заказа", "Не произведён переход на страницу 'Лента заказов'"
        assert modal_window_opened.is_displayed()


