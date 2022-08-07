from settings import valid_email, valid_password
from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def testing():
    driver = webdriver.Chrome(r'C:\Users\Admin\chromedriver_win32\chromedriver.exe')

    driver.get('http://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


@pytest.fixture
def signup_form(testing):
    driver = testing
    driver.find_element_by_id('email').send_keys(valid_email)

    driver.find_element_by_id('pass').send_keys(valid_password)

    driver.find_element_by_css_selector('button[type="submit"]').click()
    return driver
