import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#selenium4 ... updated on 13dec2024
#https://www.saucedemo.com/
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.saucedemo.com/"
driver.get(url)

driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
#
products_txt = driver.find_element(By.XPATH,"//span[contains(text(),'Products')]").is_displayed()
# print(products_txt)
# exp_title = 'OrangeHRM'
if products_txt:
     print("Login Test Pass")
else:
     print("Login Test Failed")
# time.sleep(10)
print("done....")
driver.quit()