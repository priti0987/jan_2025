#https://www.naukri.com/mnjuser/profile
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


def getAttribute(xpathOfElement):
    wait.until(EC.element_to_be_clickable((By.XPATH, xpathOfElement)))
    xpathListOfDatesEnabled = "//div[@aria-disabled='false']"
    returnAttribute = driver.find_element(By.XPATH, xpathOfElement).text
    returnAttribute=returnAttribute.replace("₹","")
    #print(returnAttribute.replace(",",""))

    listofdates_1 = driver.find_elements(By.XPATH,xpathListOfDatesEnabled)
    print(len(listofdates_1))
    myList=[]
    for i in range(1,len(listofdates_1)):
        try:
            xppath = '(//div[@aria-disabled="false"])['+str(i)+']/span/span'
            elementPrice = driver.find_element(By.XPATH,xppath).text
            elementPrice = elementPrice.replace("₹","")
            elementPrice = elementPrice.replace(",", "")
            myList.append(int(elementPrice))

        except:
            pass
    print("min==:",min(myList))
    # try:
    #     returnAttribute = driver.find_element(By.XPATH, xpathOfElement).get_attribute(attribute)
    #     return returnAttribute
    # except:
    #     print("error")

url = "https://www.naukri.com/mnjuser/profile"
# Launch naukri.com
driver.get(url)
driver.maximize_window()
enterData("//input[@id='usernameField']","pritibhushanf@gmail.com")
enterData("//input[@id='passwordField']","Bhavika@1")
click("//button[@type='submit']")
time.sleep(15)
