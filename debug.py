#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

browser = webdriver.Chrome(r'D:\Unittest\Tools\chromedriver.exe')
browser.maximize_window()
browser.get('https://www.imooc.com/')
browser.find_element_by_id('js-signin-btn').click()
browser.find_element_by_name('email')
browser.find_element_by_name('password').send_keys('222')
browser.find_element_by_class_name('rlf-group clearfix').find_element_by_tag_name('input').click()
