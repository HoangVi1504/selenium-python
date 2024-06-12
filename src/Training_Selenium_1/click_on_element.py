# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# set implicit wait time
driver.implicitly_wait(10) # seconds

# get geeksforgeeks.org
driver.get("https://staging.hasaki.vn/")

# get element
# element = driver.find_element(By.LINK_TEXT, "Hasaki Deals")
element = driver.find_element(By.LINK_TEXT, "HASAKI DEALS")

# print complete element
print(element)
print(element.text)
time.sleep(3)
element.click()

time.sleep(10)