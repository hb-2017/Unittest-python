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
browser.find_element_by_id('addWaybillTemplateBtn').click()
time.sleep(2)
browser.find_element_by_id('select2-imgType_selectVal-container').click()
browser.find_element_by_class_name('select2-search__field').send_keys('顺丰')
browser.find_element_by_class_name('select2-search__field').send_keys(Keys.ENTER)
div = browser.find_element_by_id('printTypeDiv')
label = div.find_elements_by_tag_name('label')
label_text1 = []
for item in label:
    item1 = item.text
    if item1=='顺丰热敏136mm':
        item.click()
browser.find_element_by_class_name('payTypeGroup_1').click()
