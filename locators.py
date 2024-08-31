from selenium.webdriver.common.by import By


class Locators:
# Авторизация на сайте
    account_button = (By.XPATH, "//a[@href = '/account']")
    email_input = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    password_input = (By.XPATH, './/input[@name="Пароль"]')
    enter_click = (By.XPATH, './/button[contains(text(),"Войти")]')

# Кнопка Войти
    enter_button = (By.XPATH, ".//a[text()='Войти']")

# Кнопка Выход
    exit_button = (By.XPATH, "//button[contains(text(),'Выход')]")

# Проверка текста ВХОД
    text_enter = (By.XPATH, ".// h2[text() = 'Вход']")

# Кнопка зарегистрироваться
    registr_button = (By.XPATH, "//a[(text()='Зарегистрироваться')]")

# Кнопка восстановить пароль
    recover_pass = (By.XPATH, ".//a[text()='Восстановить пароль']")

# Ошибка при вводе неправильного пароля
    invalid_password = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

# Кнопка Войти в аккаунт
    account_enter = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")

# Поле ввода имени
    name_input = (By.XPATH, './/input[@name="name"]')

# Оформить заказ
    button_order = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

# Переход в личный кабинет
    account_autorize_button = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

# Переход в конструктор
    constructor = (By.XPATH, "//p[contains(text(),'Конструктор')]")

# Клик на логотип
    logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

# Переход Булки
    bread = (By.XPATH, "//span[text() = 'Булки']")

# Переход Соусы
    sauce = (By.XPATH, "//span[text() = 'Соусы']")

# Переход Начинки
    filling = (By.XPATH, "//span[text() = 'Начинки']")

# Активированная секция
    active_section = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")

# Проверка личного кабинета
    check_account_page = (By.XPATH, ".//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]")

# Локаторы для проверки наличия текста
    sauce_check = (By.XPATH, "//span[text() = 'Соусы']")
    bread_check = (By.XPATH, "//span[text() = 'Булки']")
    filling_check = (By.XPATH, "//span[text() = 'Начинки']")
