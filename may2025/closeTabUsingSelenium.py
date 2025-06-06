import time
from selenium import webdriver
#import library
driver = webdriver.Chrome()
#define driver for chrome
driver.maximize_window()
#maximize driver / web page
driver.get("https://www.google.com")
#navigate to googgle
print(driver.title)
#fetch title of webpage
driver.execute_script('window.open("https://www.icicibank.com");')
#for opening in another tab use window.open and navigate to another web site
print(len(driver.window_handles))
#fetch how many webpages are open in 1 chrome with different tab
driver.switch_to.window(driver.window_handles[1])
#switch to window with another web application
print(driver.title)
#fetch title of new web application
driver.close()
#close current web page / window
driver.switch_to.window(driver.window_handles[0])
#switch back to parent window
print(driver.title)
#fetch title of parent tab

time.sleep(5)