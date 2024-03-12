import time
import pytest
import requests
from common.Hmac_sha256 import get_sha256



# 动态脱敏
class Test_Case_datamask:
    
    def test_datamask_成功脱敏(self):
        url = "http://101.227.34.238:31943/dsp/system/http/api/httpDataMask/execDataMask"
        accessKey = "6wULrs3PA2w4g21MUNBkpXAUY4PbqzjqiVjZylNQlIc"
        securityKey = "cQuLkPqVl-4fh-f6iADGAsvgs5Log6freWmEz4boXgU"
        data = {'dataHeaderList':['name','age','phone','mail'],'dataList':[['张三',18,'17853303959','9323566@qq.com'],['李四',17,'13325120526','38178947@sina.cn']],'strategyUuid':'9303d08480214006a14b6e84f554f798'}

        headers = {"Content-Type":"application/json"}
        # timestamp = (int(time.time()*1000)) # 时间戳
        timestamp = str(int (time.time()))
        # timestamp = timestamp + str(1211) # 时间戳超时120秒
        metasign = accessKey+"@"+timestamp # 获取变化的签名metasign,没有加密的签名
        Sign = get_sha256(metasign,securityKey)     # 获取本地签名localSign--使用未加密的签名+securityKey本地的私钥，传给后端校验，验证localsign签名的合法性

        params = {"accessKey":accessKey,"timeStamp":timestamp,"sign":Sign, "data":data}
        rep = requests.request("post",url=url,json=params,headers=headers)
        print("请求参数:", params)
        print("返回结果:", rep)
        print("返回结果:", rep.text)
        print("返回结果:",rep.reason)
        print("返回结果:",rep.content.decode("utf-8"))
        print("返回结果:",rep.json())
        print("返回结果:", rep.encoding)
        print("返回结果:", rep.headers)


if __name__ == '__main__':
    pytest.main(["-vs"])
