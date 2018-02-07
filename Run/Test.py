#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest
import HTMLTestRunner
# import Test_case
from Test_case import Tese1
from System_setting.Report import Report
from Browser_statr.Driver_statr import Load_drive
from System_setting.SMTP import Smtp

cases=unittest.TestLoader().loadTestsFromTestCase(Tese1.Test_login)
suite = unittest.TestSuite([cases])
# suite.addTest(Tese1.Test_login("test_login"))  #登录测试用例
# suite.addTest(Load_drive("test_quit_browser"))  #退出浏览器

if __name__=='__main__':
    # 实例化测试报告
    re = Report()
    report_title = 'Test_login'
    fp,report_path = re.Test_report(report_title)
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"登录测试", description=u"用例测试情况",verbosity=2,tester='huxiansheng')
    # 开始执行测试套件
    runner.run(suite)
    fp.close()
    # 发送邮件
    smtp = Smtp(report_path)
    smtp.smtp163()


