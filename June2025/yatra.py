import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
wait = WebDriverWait(driver,15)
def click(xpathOfElement):
    wait.until(EC.element_to_be_clickable((By.XPATH,xpathOfElement)))
    driver.find_element(By.XPATH,xpathOfElement).click()


def enterData(xpathOfElement,data):
    wait.until(EC.element_to_be_clickable((By.XPATH, xpathOfElement)))
    driver.find_element(By.XPATH, xpathOfElement).send_keys(data)


url = "https://www.yatra.com"
# Launch Yatra.com
driver.get(url)
driver.maximize_window()

# 2. Click on departure date calendar with default selected cities
click("(//div[contains(@aria-label,'Departure Date inputbox')]/div)[2]")
# 3. Select any random date with lowest fare in current month.
click("//div[@aria-label='Choose Friday, June 20th, 2025']")
# 4. Select any random date with lowest fare in next month.
click("//span[contains(text(),'Book Round Trip')]")
click("//div[@aria-label='Choose Wednesday, July 16th, 2025']")
# 5. Select any random date with lowest fare in both month.

time.sleep(15)
