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


url = "https://www.linkedin.com"
driver.get(url)
driver.maximize_window()
signinXpath="//a[contains(@href,'signin')]"
click(signinXpath)
userIdXpath="//input[@id='username']"
pwdXpath="//input[@id='password']"
loginbuttonXpath="//button[@type='submit']"
enterData(userIdXpath,"pritibhushanf@gmail.com")
click(loginbuttonXpath)

click("//span[@title='Jobs']")
print("Done....")

time.sleep(5)