from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
try:
    driver.find_element(By.ID,"testtwee").send_keys("test")
except Exception as e:
    print(e)
driver.find_element(By.ID,"kw").send_keys("testtest1233")
#代码加上异常