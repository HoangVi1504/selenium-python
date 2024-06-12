# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

driver.get("https://staging.hasaki.vn/")

# get element 
element = driver.find_element(By.ID, "v3_wrapper_container")

# print complete element
print(element)
print(element.text)
time.sleep(10)
