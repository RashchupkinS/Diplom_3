from selenium.webdriver.common.by import By



# заголовок "Соберите бургер"
HEADER_ASSEMBLE_BURGER_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//h1[text()='Соберите бургер']"

# заголовок "Соберите бургер"
INGREDIENT_R2_D2_BUN_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"

INGREDIENT_DETAILS_WINDOW_CONSTRUCTOR_PAGE_LOCATOR = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and text()='Детали ингредиента']")

# иконка "крестик" модального окна "Детали ингредиента
ICON_CROSS_MODAL_WINDOW_CONSTRUCTOR_PAGE_LOCATOR = By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]"


MODAL_WINDOW_CLOSED_CONSTRUCTOR_PAGE_LOCATOR = By.CSS_SELECTOR, "section.Modal_modal__P3_V5"






