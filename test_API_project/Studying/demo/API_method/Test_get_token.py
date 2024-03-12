# -*- coding: utf-8 -*-
import json

import pytest
import requests


class Test_dsmp_login:
    @pytest.fixture()
    def test_login_get_SSO_session(self):
        url = "http://datawings.ctcdn.cn:18000/gateway/ddaf-authserver/sso/datawings/login"
        headers = {
            "Content-Type":"application/json"
        }
        data = {"name":"automation_poc","password":"e0une-Se5R#gPp","code":"rvvp"}
        response = requests.post(url,json = data,headers=headers)
        # print("打印cookies",response.cookies)
        # print("打印打印请求头",response.headers)
        print("打印请求头中的Set-Cookie",response.headers['Set-Cookie'])
        print("打印请求头",response.request.headers)
        # a=1234;,通过split函数进行分割，前面截取“=”，后面截取";"
        cookies_split = response.headers['Set-Cookie'].split("=")
        SSO_session = cookies_split[1].split(";")[0]
        print("获取SSO_session:",SSO_session)

    def test_login_get_DSP_token(self):
        url = "http://datawings.ctcdn.cn:18000/gateway/ddaf-authserver/oauth/authorize?client_id=dsp&response_type=code&state=STATE&redirect_uri=http://datawings.ctcdn.cn:18000/gateway/securityapi/auth/middleplatform/token/?redirect=http://datawings.ctcdn.cn:18000/security/category/template"
        response = requests.get(url)
        print("打印",response.request.headers['cookie'])
        cookies = response.request.headers['cookie']
        SSO2_session=cookies.split("=")[1]
        print("获取SSO2_session:",SSO2_session)

    def test_login_get_security_token(self):
        url = "http://datawings.ctcdn.cn:18000/gateway/securityapi/home/api/page/getDatasourceInfo"
        res = requests.get(url)
        print("安全的返回:",res.request.headers)
    def test_login_get_index_token(self):
        url = "http://datawings.ctcdn.cn:18000/gateway/ddaf-authserver/api/v2/user"
        res = requests.get(url)
        print("安全的返回:",res)

if __name__ == '__main__':
    pytest.main()