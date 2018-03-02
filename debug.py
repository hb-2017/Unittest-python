#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(r'D:\Unittest-python\Tools\chromedriver.exe')
browser.maximize_window()
browser.get('http://www.1dadan.com/')
browser.find_element_by_id('userName').send_keys('test09')
browser.find_element_by_id('passWord').send_keys('1qaz2wsx')
browser.find_element_by_id('submit').click()
time.sleep(2)
browser.find_element_by_id('expressSet_os_btn').click()
time.sleep(2)
browser.find_element_by_id('printGlobalSettings').click()
time.sleep(2)
lis = browser.find_elements_by_class_name('dd-item')
for li in lis:
    try:
        li.find_element_by_tag_name('i').click()
    except:
        pass
    browser.find_element_by_class_name('confirm').click()


