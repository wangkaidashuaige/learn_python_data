import requests


class Test_api:
    # 全局变量
    token = '3fe64d7b260488b8c3e1d5d3c4de1669'
        #app用户登入
    def test_apptoken(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal/v1/appuser/appLogin"
        # 密码有MD加密
        json = {
         "phoneNumber":"17637932770",
        "password":"e10adc3949ba59abbe56e057f20f883e",
         "loginType":"2"
        }
        raw = requests.post(url=url, json=json)
        #Test_api.access_token = raw.json()['access_token']
        print(raw.json())

    # 新增评价
    #@pytest.mark.parametrize()
    def test_pingjia(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal/v1/evaluation/addEvaluationInfo"
        headers = {"Authorization": Test_api.token}
        json = {
            "score": "1",
            "comment": "非常棒",
            "chargeOrderCode": "C2211141038003106041",
            "deviceNumber": "TEST100151"
        }
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        # 分页查询反馈列表内容

    def test_fenyechaxunliebiaoneirong(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal/v1/feedback/selectFeedbackInfo"
        headers = {"Authorization": Test_api.token}
        json = {
            "currentPage": "1",
            "pageNumber": "2"
        }
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        # 新增车牌

    def test_xinzhengchepai(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal//v1/car/addCarNumber"
        headers = {"Authorization": Test_api.token}
        json = {
            "carNumber": "10086",
            "carBrand": "吉利",
            "carModel": "c",
            "vinNo": "10010",
            "manual": "true"
        }
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '当前车牌号已经存在'
        # 车牌列表

    def test_chepailiebiao(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal/v1/car/listCarNumber"
        headers = {"Authorization": Test_api.token}
        json = {
            "无": "10086"
        }
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        # 充电页面信息确认

    def test_chongdianyemianxinxiqueren(self):
        url = "https://cloud-api-pre.vremtglobal.com/charge/v1/charge/chargeBasicInfo"
        headers = {"Authorization": Test_api.token}
        json = {
            "Authorization": Test_api.token
        }
        raw = requests.get(url=url, data=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '设备不存在'
        # 流水记录
    def test_liushuijilu(self):
        url="https://cloud-api-pre.vremtglobal.com/personal/v1/user/MineBalanceStream"
        headers = {"Authorization": Test_api.token}
        json = {
        }
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        #我的消息列表
    def test_wodexiaoxiliubiao(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal/v1/user/messageList"
        headers = {"Authorization": Test_api.token}
        json = {
        }
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        #微信退款前的鉴权
    def test_weixintuikuanqiandejianquan(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal/v1/weixin/pay/refundAuthen"
        headers = {"Authorization": Test_api.token}
        json = {"cardId":"111"}
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['title'] == '微信退款失败'
        #发票详情
    def test_fapiapoxiangqing(self):
        url ="https://cloud-api-pre.vremtglobal.com/invoice/v1/invoice/invoiceDetail"
        headers = {"Authorization": Test_api.token}
        json ={"invoiceId":"10086"}
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '获取开票信息失败，请稍后重试或联系客服了解详细原因'
        #发票抬头输入栏模糊联想
    def test_fapiao(self):
        url = "https://cloud-api-pre.vremtglobal.com/invoice/v1/invoice/historyInvoiceDetail"
        headers = {"Authorization": Test_api.token}
        json = {"prefixName":"100","mode":"2"}
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        #发聩
    def test_fankui(self):
        url = "https://cloud-api-pre.vremtglobal.com/personal/v1/user/feedback"
        headers = {"Authorization": Test_api.token}
        json = {"feedbackType":1,       #如果设置成0（建议就报错）   设置成1(报修)就成功
                "message": "反馈 反馈"}
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        #历史发票抬头展示
    def test_lishifapiaotaitou(self):
        url = "https://cloud-api-pre.vremtglobal.com/invoice/v1/invoice/historyInvoiceTitle"
        headers = {"Authorization": Test_api.token}
        json = {}
        raw = requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        #历史发票列表
    def test_lishifapiaoliebiao(self):
        url = "https://cloud-api-pre.vremtglobal.com/invoice/v1/invoice/historyInvoiceList"
        headers = {"Authorization": Test_api.token}
        json = {}
        raw =requests.post(url=url, json=json, headers=headers)
        print(raw.json())
        assert raw.status_code == 200
        assert 'msg' in raw.json()
        assert raw.json()['msg'] == '成功'
        #列表展示卡包
    def test_liebiaozhanshikabao(self):
        url = 'https://cloud-api-pre.vremtglobal.com/personal/v1/card/whole'
        headers = {"Authorization": Test_api.token}
        json = {
            "pageNumber": "1",           #当前页
        }
        raw =requests.post(url=url, json=json, headers=headers)
        print(raw.json())


