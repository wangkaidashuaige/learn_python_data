# 数据安全TEST
from time import sleep

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''-----------对元素截图操作-需pip install Pillow'''
''''''''''''''''''''''''''''''''''好使'’'''''''''''''''''''''''''''''''''''''''''''''''''' csdn中演示的代码-截取元素验证码截图'''
width = driver.get_window_size().get("width")
print(width)
driver.get('http://101.227.34.238:31943/login?redirect=%2Fdatasource%2Fdbsource')    # 数据安全地址
driver.save_screenshot('dsmp_login1.png') # 对页面全屏截屏
element = driver.find_element(By.XPATH,"//*[@id='app']/div/form/div[3]/div/div[2]/img") # 数据安全验证码元素
print(element.location)  # 打印元素坐标
print(element.size)  # 打印元素大小
left = element.location['x']
top = element.location['y']
right = (element.location['x'] + element.size['width'])
bottom = (element.location['y'] + element.size['height'])
im = Image.open('../case/dsmp_login1.png')
i = im.size
p = i[0]
n = p / width
im = im.crop((left * n, top * n, right * n, bottom * n))
im.save('dsmp_code1.png')


''''''''''''''''''''''''''''''''''’''''''''''''''''''''''''''''''''''''''''''''''''''''''''‘’‘’‘’‘’‘’‘’‘’‘’'' 提取验证码值'''
# str ='predict succ ret: 0 request_id: 20221114100050a1d085d30005c05c44 pred: 24 err:'
# beg = str.find('pred:') # 找到验证码的前位置
# beg1 = str.find('err')  # 找到验证码的后位置
# print(beg)
# print(beg1)
# print(str[beg+5:beg1].lstrip())# .lstrip()消除空格的方法


