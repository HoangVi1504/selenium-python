# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://staging.hasaki.vn/san-pham/phan-ma-hong-08-peach-rock-5g-8235.html")

# get element
element = driver.find_element(By.LINK_TEXT, "Thông tin sản phẩm")

# print complete element
print(element)
print(element.text)
# ----------------------------------

element2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Thông tin")

# print complete element
print(element)
print(element.text)

time.sleep(10)
