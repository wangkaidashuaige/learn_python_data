from time import sleep
import pytest
from selenium import webdriver
from PO_.loginpage import LoginPage



class Test01:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.fabrie.cn/login')
        print("开始测试")
    def teardown(self):
        self.driver.quit()
        print("结束测试")
    def test_login01(self):
        log=LoginPage(self.driver)
        log.login('15981605527','wangkaishiniba1!')
        title = self.driver.title
        print(title)
        assert title == '登录 | Fabrie - 设计师的在线设计协作平台'
        sleep(1)

if __name__ == '__main__':
    pytest.main()