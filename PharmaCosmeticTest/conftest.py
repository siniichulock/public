import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CHR_opt


@pytest.fixture
def get_chrome_options():
    options = CHR_opt()
    options.add_argument("headless")
    options.add_argument('--start-maximize')
    options.add_argument('--window-size=1400,1000')
    return options


@pytest.fixture
def go_browser(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options)
    yield driver
    driver.quit()