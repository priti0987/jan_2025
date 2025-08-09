import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

search_keywords = [
    "selenium python",
    "priti",
    "tutorials"
]

@pytest.mark.parametrize("search_keyword",search_keywords)
class TestGoogleSearch:
    def test_search(self,browser,search_keyword):
        driver = browser
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.XPATH,"//textarea[@name='q']")
        search_box.send_keys(search_keyword)
        search_box.send_keys(Keys.Return)
        time.sleep(10)
        assert search_keyword in driver.title
        print(f"Search for {search_keyword}")

class test_1:
    def test_search1(self):
        driver = webdriver.chrome()
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.XPATH,"//textarea[@name='q']")
        search_box.send_keys("test")