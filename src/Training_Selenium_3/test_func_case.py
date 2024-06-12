from selenium import webdriver
from selenium.webdriver.common.by import By


def test_check_element_failed_success():
    driver = webdriver.Chrome()
    driver.get("https://staging.hasaki.vn/")
    element = driver.find_element(By.LINK_TEXT, 'HASAKI DEALS')
    assert element.text != 'Hasaki deals'
    driver.quit()


def test_check_element_success():
    driver = webdriver.Chrome()
    driver.get("https://staging.hasaki.vn/")
    element = driver.find_element(By.LINK_TEXT, 'HASAKI DEALS')
    assert element.text == 'HASAKI DEALS'
    driver.quit()