import allure
from pages.base_page import BasePage
from urls import Urls
from locators.constructor_page_locators import ConstructorPageLocators as CPL




class ConstructorPage(BasePage):

    @allure.step('Открыть страницу "Конструктор"')
    def open_constructor_page(self):
        self.open_page(Urls.URL_MAIN_PAGE)


    @allure.step('Кликнуть булку "Флюоресцентная булка R2-D3" на странице "Конструктор" '
                 'и дождаться загрузки окна с деталями ингредиента')
    def click_on_r2_d3_bun(self):
        self.click_to_element_by_script(CPL.INGREDIENT_R2_D3_BUN_CONSTRUCTOR_PAGE_LOCATOR)
        self.wait_for_visible_element(CPL.HEADER_INGREDIENT_DETAILS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Перетащить булку "Флюоресцентная булка R2-D3" в корзину бургера')
    def drag_and_drop_r2_d3_bun_to_burger(self):
        self.drag_and_drop_element(CPL.INGREDIENT_R2_D3_BUN_CONSTRUCTOR_PAGE_LOCATOR,
                                   CPL.BURGER_BASKET_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Кликнуть кнопку "Оформить заказ" на странице "Конструктор" и '
                 'дождаться видимости заголовка "идентификатор заказа" в открывшемся окне')
    def click_on_create_order_button(self):
        self.click_to_element_by_script(CPL.BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)
        self.wait_for_real_order_number(CPL.HEADER_NUMBER_OF_ORDER_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Кликнуть иконку "Крестик"')
    def click_on_cross_in_ingredients_window(self):
        self.click_to_element_by_script(CPL.ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        self.wait_for_constructor_page()


    @allure.step('Получить значение счётчика ингредиента')
    def get_ingredient_r2_d3_counter_value(self):
        return self.get_element_title(CPL.INGREDIENT_COUNTER_R2_D3_BUN_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Получить номер заказа из окна с заказом')
    def get_number_of_order(self):
        element = self.find_element(CPL.HEADER_NUMBER_OF_ORDER_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)
        text = element.text.replace(" ", "").strip()
        return text


    @allure.step('Получить заголовок ингредиента "Флюоресцентная булка R2-D3" в корзине')
    def get_title_ingredient_r2_d3_in_basket(self):
        return self.get_element_title(CPL.INGREDIENT_R2_D3_BUN_IN_BASKET_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Получить заголовок: "идентификатор заказа"')
    def get_title_id_order(self):
        return self.get_element_title(CPL.HEADER_ORDER_ID_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Получить заголовок: "Детали ингредиента"')
    def get_title_ingredient_details(self):
        return self.get_element_title(CPL.HEADER_INGREDIENT_DETAILS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Получить заголовок: "Соберите бургер"')
    def get_title_header_assemble_burger(self):
        return self.get_element_title(CPL.HEADER_ASSEMBLE_BURGER_CONSTRUCTOR_PAGE_LOCATOR)


    @allure.step('Проверка отображения модального окна')
    def is_displayed_opened_modal_window(self):
        return self.find_element(CPL.MODAL_WINDOW_OPENED_CONSTRUCTOR_PAGE_LOCATOR).is_displayed()


    @allure.step('Проверка отображения модального окна')
    def is_displayed_closed_modal_window(self):
        return self.find_element(CPL.MODAL_WINDOW_CLOSED_CONSTRUCTOR_PAGE_LOCATOR).is_displayed()


