from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start a browser session (make sure you have the correct WebDriver installed)
driver = webdriver.Chrome()  # or Firefox, Edge, etc.

# Load your target web page
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.maximize_window()
time.sleep(3)

# Find all elements using a universal selector '*'
all_elements = driver.find_elements(By.CSS_SELECTOR, "*")

# Print each element's tag name
for element in all_elements:
    try:
        print(element.tag_name)
    except Exception as e:
        print("Error retrieving tag:", e)

# Close the browser
driver.quit()
