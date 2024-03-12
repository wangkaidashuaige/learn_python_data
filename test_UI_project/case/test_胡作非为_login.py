from selenium import webdriver
import pytest
from time import time,ctime,sleep
from common.utils import Fabrie_login



class Test_login:


    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.fabrie.cn/login")

    def teardown_class(self):
        print("测试时间：", ctime())
        print("结束呦西")

    def test_success_login01(self):
        Fabrie_login(self.driver,'15981605527','wangkaishiniba1!')
        sleep(2)
        title=self.driver.title
        # print(title)
        assert title == "Fabrie - 设计师的在线设计协作平台 | 融合表格的在线白板工作台"
        self.driver.quit()

    def test_mobilefail_login02(self):
        Fabrie_login(self.driver,'15981609999','wangkaishiniba1!')
        sleep(2)
        title=self.driver.title
        # print(title)
        assert title == "登录 | Fabrie - 设计师的在线设计协作平台"
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()