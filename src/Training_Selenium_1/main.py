from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://staging.hasaki.vn/#popup-login")
driver.implicitly_wait(3)
user_name = driver.find_element(By.ID, "username")
user_name.send_keys("0332333444")
password = driver.find_element(By.ID, "password")
password.send_keys("123456")
btn_login = driver.find_element(By.XPATH, "//button[text()='Đăng nhập']")
btn_login.click()

# get element by ID
el = driver.find_element(By.XPATH, "//*[@id='v3_wrapper_container']")
print(el.text)

# get element by name
el = driver.find_element(By.XPATH, "//*[@name='q']")
print(el.text)

# get element by text
el = driver.find_element(By.XPATH, "//*[text()='Flash Deals']")
print(el.text)