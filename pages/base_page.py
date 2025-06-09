import allure
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from locators.constructor_page_locators import ConstructorPageLocators as CPL
from locators.personal_account_page_locators import ORDER_ITEMS_IN_FEED_HISTORY_IN_PERSONAL_ACCOUNT_PAGE_LOCATOR
from selenium.webdriver.common.by import By

import os
import inspect



# класс содержит базовые методы
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WDW(driver, 20)
        self.actions = ActionChains(driver)


    # метод открывает переданную страницу
    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)
        self.waiting_for_overlay_to_disappear()


    @allure.step('Ожидание исчезновения overlay')
    def waiting_for_overlay_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(CPL.OVERLAY_LOCATOR))


        # клик по элементу

    @allure.step('Кликнуть элемент с прокруткой в зону видимости')
    def click_to_element_by_js(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    @allure.step('Кликнуть элемент с прокруткой в зону видимости')
    def click_to_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        element.click()



    # метод выполняет клик по элементу
    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


    # метод
    @allure.step('Ожидание видимости элемента')
    def wait_for_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    # метод выполняет клик по элементу
    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)


    # метод передаёт тест элементу
    @allure.step('Изменить текст')
    def set_text(self, locator, text):
        element = self.wait_for_clickable_element(locator)
        element.clear()
        element.send_keys(text)


    # метод получает текущий url
    @allure.step('Получить текущий url')
    def get_current_url(self):
        return self.driver.current_url



    # # метод передаёт тест элементу
    # @allure.step('Перетащить элемент')
    # def drag_and_drop_element(self, locator_from, locator_to):
    #     drag_and_drop(self.driver, locator_from, locator_to)


    @allure.step('Перетащить элемент с помощью ActionChains')
    def drag_and_drop_element(self, locator_from, locator_to):
        source = self.wait_for_visible_element(locator_from)
        target = self.wait_for_visible_element(locator_to)
        self.actions.drag_and_drop(source, target).perform()




    # скроллинг до элемента и ожидание его кликабельности
    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.element_to_be_clickable(element))
        return element

    @allure.step("Получить список заказов")
    def get_order_list(self):
        return self.driver.find_elements(*ORDER_ITEMS_IN_FEED_HISTORY_IN_PERSONAL_ACCOUNT_PAGE_LOCATOR)

    @allure.step("Прокрутить контейнер до элемента")
    def scroll_inside_container_to_element(self, container_locator, item_locator):
        container = self.driver.find_element(*container_locator)
        items = container.find_elements(*item_locator)
        if not items:
            raise Exception("Элементы внутри контейнера не найдены")
        last_item = items[-1]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'end'});", last_item)
        self.wait.until(EC.element_to_be_clickable(last_item))
        return last_item

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)




    @allure.step("Получение списка номеров заказов в работе")
    def get_all_orders_number_in_progress_list(self, locator):
        self.wait_for_visible_element(locator)  # дождаться видимости хотя бы одного элемента
        orders_elements = self.driver.find_elements(*locator)
        list_of_orders = []
        for item in orders_elements:
            order_text = item.text.strip()
            order_number = order_text.lstrip('0')
            list_of_orders.append(order_number)
        return list_of_orders






    # # метод выполняет клик по элементу
    # @allure.step('Ожидание видимости элемента')
    # def wait_for_element(self, locator):
    #     return self.wait.until(
    #         EC.presence_of_element_located(locator))
    #

    # # метод получает текст элемента
    # @allure.step('Получить текст')
    # def get_text(self, locator):
    #     element = self.wait_for_element(locator)
    #     return element.text


    # # метод передаёт тест элементу
    # @allure.step('Изменить текст')
    # def set_text(self, locator, text):
    #     element = self.wait_for_element(locator)
    #     element.send_keys(text)


    # # метод получает текущий url
    # @allure.step('Получить текущий url')
    # def get_current_url(self):
    #     return self.driver.current_url


    # # метод проверяет, что страница загрузилась по "кликабельности" кнопки "Заказать" в хедере
    # @allure.step('Дождаться кликабельности кнопки заказать в хедере')
    # def wait_for_order_button(self):
    #     self.wait.until(
    #         EC.element_to_be_clickable(BasePageLocators.BUTTON_ORDER_IN_HEADER_LOCATOR)
    #     )


    # # при клике на логотип Яндекс, открывается новая вкладка и в ней открывается страница Дзен
    # @allure.step('Проверить переход при клике на логотип Яндекс в хедере')
    # @allure.description('При клике на логотип Яндекс, открывается новая вкладка и в ней открывается страница Дзен')
    # def click_to_logo_yandex_and_change_to_dzen(self):
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     return self.wait.until(EC.url_contains(URL_DZEN))


    # # принятие куки, клик по кнопке "Заказать" в хедере
    # @allure.step('Переход в форме заказа при клике кнопки "Заказать" в хедере')
    # @allure.description('Принять куки, клик по кнопке "Заказать" в хедере и подтверждение перехода к форме "Заказать"')
    # def click_order_button_in_header_and_transition_to_order_page(self):
    #     self.accept_cookie()
    #     self.click_to_element(BasePageLocators.BUTTON_ORDER_IN_HEADER_LOCATOR)
    #     self.wait_for_element(OrderPageLocators.FIELD_INPUT_NAME_LOCATOR)

    def wait_of_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))





    @allure.step("Сделать скриншот страницы")
    def make_screenshot(self, prefix="test"):
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        # Получаем имя вызывающего теста
        stack = inspect.stack()
        test_func_name = ""
        for frame in stack:
            if frame.function.startswith("test_"):
                test_func_name = frame.function
                break

        # Берём первые 3 слова из имени теста (по нижнему подчёркиванию)
        parts = test_func_name.split("_")[:4]  # test + 3 слова
        base_name = "_".join(parts) if parts else prefix

        # Считаем количество существующих файлов с этим префиксом
        existing = [f for f in os.listdir(folder) if f.startswith(base_name)]
        filename = f"{base_name}_{len(existing) + 1}.png"

        path = os.path.join(folder, filename)
        self.driver.save_screenshot(path)