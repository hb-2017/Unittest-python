#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)


from System_setting.Logger import Logger
from System_setting.Config import Config
from Browser_statr.Driver_statr import Load_drive

logger = Logger(logger='test_cc').getlog()

class test_cc(Load_drive):

    def test01(self):

        logger.info('test01执行')

    def test02(self):
        for i in range(10):
            logger.info('当前test02 -- %s'%i)
            if i ==5:
                raise Exception('test02异常')


    def test03(self):
        logger.info('test03执行')

    def test04(self):
        logger.info('test04执行')

