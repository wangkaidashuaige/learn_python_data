import requests
import base64
import re
import pytest
from common.fateadm_api import TestFunc
import json


class Test_Case_login:

    def test_login_成功登录01(self):
        # 首页通过正则，获取uuid,img
        code = requests.get('http://101.227.34.238:31943/dsp/system/auth/code')
        res = code.content.decode()
        print('返回结果：',res)
        uuid = re.findall(r'"uuid":"(.*?)"', res, re.S)[0]
        img = re.findall(r'"img":"data:image\/png;base64,(.*?)"', res, re.S)
        print("返回Uuid：",uuid)
        print("返回img：",img)
        # 通过base64把img中base64数据转换成图片，重复写入文件中。
        bt = base64.b64decode(img[0])
        png = open("/image/dsmp_code1.png", "wb+")
        png.write(bt)
        png.close()

        url = 'http://101.227.34.238:31943/dsp/system/auth/user/login'
        headers = {"Content-Type": "application/json"}
        # 调用第三方接口计算验证码
        r = TestFunc()
        data = json.dumps({
            "username": "ceshi1",
            "password": "FuwBfYee2Z2MRqWshKrF9hi+lcrrXlnR0PLMhsymKkMPhCY100sZjrmcBr+Pe3ZQNd0TYY5aiwtPzFPhFKBaUA==",
            "code": r,
            "uuid": uuid,
            "loginType": "generalUser"
        })
        rep = requests.request('post',url=url, data=data, headers=headers)
        print(rep.json())
        assert "user" in rep.json()



if __name__ == '__main__':
    pytest.main()