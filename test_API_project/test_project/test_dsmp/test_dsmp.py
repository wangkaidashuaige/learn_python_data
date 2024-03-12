# !/user/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import requests

@pytest.fixture
class Test_oracle:
    def test_敏感数据发现(self):
        url = ""
        params_data = {}
        headers = {"Content - Type": "application/json","Authorization": ""}
        respones = requests.get(url,params= params_data,headers=headers)
        print(respones.text)
