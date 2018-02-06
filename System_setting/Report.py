#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import time
import os
import HTMLTestRunner
from System_setting.Logger import Logger
from System_setting.Root_directory import Root_xpath

logger = Logger(logger='Test_report').getlog()

#测试报告格式化

class Report():

    def get_report_path(self):
        root = Root_xpath()
        root_path = root.get_root_path()
        report_path = root_path + '/Data/Report'
        return report_path


    def Test_report(self,report_title):
        report_path = self.get_report_path()
        # 获取系统当前时间
        month = time.strftime("%m", time.localtime(time.time()))
        day = time.strftime("%d", time.localtime(time.time()))
        report_name = time.strftime("%H_%M_%S", time.localtime(time.time()))
        report_path = report_path + r'/' + month + '月' + r'/' + day+'日'
        report_statu = os.path.exists(report_path)
        # os.makedirs(report_path)
        if report_statu==False:
            os.makedirs(report_path)
        report_path = report_path + '/' +report_name + '-' +report_title+'.html'
        fp = open(report_path, "wb")
        # logger.info('：%s已生成！'%report_title)
        return fp,report_path




