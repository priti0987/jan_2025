#scraaping
import time

from selenium import webdriver


website = "https://www.nseindia.com/option-chain"
driver = webdriver.Chrome()
newUrl="https://www.nseindia.com/get-quotes/derivatives?symbol=BANKNIFTY&identifier=OPTIDXBANKNIFTY30-09-2025CE55800.00"

driver.get(newUrl)
driver.maximize_window()

time.sleep(5)
