from locators import Locators


class TestConstructorPage:
    def test_constructor_transfer_sauce(self, wd):
        wd.find_element(*Locators.sauce).click()
        check_text_sauce = wd.find_element(*Locators.sauce).text
        check_active_element = wd.find_element(*Locators.active_section).text
        assert check_text_sauce == check_active_element

    def test_constructor_transfer_bread(self, wd):
        wd.find_element(*Locators.filling).click()
        wd.find_element(*Locators.bread).click()
        check_text_bread = wd.find_element(*Locators.bread).text
        check_active_element = wd.find_element(*Locators.active_section).text
        assert check_text_bread == check_active_element

    def test_constructor_transfer_filling(self, wd):
        wd.find_element(*Locators.filling).click()
        check_text_filling = wd.find_element(*Locators.filling).text
        check_active_element = wd.find_element(*Locators.active_section).text
        assert check_text_filling == check_active_element
