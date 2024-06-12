from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginHasaki: #Remember to add Test before Class name
    def test_check_element_failed(self):
        # create webdriver object
        driver = webdriver.Chrome()
        # get geeksforgeeks.org
        driver.get("https://staging.hasaki.vn/")
        # get element
        element = driver.find_element(By.LINK_TEXT, 'HASAKI DEALS')
        assert element.text == 'Hasaki deals'
        # time.sleep(3)
        driver.quit()

    def test_check_element_success(self):
        # create webdriver object
        driver = webdriver.Chrome()
        # get geeksforgeeks.org
        driver.get("https://staging.hasaki.vn/")
        # get element
        element = driver.find_element(By.LINK_TEXT, 'HASAKI DEALS')
        assert element.text == 'HASAKI DEALS'
        # time.sleep(3)
        driver.quit()
