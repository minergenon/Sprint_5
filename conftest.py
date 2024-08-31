import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture()
def wd():
    options = Options()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)
    yield driver
    driver.quit()
