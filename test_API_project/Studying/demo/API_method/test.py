# !/user/bin/env python3
# -*- coding: utf-8 -*-
import requests

url = "http://182.42.242.69:30115/reLogin/login"
header = {"Content-Type":"application/json"}
data = {"username":"wkai","password":"shuFVE@kfD12","verifyCode":"2842","envId":"1","clusterId":"10"}
res = requests.post(url=url,json=data,headers=header)
token = "MPP_JSESSIONID" + res.text
# vars.put("token",token)
print(token)