#https://www.amazon.in/Storio-Junior-Cricket-Plastic-Birthday/dp/B0F7FKVNXM/?_encoding=UTF8&pd_rd_w=m32LZ&content-id=amzn1.sym.fa294cf3-99e4-435e-8284-16ec3b3e2443%3Aamzn1.symc.752cde0b-d2ce-4cce-9121-769ea438869e&pf_rd_p=fa294cf3-99e4-435e-8284-16ec3b3e2443&pf_rd_r=QACXAE2FN8BSZHDDRAX5&pd_rd_wg=UUKLl&pd_rd_r=4e8bd0c6-16c1-43b3-bf7d-b6adf5509daa&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1


import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.amazon.in/Storio-Junior-Cricket-Plastic-Birthday/dp/B0F7FKVNXM/?_encoding=UTF8&pd_rd_w=m32LZ&content-id=amzn1.sym.fa294cf3-99e4-435e-8284-16ec3b3e2443%3Aamzn1.symc.752cde0b-d2ce-4cce-9121-769ea438869e&pf_rd_p=fa294cf3-99e4-435e-8284-16ec3b3e2443&pf_rd_r=QACXAE2FN8BSZHDDRAX5&pd_rd_wg=UUKLl&pd_rd_r=4e8bd0c6-16c1-43b3-bf7d-b6adf5509daa&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1"
driver.get(url)
time.sleep(3)
driver.maximize_window()
def entertext(xpath, data):
     driver.find_element(By.XPATH,xpath).clear()
     driver.find_element(By.XPATH, xpath).send_keys(data)

def getText(xpath):
    textnew = driver.find_element(By.XPATH,xpath).text
    return textnew


print(getText("//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']"))

print(getText("//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/child::span[2]/span[2]"))
# entertext("//*[text()='First Name ']/following::input[1]","priti")


elements = driver.find_elements(By.XPATH, "//span[contains(text(), '298')]")
print(len(elements))
# for el in elements:
#     print(el.text)

time.sleep(2)
print("done....")