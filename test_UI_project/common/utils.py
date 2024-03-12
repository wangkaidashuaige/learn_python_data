
import datetime
from time import sleep

import xlrd
from PIL import Image
from selenium.webdriver.common.by import By
from selenium import webdriver



# 多少天后
def dayslater(days):
    print(datetime.date.today() + datetime.timedelta(days=days)) # 当前日期+ 几天之后 = 多少天之后

# 按照列进行读取excel
def readexcel(path,col):
    xls = xlrd.open_workbook(path)# 打开文件路径赋值给xls
    sheet = xls.sheets()[0] # 找到工作铺
    print(sheet)            # 打印出工作铺
    list=[]                 # 以列组的格式展示
    for i in range(sheet.nrows):    #for循环
       list.append(sheet.cell(i,col).value) #历遍变量col（列数）
    return list

# 美团登录，
def meituan_login(driver,user,pwd):
         # 美团~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    driver.find_element(By.XPATH,"//*[@class='switch-mobile-btn']").click()# 选择登录
    driver.find_element(By.XPATH,"//*[@class=' login-switch-btn']").click()# 选择用户名密码登录
    driver.find_element(By.XPATH,"//*[@class='iLoginComp-phone-num-input']").send_keys(user) # 手机号
    driver.find_element(By.XPATH,"//*[@class='iLoginComp-code-input']").send_keys(pwd) # 密码
    driver.find_element(By.XPATH,"//*[@class='agreement-rule-checkbox ']").click()   # 同意协议
    driver.find_element(By.XPATH,"//*[@class='iLoginComp-login-btn-wrapper']").click() # 登录
# 搜索车票
def train_search(driver,fromstation,tostation,datastation):
    driver.find_element(By.NAME,'fromCity').send_keys(fromstation)
    sleep(2)
    driver.find_element(By.NAME,'toCity').send_keys(tostation)
    sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[1]/input').clear()
    sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[1]/input').send_keys(datastation)
    sleep(2)
    driver.find_element(By.CLASS_NAME,'button-search').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME,'btn').click()
# 购买车票
def train_buy(driver):
    driver.find_element(By.XPATH,'//*[@id="content"]/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div[2]/p').click()
    sleep(2)
    driver.find_element(By.XPATH,'//*[@id="content"]/div/div[4]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[1]/div/div[3]/button/span').click()
# 填写购票信息
def train_buyinfo(driver,name,ID_number,mobile):
    driver.find_element(By.CLASS_NAME,'js-passenger-name').send_keys(name)
    sleep(2)
    driver.find_element(By.CLASS_NAME,'js-cert-number"').send_keys(ID_number)
    sleep(2)
    driver.find_element(By.NAME,'driver.find_element').send_keys(mobile)

# 胡作非为_login
def Fabrie_login(driver,user,psw):
    driver.find_element(By.ID,"fabrie-account-str-pwd-login").send_keys(user)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div[2]/form/div[2]/div/div/input').send_keys(psw)
    driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/div[1]/div/div[2]/form/div[3]/div/button").click()