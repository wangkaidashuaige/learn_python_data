from selenium import webdriver          # 导入selenium中的webdriver
from time import sleep                  # 导入time中的sleep
from selenium.webdriver import ActionChains     # 导入ActionChains（鼠标操作方法）类
from selenium.webdriver.common.by import By     # 导入By方法
import smtplib                                  # python 中负责发邮件的方法
import unittest                                 # unittest 方法
import pytest                                   # pytest 方法
from email.mime.text import MIMEText            # 调用MIMEText类，定义发送邮件的正文、格式、编码
from email.header import Header                 # 调用email中Header类，定义邮件主题，和编码类型
