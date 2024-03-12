from time import sleep

from PIL import Image
from selenium import webdriver

from common.log import framelog
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



lo = framelog()
log = lo.log()
# 数据安全登录
def dsmp_login(driver,username,psw,code):
    log.info('username')
    driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[1]/div/div/input').send_keys(username)
    log.info('psw')
    driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[2]/div/div/input').send_keys(psw)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[3]/div/div[1]/input').send_keys(code)
    log.info('code')
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/form/label/span[1]/span').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[4]/div/button').click()


driver = webdriver.Chrome
# 截取验证码截图
def codeimage(driver):
    width = driver.get_window_size().get("width")
    print(width)
    driver.get('http://101.227.34.238:31943/login?redirect=%2Fdatasource%2Fdbsource')  # 数据安全地址
    driver.save_screenshot('D:\\test_UI_project\\image\\dsmp_login1.png')
    element = driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[3]/div/div[2]/img")  # 数据安全验证码元素
    # print(element.location)  # 打印元素坐标
    # print(element.size)  # 打印元素大小
    left = element.location['x']
    top = element.location['y']
    right = (element.location['x'] + element.size['width'])
    bottom = (element.location['y'] + element.size['height'])
    im = Image.open('D:\\test_UI_project\\image\\dsmp_login1.png')
    i = im.size
    p = i[0]
    n = p / width
    im = im.crop((left * n, top * n, right * n, bottom * n))
    im.save('D:\\test_UI_project\\image\\dsmp_code1.png')
#
# def Fabrie_login(driver, user, psw):
#     driver.find_element(By.ID, "fabrie-account-str-pwd-login").send_keys(user)
#     driver.find_element(By.XPATH,
#                             '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/form/div[2]/div/div/input').send_keys(psw)
#     driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[1]/div/div[2]/form/div[3]/div/button").click()