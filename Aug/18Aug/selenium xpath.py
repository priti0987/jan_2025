import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#selenium4 ... updated on 13dec2024
#https://www.saucedemo.com/
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://www.saucedemo.com/"
url = "https://money.rediff.com/gainers/bse/daily/gropua"
driver.get(url)
driver.maximize_window()
print(driver.title)
time.sleep(2)
#self node
self_nodetext = driver.find_element(By.XPATH,"//a[contains(text(),'Recycling ')]/self::a").text
print(self_nodetext)
time.sleep(10)

[parent ] = driver.find_element(By.XPATH,"//a[contains(text(),'Recycling ')]/self::a").text
