#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest
import HTMLTestRunner
import re
from Test_case.Login_case import login_case
from System_setting.Report import Report
from Browser_statr.Driver_statr import Load_drive,Out_drive
from System_setting.SMTP import Smtp



suite = unittest.TestSuite()
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_login))  #登录测试用例
suite.addTest(login_case('test_login'))  #登录测试用例
# suite.addTest(Out_drive("test_quit_browser"))  #退出浏览器


if __name__=='__main__':
    report_title = 'Test_login'
    # 实例化测试报告
    re = Report()
    report_title = 'Test_login'
    fp, report_path = re.Test_report(report_title)
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=r'登录测试', description=u"用例测试情况",verbosity=2)
    # 开始执行测试套件
    runner.run(suite)
    fp.close()
    # 发送邮件
    # smtp = Smtp(report_path)
    # smtp.smtp163()


