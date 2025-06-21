import allure
from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators as PAPL
import logging




logger = logging.getLogger(__name__)


class PersonalAccountPage(BasePage):

    @allure.step('Нажать кнопку "История заказов" на странице "Личный кабинет" и дождаться загрузки истории заказов')
    def click_orders_history_button(self):
        self.click_to_element_by_script(PAPL.BUTTON_ORDERS_HISTORY_ACCOUNT_PAGE_LOCATOR)


    @allure.step('Нажать кнопку "Выход" на странице "Личный кабинет"')
    def click_exit_button(self):
        self.click_to_element_by_script(PAPL.BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR)
        self.wait_for_login_page()


    @allure.step('Получить список заказов в "История заказов" на странице "Личный кабинет"')
    def get_order_list(self):
        return self.find_elements(PAPL.ORDER_ITEMS_IN_FEED_HISTORY_IN_PERSONAL_ACCOUNT_PAGE_LOCATOR)


    @allure.step('Ожидание список заказов в "Истории заказов" в личном кабинете')
    def wait_for_visible_feed_with_orders(self):
        return self.wait_for_visible_element(PAPL.ORDER_ITEMS_IN_FEED_HISTORY_IN_PERSONAL_ACCOUNT_PAGE_LOCATOR)


    @allure.step('Получить номер последнего заказа в истории заказов')
    def get_last_order_number(self):
        orders = self.get_order_list()
        if len(orders) > 0:
            last_order = orders[-1]
            order_text = last_order.text
            order_number = order_text.split('\n')[0]
            return order_number
        else:
            logger.warning("Список заказов пуст")
            return None


