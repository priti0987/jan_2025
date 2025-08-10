import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#selenium4 ... updated on 13dec2024
#https://www.saucedemo.com/
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://www.saucedemo.com/"
url = "https://www.hyrtutorials.com/p/add-padding-to-containers.html"
driver.get(url)
driver.maximize_window()
print(driver.title)
driver.get("https://www.youtube.com")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.refresh()