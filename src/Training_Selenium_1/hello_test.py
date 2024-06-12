from selenium import webdriver


chrome_driver = webdriver.Chrome()
chrome_driver.get("https://hasaki.vn/")


firefox = webdriver.Firefox()
firefox.get("https://staging.hasaki.vn/")

print('test')
