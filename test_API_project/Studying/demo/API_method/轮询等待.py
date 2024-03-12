import time
# -*- coding: utf-8 -*-
import requests

# 定义轮询等待的函数
# 循环判断响应状态码，错误的时候重试，最大次数3次，最后抛出异常
def test_poll_and_wait(retries=0,max_retries=3, interval=1):
    url1 = "http://datawings.test.cn:18100/gateway/securityapi/detection/api/rule"
    data = {"page":0,"size":10,"sort":"id%2Cdesc"}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    cookies = {'Authorization' : 'Bearer 88299052-0c87-4454-a1e8-a89f8c528bd1'}
    respones = requests.get(url1, params=data, headers=headers, cookies=cookies)
    print("状态码:",respones.status_code)
    # 使用 while 循环进行轮询，最多重试 max_retries 次
    while retries < max_retries:
        # 检查条件是否满足
        if respones.status_code == 401:
            print("条件满足，继续执行后续操作。")
            break  # 如果条件满足，跳出循环
        else:
            # 如果条件未满足，等待一段时间后进行下一次轮询
            print(f"条件未满足，等待 {interval} 秒后继续轮询...")
            time.sleep(interval)  # 使用 time.sleep 函数进行等待
            retries += 1  # 增加重试次数

    else:
        # 如果达到最大重试次数仍然条件未满足，输出提示信息
        print("达到最大重试次数，退出轮询。")

# 判断响应响应状态码，处理异常，没有循环
def test_try():
    try:
        url1 = "http://datawings.test.cn:18100/gateway/securityapi/detection/api/rule"
        data = {"page": 0, "size": 10, "sort": "id%2Cdesc"}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'Authorization': 'Bearer 88299052-0c87-4454-a1e8-a89f8c528bd1'}
        respones = requests.get(url1, params=data, headers=headers, cookies=cookies)
        data = respones.status_code
        print("状态码:", data)
        if data == 401:
            print("状态码:",data)
        else:
            print("请求失败，状态码:",data)
    except requests.exceptions.RequestException as e:
        print("请求出错",e)



# test
def num(cishu=0,zuidacishu=3,times=1):
    response = requests.get(url="rul")
    code = response.status_code
    while zuidacishu <= 3:
        while code == 200:
            print("继续执行下一句")
            break
    else:
        print(f"不行，状态码不对，在等{times}秒")


