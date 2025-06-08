import allure
import time



from data import email_for_test, password_for_test
from locators.constructor_page_locators import (INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR,
                                                ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR,
                                                MODAL_WINDOW_OPENED_CONSTRUCTOR_PAGE_LOCATOR,
                                                BURGER_BUN_ON_TOP_CONSTRUCTOR_PAGE_LOCATOR,
                                                BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)

from locators.feed_of_orders_page_locators import ORDER_ITEMS_2, ORDER_ITEMS_IN_LIST_FEED_OF_ORDERS_PAGE_LOCATOR, \
    TOTAL_ORDERS_FOR_ALL_TIME_COUNTER, TOTAL_ORDERS_FOR_TODAY_COUNTER, ORDERS_IN_PROGRESS
from locators.login_page_locators import (BUTTON_LOGIN_LOGIN_PAGE_LOCATOR, INPUT_EMAIL_LOGIN_PAGE_LOCATOR,
                                          INPUT_PASSWORD_LOGIN_PAGE_LOCATOR)
from locators.personal_account_page_locators import (ORDER_ITEMS, BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR,
                                                     ORDER_HISTORY_SCROLL_CONTAINER)
from urls import Urls
from pages.base_page import BasePage
from locators.main_page_locators import PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR, PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR, \
    PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR, MODAL_WINDOW_OPENED_NUMBER_OF_ORDER


class TestFeedOfOrders:

# проверка: если кликнуть на заказ, откроется всплывающее окно с деталями
    allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_on_order_open_popup_window_with_details(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_FEED_OF_ORDERS_PAGE)
        page.click_to_element(ORDER_ITEMS_IN_LIST_FEED_OF_ORDERS_PAGE_LOCATOR)
        page.wait_for_visible_element(MODAL_WINDOW_OPENED_CONSTRUCTOR_PAGE_LOCATOR)
        modal_window_opened = page.find_element(MODAL_WINDOW_OPENED_CONSTRUCTOR_PAGE_LOCATOR)
        assert modal_window_opened.is_displayed()


# проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
    allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_users_orders_displayed_in_order_history_and_on_order_feed_pages(self, driver):
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
        time.sleep(5)
        page.wait_for_clickable_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        page.click_to_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        time.sleep(3)
        page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        time.sleep(2)
        page.click_to_element(BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR)
        time.sleep(2)

        # Получаем список заказов (без скроллинга)
        orders = page.get_order_list()
        # Проверяем, что список заказов не пустой
        assert len(orders) > 0, "Список заказов пуст, хотя заказ был создан"
        # При желании: сравнение id заказа, текста, статуса и т.п.
        last_order = orders[-1]
        order_text = last_order.text
        print("Последний заказ:", order_text)


# проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_users_orders_displayed_in_order_history_and_on_order_feed_pages_with_scroll(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_LOGIN_PAGE)
        page.wait_for_clickable_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
        page.click_to_element(INPUT_EMAIL_LOGIN_PAGE_LOCATOR)
        page.set_text(locator=INPUT_EMAIL_LOGIN_PAGE_LOCATOR, text=email_for_test)
        page.click_to_element(INPUT_PASSWORD_LOGIN_PAGE_LOCATOR)
        page.set_text(locator=INPUT_PASSWORD_LOGIN_PAGE_LOCATOR, text=password_for_test)
        page.click_to_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)

        # Создание заказа
        page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        page.click_to_element(PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR)
        page.drag_and_drop_element(
            INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR,
            BURGER_BUN_ON_TOP_CONSTRUCTOR_PAGE_LOCATOR
        )
        page.click_to_element(BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)

        time.sleep(5)
        page.wait_for_clickable_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        page.click_to_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)

        # История заказов
        time.sleep(3)
        page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
        time.sleep(2)
        page.click_to_element(BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR)
        time.sleep(2)

        # Прокручиваем контейнер с заказами до последнего заказа
        last_order = page.scroll_inside_container_to_element(
            container_locator=ORDER_HISTORY_SCROLL_CONTAINER,
            item_locator=ORDER_ITEMS
        )
        time.sleep(3)

        # Получаем номер последнего заказа
        order_text = last_order.text.strip()
        print("Последний заказ:", order_text)

        # Получаем номер заказа из текста
        order_number = order_text.split('\n')[0]
        print("Номер заказа:", order_number)

        # Далее можно использовать этот номер, например:
        page.open_page(Urls.URL_FEED_OF_ORDERS_PAGE)
        time.sleep(3)

        # Получаем все заказы на странице (в контейнере)
        orders_in_feed = page.get_elements(ORDER_ITEMS_2)  # или какой у тебя локатор для заказов в ленте

        # Ищем среди них элемент с нужным номером заказа
        order_in_feed = None
        for order in orders_in_feed:
            if order_number in order.text:
                order_in_feed = order
                break

        assert order_in_feed is not None, f"Заказ с номером {order_number} не найден в ленте заказов"
        print(f"Заказ с номером {order_number} найден в ленте заказов")


# проверка: при создании нового заказа счётчик Выполнено за всё время увеличивается
    allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_when_creating_new_order_all_time_counter_increases(self, driver):
        page = BasePage(driver)
        page.open_page(Urls.URL_FEED_OF_ORDERS_PAGE)
        completed_all_time_element = int(page.find_element(TOTAL_ORDERS_FOR_ALL_TIME_COUNTER).text)
        completed_today_element = int(page.find_element(TOTAL_ORDERS_FOR_TODAY_COUNTER).text)
        print(completed_all_time_element)
        print(completed_today_element)
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
        time.sleep(5)
        page.wait_for_clickable_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        page.click_to_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        time.sleep(3)
        page.click_to_element(PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR)
        time.sleep(5)
        completed_all_time_element_after_new_order = int(page.find_element(TOTAL_ORDERS_FOR_ALL_TIME_COUNTER).text)
        completed_today_element_after_new_order = int(page.find_element(TOTAL_ORDERS_FOR_TODAY_COUNTER).text)
        print(completed_all_time_element_after_new_order)
        print(completed_today_element_after_new_order)
        print(type(completed_today_element_after_new_order))
        assert completed_all_time_element < completed_all_time_element_after_new_order
        assert completed_today_element < completed_today_element_after_new_order


# проверка: после оформления заказа его номер появляется в разделе В работе
#     allure.title("после оформления заказа его номер появляется в разделе В работе")
#     def test_after_placing_order_its_number_appears_in_progress_section(self, driver):
#         page = BasePage(driver)
#         page.open_page(Urls.URL_LOGIN_PAGE)
#         page.wait_for_clickable_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
#         page.click_to_element(INPUT_EMAIL_LOGIN_PAGE_LOCATOR)
#         page.set_text(locator=INPUT_EMAIL_LOGIN_PAGE_LOCATOR, text=email_for_test)
#         page.click_to_element(INPUT_PASSWORD_LOGIN_PAGE_LOCATOR)
#         page.set_text(locator=INPUT_PASSWORD_LOGIN_PAGE_LOCATOR, text=password_for_test)
#         page.click_to_element(BUTTON_LOGIN_LOGIN_PAGE_LOCATOR)
#         page.click_to_element(PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR)
#         page.click_to_element(PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR)
#         page.drag_and_drop_element(INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR,
#                                    BURGER_BUN_ON_TOP_CONSTRUCTOR_PAGE_LOCATOR)
#         page.click_to_element(BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)
#         time.sleep(5)
#         number_of_order = int(page.find_element(MODAL_WINDOW_OPENED_NUMBER_OF_ORDER).text)
#         print(number_of_order)
#         page.wait_for_clickable_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
#         page.click_to_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
#         time.sleep(3)
#         page.click_to_element(PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR)
#         page.wait_for_visible_element(ORDERS_IN_PROGRESS)
#         orders_in_progress = int(page.find_element(ORDERS_IN_PROGRESS).text)
#         print(orders_in_progress)
#         assert number_of_order == orders_in_progress


    def test_after_placing_order_its_number_appears_in_progress_section(self, driver):
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
        time.sleep(5)

        number_of_order = int(page.find_element(MODAL_WINDOW_OPENED_NUMBER_OF_ORDER).text)
        print(f"Номер созданного заказа: {number_of_order}")

        page.wait_for_clickable_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        page.click_to_element(ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        time.sleep(3)

        page.click_to_element(PARAGRAPH_FEED_OF_ORDERS_HEADER_LOCATOR)
        page.wait_for_visible_element(ORDERS_IN_PROGRESS)

        # Получаем список номеров заказов в работе
        orders_in_progress_list = page.get_all_orders_number_in_progress_list(ORDERS_IN_PROGRESS)
        print(f"Список номеров заказов в работе: {orders_in_progress_list}")

        # Проверяем, что номер созданного заказа есть в списке
        assert str(number_of_order) in orders_in_progress_list, "Новый заказ не отображается в списке в работе"


