import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAutomatedChromeBrowser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_getMakeModelList_Urls(self):
        driverwait = WebDriverWait(self.driver, 10)
        self.driver.get('https://www.copart.com')
        driverwait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@id="tabTrending"]')))
        popular_items_list = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]//a')

        popular_items_matrix = [[],[]]
        for item in popular_items_matrix:
            popular_items_matrix[0].append(item.text)
            popular_items_matrix[1].append(item.get_attribute('href'))

        i = 0
        while i < len(popular_items_matrix[0]):
            print(popular_items_matrix[0][i] + " - " + popular_items_matrix[1][i])
            i += 1

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()