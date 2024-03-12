import base64
import datetime
import re

import requests
import xlrd
from PIL import Image
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome
# 截取验证码截图
def codeimage(driver):
    width = driver.get_window_size().get("width")
    print(width)
    driver.get('http://101.227.34.238:31943/auth/user/login')  # 数据安全地址
    driver.save_screenshot('D:\\test_API_project\\image\\dsmp_login1.png')
    element = driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[3]/div/div[2]/img")  # 数据安全验证码元素
    print(element.location)  # 打印元素坐标
    print(element.size)  # 打印元素大小
    left = element.location['x']
    top = element.location['y']
    right = (element.location['x'] + element.size['width'])
    bottom = (element.location['y'] + element.size['height'])
    im = Image.open('D:\\test_API_project\\image\\dsmp_login1.png')
    i = im.size
    p = i[0]
    n = p / width
    im = im.crop((left * n, top * n, right * n, bottom * n))
    im.save('D:\\test_API_project\\image\\dsmp_code1.png')



# # 按照列进行读取excel
# def readexcel(path,col):
#     xls = xlrd.open_workbook(path)# 打开文件路径赋值给xls
#     sheet = xls.sheets()[0] # 找到工作铺
#     print(sheet)            # 打印出工作铺
#     list=[]                 # 以列组的格式展示
#     for i in range(sheet.nrows):    #for循环
#        list.append(sheet.cell(i,col).value) #历遍变量col（列数）
#     return list
#
#
# # 数据安全登录接口获取uuid、img
# def getcode(uuid,img):
#     # 首页通过正则，获取uuid,img
#     code = requests.get('http://101.227.34.238:31943/dsp/system/auth/code')
#     res = code.content.decode()
#     print('返回结果：', res)
#     uuid = re.findall(r'"uuid":"(.*?)"', res, re.S)[0]
#     img = re.findall(r'"img":"data:image\/png;base64,(.*?)"', res, re.S)
#     print("返回Uuid：", uuid)
#     print("返回img：", img)
#
#
