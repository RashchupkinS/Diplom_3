import allure
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from locators.login_page_locators import LoginPageLocators as LPL
from locators.feed_of_orders_page_locators import FeedOfOrdersPageLocators as FOOL
from seletools.actions import drag_and_drop




# класс содержит базовые методы
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WDW(driver, 20)


    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)
        self.wait.until(EC.url_contains(url))
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )


    @allure.step('Кликнуть элемент')
    def click_to_element_by_script(self, locator):
        element = self.wait_for_visible_element(locator)
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


    @allure.step('Ожидание наличия элемента в DOM')
    def wait_for_presence_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))


    @allure.step('Ожидание видимости элемента')
    def wait_for_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    @allure.step('Ожидание невидимости элемента либо отсутствие в DOM')
    def wait_for_invisibility_element(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))


    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)


    @allure.step('Найти элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)


    @allure.step('Очистить поле и вставить текст')
    def set_text_in_element(self, locator, text):
        element = self.wait_for_clickable_element(locator)
        element.clear()
        element.send_keys(text)


    @allure.step('Получить текущий url')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Получить элемент')
    def get_element(self, locator):
        return self.driver.find_element(*locator)


    @allure.step('Получить текст элемента')
    def get_element_title(self, locator):
        element = self.driver.find_element(*locator)
        return element.text


    @allure.step('Нажать кнопку "Конструктор" в хедере')
    def click_button_constructor_in_header(self):
        self.scroll_and_click(CPL.BUTTON_CONSTRUCTOR_IN_HEADER_LOCATOR)


    @allure.step('Нажать кнопку "Лента Заказов" в хедере')
    def click_button_feed_of_orders_in_header(self):
        self.scroll_and_click(CPL.BUTTON_FEED_OF_ORDERS_IN_HEADER_LOCATOR)


    @allure.step('Нажать на кнопку "Личный кабинет" в хедере')
    def click_button_personal_account_in_header(self):
        self.scroll_and_click(CPL.BUTTON_PERSONAL_ACCOUNT_IN_HEADER_LOCATOR)


    @allure.step('Скролл к элементу и кликаем по нему через JS: {locator}')
    def scroll_and_click(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step('Ожидание исчезновения элемента')
    def wait_for_invisible_element(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))


    @allure.step('Перетащить элемент drag-and-drop')
    def drag_and_drop_element(self, locator_from, locator_to):
        source = self.wait_for_visible_element(locator_from)
        target = self.wait_for_visible_element(locator_to)
        drag_and_drop(self.driver, source, target)


    @allure.step('Ожидание ')
    def wait_for_constructor_page(self):
        self.wait_for_presence_element(CPL.HEADER_ASSEMBLE_BURGER_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Ожидание ')
    def wait_for_login_page(self):
        self.wait_for_presence_element(LPL.HEADER_LOGIN_LOGIN_PAGE_LOCATOR)


    @allure.step('Ожидание ')
    def wait_for_feed_of_orders_page(self):
        self.wait_for_presence_element(FOOL.HEADER_FEED_OF_ORDERS_PAGE_LOCATOR)


    @allure.step("Обновить страницу и дождаться её полной загрузки")
    def refresh_page_and_wait(self, locator):
        self.driver.refresh()
        self.wait.until(EC.presence_of_element_located(locator))


    @allure.step("Получить значение счётчика по локатору")
    def get_counter_by_locator(self, locator):
        element = self.find_element(locator)
        text = element.text.replace(" ", "").strip()
        return int(text)


