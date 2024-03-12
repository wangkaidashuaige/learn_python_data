from selenium.webdriver.common.by import By


class base:
    def __init__(self,driver):
        self.driver = driver
    # 通过ID的方法定位
    def by_id(self,ele):
        return self.driver.find_element(By.ID,ele)

    # 通过name的方法定位
    def by_name(self,ele):
        return self.driver.find_element(By.NAME,ele)

    # 通过class的方法定位
    def by_css(self,ele):
        return self.driver.find_element(By.CSS_SELECTOR,ele)

    # 通过xpath的方法定位
    def by_xpath(self,ele):
        return self.driver.find_element(By.XPATH,ele)

    # 通过class_name的方法定位
    def by_class_name(self,ele):
        return self.driver.find_element(By.CLASS_NAME,ele)

    # 通过link_text的方法定位
    def by_link_text(self,ele):
        return self.driver.find_element(By.LINK_TEXT,ele)


    # def by_id(self,ele):
    #     return self.driver.find_element(By.ID,ele)
    #
    # def by_id(self,ele):
    #     return self.driver.find_element(By.ID,ele)


    