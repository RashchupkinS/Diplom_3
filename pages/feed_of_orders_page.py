import allure
from pages.base_page import BasePage
from urls import Urls
from locators.feed_of_orders_page_locators import FeedOfOrdersPageLocators as FOOL




class FeedOfOrdersPage(BasePage):

    @allure.step('Открыть страницу "Лента заказов"')
    def open_feed_of_orders_page(self):
        self.open_page(Urls.URL_FEED_OF_ORDERS_PAGE)


    @allure.step('Кликнуть ')
    def click_on_order(self):
        element = self.wait_for_visible_element(FOOL.ORDER_ITEMS_IN_LIST_FEED_OF_ORDERS_PAGE_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()


    def get_title_order_details(self):
        return self.get_element_title(FOOL.HEADER_ORDERS_DETAIL_MODAL_WINDOW_FEED_OF_ORDERS_PAGE_LOCATOR)


    @allure.step('Окно открыто')
    def is_displayed_opened_modal_window(self):
        return self.find_element(FOOL.MODAL_WINDOW_OPENED_FEED_OF_ORDERS_PAGE_LOCATOR).is_displayed()


    @allure.step('Ожидание ')
    def wait_for_visible_window_with_order(self):
        return self.wait_for_visible_element(FOOL.HEADER_ORDERS_DETAIL_MODAL_WINDOW_FEED_OF_ORDERS_PAGE_LOCATOR)


    @allure.step('Поиск')
    def find_modal_window_order_details(self):
        return self.find_element(FOOL.HEADER_ORDERS_DETAIL_MODAL_WINDOW_FEED_OF_ORDERS_PAGE_LOCATOR)


    def get_counter(self, locator):
        element = self.find_element(locator)
        return int(element.text.replace(" ", "").strip())


    @allure.step("Получение списка номеров заказов в работе")
    def get_all_orders_number_in_progress_list(self):
        self.wait_for_visible_element(FOOL.ORDERS_IN_PROGRESS_FEED_OF_ORDERS_PAGE_LOCATOR)
        orders_elements = self.driver.find_elements(*FOOL.ORDERS_IN_PROGRESS_FEED_OF_ORDERS_PAGE_LOCATOR)
        list_of_orders = []
        for item in orders_elements:
            order_text = item.text.strip()
            order_number = order_text.lstrip('0')
            list_of_orders.append(order_number)
        return list_of_orders

    @allure.step('Получить список номеров заказов из ленты заказов')
    def get_order_numbers_in_feed_of_orders(self):
        orders_elements = self.find_elements(FOOL.ORDER_NUMBERS_IN_FEED_FEED_OF_ORDERS_PAGE_LOCATOR)
        order_numbers = []
        for order_el in orders_elements:
            # предположим, что номер заказа — это первая строка текста элемента
            order_text = order_el.text
            order_number = order_text.split('\n')[0].strip()
            order_numbers.append(order_number)
        return order_numbers


    def refresh_feed_of_orders_page_and_wait(self):
        self.refresh_page_and_wait(FOOL.HEADER_FEED_OF_ORDERS_PAGE_LOCATOR)


