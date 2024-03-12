import time

import requests





def test_api():
    url="http://182.42.228.170:18022/api/v1/dataapi/execute/post1"
    AppKey ="b0f420a4-20a2-4107-9ff5-02f0b74fa70b"
    AppSecret = "a1b9c3629fb52345817710ce58c52fd6"
    path = "/api/v1/dataapi/execute/post1"
    method = "POST"
    timestamp=time.localtime()
    data = ("id", "1")
    signature=(path,method,AppKey,timestamp,data,AppSecret)



    header = {
        AppKey:"AppKey",
        signature:"signature",
        timestamp:"timestamp"
    }
    rep=requests.request("post",url=url,data=data,headers=header)
    print(rep.json)