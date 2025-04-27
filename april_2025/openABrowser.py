import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome browser using WebDriver Manager (auto handles driver setup)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# Open a website
driver.get(url)

# Optional: Maximize the browser window
driver.maximize_window()
time.sleep(3)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
try:
    print("intryyy")
    myele = driver.find_elements(By.TAG_NAME, "p")
    print(len(myele))
    print(myele[0].text)
    myele[0].click()
    time.sleep(1)
    logoutLink = driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]")
    print("logoutlink=  ",logoutLink.is_displayed())
    logoutLink.click()
    #for i in myele:
    #    print(i.text)
    #myele.click()
except:
    pass

#logoutLink=driver.find_element(By.XPATH("//a[contains(@href,'logout')]")).is_displayed()
#print(logoutLink)
#input("Press ENTER to close the browser...")

time.sleep(16)

