import time
import pytest
import requests


# get向导模式主流程
class Test_Case_dataservers:


    def setup(self):
        Test_Case_dataservers.Cookie = "SSO-Session=NmZlNzZlNjItMDU2My00ODhlLWFjYWItMzFkZjA2MjM2MGMz; gabdmp-access-token=9c9e7056-1d23-466e-8c31-c8fdf24e43bc; bdp-user-ticket-id=M7UZXQP9Ld2c9P9WbbQPsh5vCcNGs2fD2HLiVea4FcQ=; SESSION=NTQwYjBlN2EtNjQyYS00NDgwLWE2ZjktYmZlZTAwZGQwNDlh"
        Test_Case_dataservers.Authorization = "Bearer 9c9e7056-1d23-466e-8c31-c8fdf24e43bc"

    def teardown(self):
        print('测试结束')

    def test_获取数据源类型列表01(self):
        url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
        headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
        rep = requests.request("get", url=url,headers=headers)
        print("返回结果:", rep.json())
        code = rep.json()['data']
        print(code)


    # def test_获取数据源驱动列表02(self):
    #     url = "/gateway/iconnect-datasource/api/v1/datasource/plugin/"+Test_Case_dataservers.code+"/driver/list"
    #     headers = {"Content-Type": "application/json","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_链接测试03(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_新增数据源4(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_新增api分组5(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_创建get向导模式6(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_保存get向导模式配置信息7(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_测试api8(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_删除数据源9(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_删除api10(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())
    #
    # def test_删除api分组11(self):
    #     url = "http://datawings-test.ctcdn.cn:18000/gateway/iconnect-datasource/api/v1/datasource/plugin/list?withIcon=false&ability="
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Cookie":Test_Case_dataservers.Cookie,"Authorization":Test_Case_dataservers.Authorization}
    #     rep = requests.request("get", url=url,headers=headers)
    #     print("返回结果:", rep.json())




if __name__ == '__main__':
    pytest.main(["-vs"])
