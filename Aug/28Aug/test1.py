import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobile")
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(2)
result_items = driver.find_elements(By.CSS_SELECTOR,"div.s-main-slot div[data-component-type='s-search-result']")
print(len(result_items))
assert result_items >0
result_items[1].click()
time.sleep(5)