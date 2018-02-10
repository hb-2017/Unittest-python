#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

# from selenium import webdriver
# import inspect
# from Browser_statr.Driver_statr import Load_drive
# from System_setting.Screenshot import Screen


# class pp(Load_drive):
#
#     def test01(self):
#         s = Screen()
#         s.get_windows_img('login')

import os
import time
Screen_path = 'D:\\Unittest-python/Data/Screenshots'
month = time.strftime("%m", time.localtime(time.time()))
day = time.strftime("%d", time.localtime(time.time()))
Screen_name = time.strftime("%H_%M_%S", time.localtime(time.time()))
Screen_path = Screen_path + r'/' + month + '月' + r'/' + day + '日'
Screen_statu = os.path.exists(Screen_path)
if Screen_statu == False:
    os.makedirs(Screen_path)


