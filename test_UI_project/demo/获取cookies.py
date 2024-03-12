

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''百度网盘--------获取cookies'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome
driver.get('https://pan.baidu.com/')
driver.find_element(By.XPATH,'/html/body/section/main/div/section/main/div/div[1]/div[3]/button').click()
# sleep(15)
# cookies = driver.get_cookies() # 1、输入用户名密码获取用户的cookie
# print(cookies)                                              # 获取登录的cookie
coo = [{'domain': '.baidu.com', 'expiry': 1668143777, 'httpOnly': True, 'name': 'ab_sr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1.0.1_NDI0ZDA0YjM1YmNhYTY1OTNmMDFlYjY5ZDY4ZTkzZjdiZDg1MjBjNWNiYzZlMjRlNDkyYmRjZWQ1MTQ0NTdkNDM2NjcyMzAyZGM4MGIyOWNkYTU2ZWUwZDdkYTRhMzg4ZjJkYzczZjRkYTY4ZDczMzYxZmJmYjUyMjc4NGE4OGJkZTY4ZDQzNGY5NjU5MGEyYjE0ZjRkMTI2YjAyOTY3NjM1ZjZiM2IwNTM0MzQ1NzhmODg4N2VjNjE5N2UwODNm'}, {'domain': '.pan.baidu.com', 'expiry': 1670814975, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': '5144bba7f95752c6fecd859be4bb9dbac7529d8c3c9e57d29e90226ed6b3ab5d'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'secure': False, 'value': 'ePPzKbqCjAMuuELKDTDpBoL3'}, {'domain': '.baidu.com', 'expiry': 1702696574, 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'm1lUXpKS2pBWW5XNEhVSzFOVVFWUXJKRmR-cTk0cHdNcHZJNll0VGYyWn5TNVZqSVFBQUFBJCQAAAAAAAAAAAEAAACGxNV~vtDB9MW2zazA1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH--bWN~vm1jM'}, {'domain': '.pan.baidu.com', 'expiry': 1668222976, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '15320108014895355933%3ADJI9ZdfpjgJOnal3y0LEeHlibiKzYuqjp9mBzznPNztk2gXrFpwRszgAJXHPhuRJ5eSXRigWTxwr2wqYbSNJzJt0bv4HmRzAkr%2Fj3K39d%2BxE2OlLZIpvWm0rX84ZNRi4usjlivDBSeRyx4n1zr2IJ5C9qgHiau%2FldS8c7ndIzLExGZiuUUeCaoX0p6z9lD8V7g%2B5PM2vWus%3D'}, {'domain': '.baidu.com', 'expiry': 1702696574, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'm1lUXpKS2pBWW5XNEhVSzFOVVFWUXJKRmR-cTk0cHdNcHZJNll0VGYyWn5TNVZqSVFBQUFBJCQAAAAAAAAAAAEAAACGxNV~vtDB9MW2zazA1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH--bWN~vm1jM'}, {'domain': '.baidu.com', 'expiry': 1699672561, 'httpOnly': False, 'name': 'BAIDUID_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '49FBB426D2B959046DCD42C032AB11FB:FG=1'}, {'domain': 'pan.baidu.com', 'expiry': 1670728577, 'httpOnly': False, 'name': 'ndut_fmt', 'path': '/', 'secure': False, 'value': 'EB0D3E044B05C73B12FC1D9ECDF4C6CCCADD7CEAF5F6709474E99594EBAD917B'}, {'domain': '.baidu.com', 'expiry': 1670728561, 'httpOnly': True, 'name': 'newlogin', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.baidu.com', 'expiry': 1699672561, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '49FBB426D2B959046DCD42C032AB11FB:FG=1'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'XFCS', 'path': '/disk', 'secure': False, 'value': '7DD8A8E318E851BE561B931983326DAAE6908387BEFDC3406EB5ECE1F0081922'}, {'domain': 'pan.baidu.com', 'httpOnly': False, 'name': 'XFI', 'path': '/disk', 'secure': False, 'value': '496e0e6c-dfa1-0d2c-fd43-1ad7f0cf8fa4'}]
for cookie in coo:      # 使用for循环得到cookie
    driver.add_cookie(cookie)
sleep(1)
driver.get('https://pan.baidu.com/')    # 获取到cookie再次打开地址，成功使用cookie登录