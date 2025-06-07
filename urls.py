class Urls:
    # url раздела "Главная страница" и раздела "Конструктор"
    URL_MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    # url раздела "Регистрация"
    URL_REGISTRATION_PAGE = URL_MAIN_PAGE + "register"
    # url раздела "Вход"
    URL_LOGIN_PAGE = URL_MAIN_PAGE + "login"
    # url раздела "Восстановление пароля"
    URL_FORGOT_PASSWORD_PAGE = URL_MAIN_PAGE + "forgot-password"
    # url раздела "Личный кабинет
    URL_PERSONAL_ACCOUNT_PAGE = URL_MAIN_PAGE + "account/profile"
    # url раздела "Сбросить пароль"
    # данная страница открывается при переходе со страницы "Восстановление пароля"
    # по прямой ссылке автоматический переход на страницу "Восстановление пароля"
    URL_RESET_PASSWORD_PAGE = URL_MAIN_PAGE + "reset-password"
    # url раздела "История заказов"
    URL_ORDERS_HISTORY_PAGE = URL_MAIN_PAGE + "account/order-history"
    # url раздела "Лента заказов"
    URL_FEED_OF_ORDERS_PAGE = URL_MAIN_PAGE + "feed"


