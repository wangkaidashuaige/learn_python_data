

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''# 携程------ ---滑块验证码 '''
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://passport.ctrip.com/user/reg/home')
driver.find_element(By.XPATH,'//*[@id="agr_pop"]/div[3]/a[2]').click()
a_ele=driver.find_element(By.XPATH,'//*[@class="cpt-drop-btn"]')# 把移动的点 赋予一个变量a_ele
print(a_ele.size['width'])  # 打印出 X轴宽度
print(a_ele.size['height']) # 打印出 Y轴高度
b_ele=driver.find_element(By.XPATH,'//*[@id="slideCode"]/div[1]/div[4]') # 移动范围框框，赋予一个b_ele变量
action=ActionChains(driver) #初始化一个鼠标对象
sleep(2)
action.drag_and_drop_by_offset(a_ele,b_ele.size['width'],-b_ele.size['height']).perform() # 按住鼠标拖拽到指定位置