from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *


class TestExitAccount:
    def test_log_out_account(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located(Locators.account_button))
        wd.find_element(*Locators.account_button).click()
        exit_button = WebDriverWait(wd, 10).until(EC.element_to_be_clickable(Locators.exit_button))
        exit_button.click()
        check_text_enter = WebDriverWait(wd, 10).until(EC.visibility_of_element_located(Locators.text_enter)).text
        assert check_text_enter == 'Вход'
