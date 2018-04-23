#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.imooc.com/')
browser.find_element_by_id('js-signin-btn').click()
time.sleep(2)
browser.find_element_by_class_name('icon-qq').click()
browser.switch_to_window()


