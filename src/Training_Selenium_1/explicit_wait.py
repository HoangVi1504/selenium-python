# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://staging.hasaki.vn/")

# get element
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.block_app_topbar555"))
)

# print complete element
print(element)
print(element.text)

time.sleep(10)
