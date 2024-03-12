import pytest
import requests

class Test_fixtrue1:
    @pytest.fixture()
    def test_get_dsmp_list(self): # 获取数据安全——敏感数据发现-识别规则列表
        url = "http://datawings.ctcdn.cn:18000/gateway/securityapi/detection/api/rule?page=0&size=10&sort=id%2Cdesc"
        params = {"page":"0","size":"10","sort":"id,desc"}
        # data={"username":"automation_poc","password":"e0une-Se5R#gPp"}
        # "Content-Type": "application/x-www-form-urlencoded",
        headers={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxOSwidXNlcl9rZXkiOiI0Yjc0MGY0NC1jZDJiLTQ2ZjMtYTM3OS1mNDQ1YTJjZjYwZmIiLCJ1c2VybmFtZSI6ImF1dG9tYXRpb25fcG9jIn0.olcIl-vdZ-dDKUgzQ1V10Dn7L5q0qTRBZva9KdY9JoklyRM-XGI_WK6uZcrDFBG5fVjyAsCIVP2QTQritQxRSQ",
                 "Cookie":"cdn_tgc=50bb2531-b9f9-4e75-99c4-a3e0fe17c144; SSO-Session=MmE3ZDAwZWYtNzMzNi00YjJhLTkzNmQtZDExN2NiNmMyMGRk; gabdmp-access-token=7bdd2e46-7c3a-44b4-8da4-6f1ff25101fc; DSP-TOKEN=Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxOSwidXNlcl9rZXkiOiI0Yjc0MGY0NC1jZDJiLTQ2ZjMtYTM3OS1mNDQ1YTJjZjYwZmIiLCJ1c2VybmFtZSI6ImF1dG9tYXRpb25fcG9jIn0.olcIl-vdZ-dDKUgzQ1V10Dn7L5q0qTRBZva9KdY9JoklyRM-XGI_WK6uZcrDFBG5fVjyAsCIVP2QTQritQxRSQ"}
        res = requests.get(url=url,params=params,headers=headers)
        # print(res.json())
        info = res.json()
        id = info['content'][0]['id']
        return id
    def test_example(self, test_get_dsmp_list):  # test_get_dsmp_list当做参数传入下一个方法函数当中
        # 这是一个示例测试用例，使用 test_get_metersphere_login fixture
        print(test_get_dsmp_list)