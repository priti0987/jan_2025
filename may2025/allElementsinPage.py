from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

# Start a browser session (make sure you have the correct WebDriver installed)
driver = webdriver.Chrome()  # or Firefox, Edge, etc.

# Load your target web page
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.maximize_window()
time.sleep(3)

# Find all elements using a universal selector '*'
# all_elements = driver.find_elements(By.CSS_SELECTOR, "*")

# Print each element's tag name
# for element in all_elements:
#     try:
#         print("tag of element ",element.tag_name)
#     except Exception as e:
#         print("Error retrieving tag:", e)

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

# clickElement('XPATH','(//a[contains(@href,"customer/login")])[2]')
writeIn('XPATH','//input[@name="email"]','priti')
writeIn('XPATH','//input[@name="Password"]','password')
writeIn('XPATH','//input[@name="company"]','companYY')
writeIn('XPATH','//input[@name="mobile number"]','9988774455')

time.sleep(2)
clickElement('XPATH',"//button[@value='Submit']")
time.sleep(2)
writeIn('ID','inp_val','ok')

# Close the browser
driver.quit()
