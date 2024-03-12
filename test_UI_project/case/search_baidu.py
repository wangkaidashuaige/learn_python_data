from selenium import webdriver
from time import sleep,ctime
import unittest
from selenium.webdriver.common.by import By


print('测试时间:'+ctime())
class Testbaidu(unittest.TestCase):
    def setUp(self):#  每个方法执行一次
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com"
        self.driver.maximize_window()


    def test_search_key_selenium(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input").send_keys("selenium")
        self.driver.find_element(By.ID,"su").click()
        sleep(3)
        title = self.driver.title
        self.assertEqual(title,'selenium_百度搜索')

    def test_search_key_unittest(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID,'kw').send_keys('unittest')
        self.driver.find_element(By.ID,'su').click()
        sleep(3)
        title = self.driver.title
        self.assertEqual(title,'unittest_百度搜索')


    def tearDown(self) :# 每个方法最后都执行一次
        self.driver.quit()
if __name__ =='__main__':
    unittest.main()

