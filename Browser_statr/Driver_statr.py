#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-31 19:11:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import unittest
from System_setting.Driver import Driver
from System_setting.Logger import Logger
import time

logger = Logger(logger='quit_browser').getlog()

#驱动加载
class Load_drive(unittest.TestCase):

    Driver_ = Driver()
    browser = Driver_.open_browser()

    def setUp(self):
        # 测试固件的setUp()的代码，主要是测试的前提准备工作
        pass

    def tearDown(self):
        # 测试固件的tearDown()的代码，这里基本上都是关闭浏览器
        # self.browser.quit()
        pass

class Out_drive(Load_drive):

    def test_quit_browser(self):
        time.sleep(1)
        self.browser.quit()
        logger.info('浏览器退出 !')



