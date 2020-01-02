import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from WebpageLinks import ValidateLinks

class TestAutomatedChromeBrowser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver_wait = WebDriverWait(self.driver, 10)
        self._popular_items_matrix = [[], []]

    def open_webpage(self):
        self.driver.get('https://www.copart.com')

    def wait_for_page_to_load(self):
        self.driver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@id="tabTrending"]')))

    def get_popular_items(self):
        popular_items_list = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]//a')
        return popular_items_list

    def check_each_popular_item_link(self):
        i = 0
        while i < len(self._popular_items_matrix[0]):
            try:
                self.driver.get(self._popular_items_matrix[1][i])
                self.driver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//img[@alt="Copart"]')))
            except TimeoutError:
                print("ERROR: {}'s link ({}) timed out".format(str(self._popular_items_matrix[0][i]).upper(),
                                                               str(self._popular_items_matrix[1][i]).upper()))
            i += 1

    def test_get_Popular_Searches_Items_and_Urls(self):
        copart_links = ValidateLinks()
        self.open_webpage()
        self.wait_for_page_to_load()
        copart_links.store_link_text_and_url(self.get_popular_items())
        element = '//*[@src="/images/icons/loader.gif"]'
        wait_elements = []
        wait_elements.append(element)
        copart_links.validate_urls('//*[contains(@alt, "Copart")]', wait_elements)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()