# Python program to demonstrate
# selenium
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
# set implicit wait time
driver.implicitly_wait(10) # seconds

# get geeksforgeeks.org
driver.get("https://staging.hasaki.vn/#popup-login")

time.sleep(10)
#anchor