import requests


class Test_api:
    # 全局变量
    token = ''

    # app用户登入
    def test_apptoken(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal/v1/appuser/appLogin"
        # 密码有MD加密
        json = {
            "phoneNumber": "17637932770",
            "password": "e10adc3949ba59abbe56e057f20f883e",
            "loginType": "2"
        }
        raw = requests.post(url=url, json=json)
        # Test_api.access_token = raw.json()['access_token']
        #token = raw.json()["token"]
        data = raw.json()
        for i in data.values():
                print(i)

