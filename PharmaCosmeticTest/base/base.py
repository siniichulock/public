import time
from typing import List
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    _browser = None

    def __init__(self, browser, url):
        self._browser = browser
        self.wait = WebDriverWait(browser, 10, 0.3)
        self.open_main_page(url)

    def open_main_page(self, url):
        self._browser.get(url)

    def go_back(self):
        self._browser.back()

    def scroll_down(self, offset=0):
        if offset:
            self._browser.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self._browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        if offset:
            self._browser.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self._browser.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    @staticmethod
    def __change_type_of_search(find_by: str):
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'id': By.ID,
                    'xpath': By.XPATH,
                    'class': By.CLASS_NAME,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'part_link_txt': By.PARTIAL_LINK_TEXT,
                    'tag': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str):
        return self.wait.until(ec.visibility_of_element_located((self.__change_type_of_search(find_by), locator)))

    def is_present(self, find_by: str, locator: str) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.__change_type_of_search(find_by), locator)))

    def is_not_present(self, find_by: str, locator: str) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located((self.__change_type_of_search(find_by), locator)))

    def are_visible(self, find_by: str, locator: str) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.__change_type_of_search(find_by), locator)))

    def are_present(self, find_by: str, locator: str) -> List[WebElement]:
        return self.wait.until(ec.presence_of_all_elements_located((self.__change_type_of_search(find_by), locator)))

    def get_current_url(self):
        return self._browser.current_url

    def get_relative_link(self):
        url = urlparse(self._browser.current_url)
        return url.path

    @staticmethod
    def get_text_from_elements(elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

    @staticmethod
    def get_elements_by_text(elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def open_link(self, find_by, locator):
        button = self.is_visible(find_by, locator)
        button.click()
        time.sleep(5)

    def get_text(self, find_by, locator):
        element = self.is_visible(find_by, locator)
        text = ''

        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_list_of_elements_text(self, find_by, locators) -> str:
        elements = self.are_visible(find_by, locators)
        elements_text = self.get_text_from_elements(elements)
        return ','.join(elements_text)

    def open_link_in_footer(self, find_by, locator):
        self.scroll_down()
        button = self.is_visible(find_by, locator)
        button.click()

    def send_text(self, keys, find_by, locator, wait=2):
        keys = keys.replace('\n', '\ue007')

        element = self.is_visible(find_by, locator)

        if element:
            element.click()
            element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(locator))

    def search_page_open(self, keys, find_by1, locator1, find_by2, locator2):
        self.send_text(keys, find_by1, locator1)
        self.open_link(find_by2, locator2)
