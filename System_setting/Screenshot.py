#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-31 18:10:12
# @Author  : huxiansheng (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import time
import os
from System_setting.Logger import Logger
from System_setting.Root_directory import Root_xpath
from Browser_statr.Driver_statr import Load_drive


#实例化日志类
logger = Logger(logger = 'Screenhorts').getlog()

class Screen(Load_drive):

	def get_report_path(self):
		root = Root_xpath()
		root_path = root.get_root_path()
		Screen_path = root_path + '/test_screen'
		return Screen_path


	def get_windows_img(self,screen_title):
		Screen_path = self.get_report_path()
		# 获取系统当前时间
		month = time.strftime("%m", time.localtime(time.time()))
		day = time.strftime("%d", time.localtime(time.time()))
		Screen_name = time.strftime("%H_%M_%S", time.localtime(time.time()))
		Screen_path = Screen_path + r'/' + month + '月' + r'/' + day + '日'
		Screen_statu = os.path.exists(Screen_path)
		if Screen_statu == False:
			os.makedirs(Screen_statu)
		screenname = Screen_path + '/' + Screen_name + '-' + screen_title + '.png'
		try:
			self.browser.get_screenshot_as_file(screenname)
			logger.info('产生截图,截图时间:%s,名称为%s ' % (time.time(), screen_title))
		except NameError as e:
			logger.error('系统截图发生未知异常, %s' % e)
			self.get_windows_img(screen_title)