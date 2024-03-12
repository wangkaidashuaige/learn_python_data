# !/user/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://search.bilibili.com/all?vt=07908470&keyword=python")
# driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul[2]/li[1]/li/div[1]/div/span").click()
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div[4]/div[2]/form/div[1]/input").send_keys("15981605527")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div[4]/div[2]/form/div[3]/input").send_keys("wangkaishiniba1")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div[4]/div[2]/div[2]/div[2]").click()


driver.get("https://member.bilibili.com/platform/upload/video/frame?page_from=creative_home_top_upload")
driver.find_element(By.XPATH,"/html/body/div/div[3]/div[1]/div/div/div[1]/div[2]/div/div/div/div/a").click()
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input").send_keys("15981605527")
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/input").send_keys("wangkaishiniba1")
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]").click()
