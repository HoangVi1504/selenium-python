# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://staging.hasaki.vn/")

# get element
element = driver.find_elements(By.XPATH, '//*[text()="Hasaki deals"]')

print(element)
print(element.text)

time.sleep(10)
