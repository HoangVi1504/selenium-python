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

# set implicit wait time
driver.implicitly_wait(10) # seconds

# get geeksforgeeks.org
driver.get("https://staging.hasaki.vn/")

# get element
element = driver.find_element(By.CSS_SELECTOR, "div.block_app_topbar555")

# print complete element
print(element)
print(element.text)

time.sleep(10)
