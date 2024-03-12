import unittest
from time import sleep, ctime
from selenium import webdriver
from common.fateadm_api import TestFunc
from common.function import dsmp_login
from common.function import codeimage


class Test_dmsp(unittest.TestCase):
    def setUp(self):
        print('测试时间:', ctime())
        self.driver = webdriver.Chrome()
        self.url = 'http://101.227.34.238:31943/'
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def test_dsmp_login1(self): # 登录正确
        self.driver.get(self.url)
        codeimage(self.driver)  # 调用codeimage函数，获取验证码截图
        r = TestFunc()  # 调用TestFunc函数，获取验证码截图的值，并赋值 r
        dsmp_login(self.driver, 'ceshi1', 'Ct$Ad@20.', r) # 调用数据安全登录函数，
        sleep(2)
        title = self.driver.title
        print(title)
        self.assertEqual(title,'工作空间 - 数据安全管理平台')

    @unittest.skip('不需要测试该用例')
    def test_dsmp_login2(self):
        self.driver.get(self.url)
        codeimage(self.driver)  # 调用codeimage函数，获取验证码截图
        r = TestFunc()  # 调用TestFunc函数，获取验证码截图的值，并赋值 r
        dsmp_login(self.driver, 'ceshi1', 'Ct$Ad@20.', r)  # 调用数据安全登录函数，
        sleep(2)
        title = self.driver.title
        print(title)
        self.assertEqual(title, '工作空间 - 数据安全管理平台')


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()