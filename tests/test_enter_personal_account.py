from locators import Locators
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPersonalAccount:
    def test_transfer_to_personal_account(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        WebDriverWait(wd, 10).until(EC.presence_of_element_located(Locators.check_account_page))
        check_account_page = wd.find_element(*Locators.check_account_page).text
        assert check_account_page == 'В этом разделе вы можете изменить свои персональные данные'

    def test_transfer_to_constructor(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.constructor).click()
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable(Locators.button_order))
        check_text = wd.find_element(*Locators.button_order).text
        assert check_text == 'Оформить заказ'

    def test_transfer_to_logo(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.logo).click()
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable(Locators.button_order))
        check_text = wd.find_element(*Locators.button_order).text
        assert check_text == 'Оформить заказ'
