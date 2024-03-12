from time import ctime
from selenium import webdriver

from common import train_search, train_buy, train_buyinfo

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
print('测试时间:'+ctime())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''美团~~~~~~~~~定义函数'''
# def login(user,pwd):
#     driver.get('https://passport.meituan.com/useraccount/login')
#     driver.find_element(By.XPATH,"//*[@class='switch-mobile-btn']").click()# 选择登录
#     driver.find_element(By.XPATH,"//*[@class=' login-switch-btn']").click()# 选择用户名密码登录
#     driver.find_element(By.XPATH,"//*[@class='iLoginComp-phone-num-input']").send_keys(user) # 手机号
#     driver.find_element(By.XPATH,"//*[@class='iLoginComp-code-input']").send_keys(pwd) # 密码
# login('15981605527','wangkaishinba1')                                      # =====================引用函数赋值==================


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''导入common模块中的meituan_login函数，'''
# driver.get('https://passport.meituan.com/useraccount/login') # 美团~
'''调用自己写的函数，输入参数，点击执行'''
# meituan_login(driver,'15981605527','wangkaishiniba1')


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''去哪旅游网---------调用封装的函数'''
driver.get('https://www.qunar.com/')
train_search(driver,'上海','北京','2022-11-11')
train_buy(driver)
train_buyinfo('王凯','123456789','15981605527')






