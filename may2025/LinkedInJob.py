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
enterData(pwdXpath,"Pratap@1")
click(loginbuttonXpath)
#********************* click on setting ********************
#click("//span[@title='Jobs']")
# click("//span[text()='Me']")
resume_page_Url="https://www.linkedin.com/jobs/application-settings/?hideTitle=true"
driver.get(resume_page_Url)
time.sleep(3)

pathOffile ="C:\\Users\\Dell\\Downloads\\PRITIFUSE.pdf"
isenable_uploadButton = driver.find_element(By.XPATH,"//label[text()='Upload resume']").is_enabled()
print(isenable_uploadButton)
enterData("//label[text()='Upload resume']",pathOffile)
#enterData("//input[@id='resume-upload-button']",pathOffile)
time.sleep(5)
print("Done....")