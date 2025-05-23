from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
url = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
driver.get(url)
def writeIn(by, desc,data):
    print("in writeIn.......")
    wait = WebDriverWait(driver, 15)
    by = by.upper()
    if by == 'ID':
        wait.until(EC.element_to_be_clickable((By.ID, desc)))
        driver.find_element(By.ID,desc).send_keys(data)
    elif by == 'XPATH':
        wait.until(EC.element_to_be_clickable((By.XPATH, desc)))
        driver.find_element(By.XPATH,desc).send_keys(data)
    elif by=='Name':
        wait.until(EC.element_to_be_clickable((By.NAME, desc)))
        driver.find_element(By.NAME, desc).send_keys(data)

def clickElement(by, desc):
    print("in click ...")
    wait = WebDriverWait(driver, 15)
    by = by.upper()
    if by == 'ID':
        wait.until(EC.element_to_be_clickable((By.ID, desc)))
        driver.find_element(By.ID,desc).click()
    if by == 'XPATH':
        # print("in click xpath...")
        wait.until(EC.element_to_be_clickable((By.XPATH, desc)))
        driver.find_element(By.XPATH,desc).click()


#Student Registration Form
#Enter Name
writeIn('XPATH','//input[@id="name"]','priti')

# clickElement('XPATH',"(//input[@type='radio'])[1]")
clickElement('XPATH','//label[text()="Male"]//ancestor::div/input')
clickElement('XPATH','//label[text()="Female"]//ancestor::div/input')
clickElement('XPATH','//label[text()="Other"]//ancestor::div/input')

# time.sleep(3)
print("Done ... !!")
time.sleep(2)