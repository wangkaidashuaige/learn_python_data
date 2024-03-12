from time import ctime, sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
print('测试时间:'+ctime())

driver.get('https://passport.meituan.com/useraccount/login')          # 美团~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-
driver.find_element(By.XPATH,"//*[@class='switch-mobile-btn']").click()# 选择登录
driver.find_element(By.XPATH,"//*[@class=' login-switch-btn']").click()# 选择用户名密码登录
driver.find_element(By.XPATH,"//*[@class='iLoginComp-phone-num-input']").send_keys('15981605527') # 手机号
driver.find_element(By.XPATH,"//*[@class='iLoginComp-code-input']").send_keys('wangkaishiniba1') # 密码
driver.find_element(By.XPATH,"//*[@class='agreement-rule-checkbox ']").click()   # 同意协议
driver.find_element(By.XPATH,"//*[@class='iLoginComp-login-btn-wrapper']").click() # 登录


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''百度----------------悬停设置'''
driver.get('https://baidu.com')
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')).perform() # 悬停设置

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''QQ邮箱~~~~~ ~定位frame '''
driver.get('https://mail.qq.com/')
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="login_frame"]'))      # webdriver 的方法定位frame
driver.find_element(By.XPATH,'//*[@id="u"]').send_keys('2421110201')
driver.find_element(By.XPATH,'//*[@id="p"]').send_keys('wangkaishiniba1')
driver.find_element(By.XPATH,'//*[@id="login_button"]').click()
driver.switch_to.default_content()                                                   # 返回之前的frame

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''## QQ邮箱~~~~~ ~发送附件 '''
driver.get('https://mail.qq.com/')
driver.find_element(By.XPATH,'//*[@id="composebtn"]').click()                        # 点击写信
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="mainFrame"]'))
driver.find_element(By.XPATH,'//*[@name="UploadFile"]').send_keys('E:\\learn_data\\testcases_api.xlsx') # 输入内容里面填写上传文件路径

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''## 百度~~~~~~-- ~键盘操作'''
driver.get('https://baidu.com')
driver.find_element(By.ID,"kw").send_keys('python1')    # 搜索python1
sleep(2)
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(Keys.BACK_SPACE)  # 使用一下删除键，删除最后一个数字
# # driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('python1'+Keys.BACK_SPACE) # 组合的方法（省事）



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#   # hao123-------------多窗口切换 '''
driver.get('https://www.hao123.com/?from=offline_host')
driver.find_element(By.XPATH,'//*[@id="govsite-top"]/a[1]').click() #第二个窗口
windows = driver.window_handles # 获取打开的多个窗口句柄
print(windows)
driver.switch_to.window(windows[-1]) # 切换到当前最新打开的窗口
driver.find_element(By.XPATH,'//*[@id="erjiV2Header"]/div[1]/div/div[4]/div[1]/a/em').click()   #点击注册

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''百度---------selenium模拟手机移动端测试'''
mobile = {"deviceName":"iPad"} # 定义硬件设备名字
options = webdriver.ChromeOptions() #定义一下webdriver.ChromeOptions()的方法
options.add_experimental_option ("mobileEmulation", mobile) # 使用add的方法添加，name、values
driver = webdriver.Chrome(chrome_options=options) # Chrome（）写好参数
driver.get ("http://m.baidu.com")
driver.find_element(By.XPATH,'//*[@id="index-kw"]').send_keys ("test")

