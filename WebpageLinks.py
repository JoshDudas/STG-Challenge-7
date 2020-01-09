from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import WebDriverException


class ValidateLinks:
    def __init__(self, driver):
        self._driver = driver
        self._driver_wait = WebDriverWait(self._driver, 10)
        self._wait_elements = []
        self._links_matrix = {'display_text': '', 'link_url': ''}

    def _page_load_wait(self, wait_elements):
        if len(wait_elements) > 1:
            for element in wait_elements:
                self._driver_wait.until(ec.invisibility_of_element((By.XPATH, element)))
        else:
            self._driver_wait.until(ec.invisibility_of_element((By.XPATH, str(wait_elements))))

    def store_link_text_and_url(self, element_list):
        element_text_list = []
        element_url_list = []
        for element in element_list:
            element_text_list.append(element.text)
            element_url_list.append(element.get_attribute('href'))
        self._links_matrix['display_text'] = element_text_list
        self._links_matrix['link_url'] = element_url_list

    def validate_urls(self, validation_element: str, wait_element: list):
        for url in self._links_matrix['link_url']:
            try:
                self._driver.get(url)
                url_page_source = self._driver.page_source
                self._page_load_wait(wait_element)
                assert(self._driver.find_element(By.XPATH, validation_element).is_displayed())
            except AssertionError as validate_url_error:
                print('when checking if the validation element exists. The following error was thrown: {}'.format(validate_url_error.msg))
            except WebDriverException as validate_url_error:
                print("When attempting to load link ({}) it threw the following error: {}".format(url, validate_url_error.msg))
                continue

