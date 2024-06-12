import time

from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://staging.hasaki.vn/")

# get source element
source_element = driver.find_element(By.XPATH, '//a[text()="Hasaki deals"]')
# get target element
target_element = driver.find_element(By.XPATH, '//a[text()="Hot deals"]')
time.sleep(3)
# create action chain object
action = ActionChains(driver)
# drag and drop the item
action.drag_and_drop(source_element, target_element)
# perform the operation
action.perform()

time.sleep(10)