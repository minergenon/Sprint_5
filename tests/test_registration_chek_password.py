from locators import Locators
from data import *
from generate import *


class TestRegistration:
    def test_successful_registration(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.registr_button).click()
        wd.find_element(*Locators.name_input).send_keys(user_name)
        wd.find_element(*Locators.email_input).send_keys(generator_email())
        wd.find_element(*Locators.password_input).send_keys(generator_password())
        wd.find_element(*Locators.enter_button).click()
        enter_page_main = wd.find_element(*Locators.text_enter).text
        assert enter_page_main == "Вход"

    def test_invalid_password(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.registr_button).click()
        wd.find_element(*Locators.name_input).send_keys(user_name)
        wd.find_element(*Locators.email_input).send_keys(generator_email())
        wd.find_element(*Locators.password_input).send_keys(invalid_password)
        wd.find_element(*Locators.enter_button).click()
        incorrect_password = wd.find_element(*Locators.invalid_password).text
        assert incorrect_password == "Некорректный пароль"
