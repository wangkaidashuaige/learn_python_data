from selenium import webdriver
driver = webdriver.Chrome()
# # webdriver还提供了另一种写法，统一调用 find_element（）方法，通过By来定位。常用。
#     find_element(By.id,"kw")
#     find_element(By.name,"wd")
#     find_element(By.class_name,"s_ipt")
#     find_element(BY.tag_name,"input")
#     find_element(By.link_text，"新闻")
#     find_element(BY.partial_link_text,"新")
#     find_element(By.xpath,"//*[@class='big s_btn']")
#     find_element(BY.css_selector,"span.bg s_btn_wr>input#su")
#
# # selenium常用方法:````````````````````````````````````````````````````````````````````````````````````````````````````
#     driver.set_window_size()        # 设置浏览器大小
#     driver.maximize_window()        # 设置浏览器最大
#     driver.refresh()                # 刷新web界面
#     driver.back()                   # 后退
#     driver.forward()                # 前进
#     driver.clear()                  # 清除文本
#     send_keys(values)               # 模拟输入
#     click()                         # 模拟单击袁元素
#     submit()                        # 提交
#     driver.implicitly_wait(10)      # 隐式等待10秒
#     driver.current_url              # 打印出URL
#     driver.title                    # 获取当前页面title信息
#     driver.close（）                 # 关闭当前窗口
#     driver.quit()                   # 退出并关闭所有窗口
#     driver.save_screenshot('abc.png') # 保存截图
#
# # 在webdriver中与鼠标操作的相关方法都封装在 ActionChains 类中。ActionChains类提供了鼠标常用发发如下:``````````````````````````````
#     perform()               # 执行ActionChains类型储存的所有行为
#     context_click()         # 右击
#     double_click()          # 双击
#     drag_and_drop()         # 拖动
#     move_to_element()       # 鼠标悬停
#     perform()  # 执行以上事件的方法 【重点】
#          move_to_element()   # 鼠标悬停方法讲解：
#         above = driver.find_element_by_link_text("设置")
#         ActionChains(driver).move_to_element(above).perform()
#         ActionChains(driver)            # 调用ActionChains类吧driver浏览器驱动作为参数传入
#         move_to_element(above)          # move_to_element()模拟鼠标移动到元素上，调用时指定元素above = driver.find_element_by_xpath
#         perform()                       # 提交ActionChains类中储存的行为


# keys# 常用键盘事件``````````````````````````````````````````````````````````````````````````````````````````````````````
# Keys.BACK_SPACE :删除键
# Keys.SPACE :空格键
# Keys.TAB: Tab键
# Keys.ESCAPE :回退键
# Keys.ENTER :回车键
# Keys.CONTROL,"a" :组合键,Ctrl + A
# Keys.CONTROL,"x" :组合键,Ctrl +X
# Keys.CONTROL,"v" :组合键, Ctrl + V
# Keys.CONTROL,"C" :组合键, Ctrl + C
# Keys.F1: F1键
# Keys.F12: F12键