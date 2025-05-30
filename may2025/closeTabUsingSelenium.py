import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.execute_script('window.open("https://www.icicibank.com");')
print(len(driver.window_handles))
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.title)

time.sleep(5)