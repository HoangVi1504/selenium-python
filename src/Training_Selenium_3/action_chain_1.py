import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

driver.get("https://staging.hasaki.vn/")

# get element
element = driver.find_element(By.XPATH, '//div[@class="item_header item_login "]')

inside_element = element.find_element(By.XPATH, './/a[@id="hskLoginButton"]')

actions = ActionChains(driver)
actions.move_to_element(element)
actions.click(inside_element)
actions.perform()

time.sleep(5)

account = driver.find_element(By.ID, "username")
passw = driver.find_element(By.ID, "password")
button = driver.find_element(By.XPATH, '//*[@id="form-head-login"]/button')
# click the username
actions.click(on_element=account)
actions.send_keys("hangdoan11101986@gmail.com")
# click the password
actions.click(on_element=passw)
actions.send_keys("12345678")
#
actions.move_to_element(button)
actions.click()
actions.perform()

time.sleep(10)
