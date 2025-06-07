import allure

from locators.constructor_page_locators import HEADER_ASSEMBLE_BURGER_CONSTRUCTOR_PAGE_LOCATOR, \
    INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR, INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR, \
    ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR, MODAL_WINDOW_CLOSED_CONSTRUCTOR_PAGE_LOCATOR
from locators.feed_of_orders_page_locators import HEADER_FEED_OF_ORDERS_PAGE_LOCATOR
from urls import Urls
from pages.base_page import BasePage
from locators.main_page_locators import PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR, PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR


# Проверка основного функционала
#     -переход по клику на «Конструктор»,
#     -переход по клику на «Лента заказов»,
#     -если кликнуть на ингредиент, появится всплывающее окно с деталями,
#     -всплывающее окно закрывается кликом по крестику,
#     -при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
#     -залогиненный пользователь может оформить заказ.


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
        assert modal_window.text == "Детали ингредиента", "Не произведён переход на страницу 'Лента заказов'"


# проверка: всплывающее окно закрывается кликом по крестику
    allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_window_with_ingredient_details_by_click_to_cross(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_MAIN_PAGE)
        page.click_to_element(INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR)
        page.wait_for_visible_element(INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        page.click_to_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)

        page.click_to_element(INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR)
        page.wait_for_visible_element(INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        page.click_to_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)

        modal_window_close = page.find_element(MODAL_WINDOW_CLOSED_CONSTRUCTOR_PAGE_LOCATOR)
        assert modal_window_close.is_displayed()


