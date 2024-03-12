from PO_.Base import base


class LoginPage(base):
    # 用户名
    def username(self):
        return self.by_id('fabrie-account-str-pwd-login')
    # 密码
    def password(self):
        return self.by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div[2]/form/div[2]/div/div/input")
    def yes(self):
        return self.by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div[2]/form/div[3]/div/button")
    # 登录
    def login(self,user,pwd):
        self.username().send_keys(user)
        self.password().send_keys(pwd)
        self.yes().click()




