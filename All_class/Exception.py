#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import inspect
from System_setting.Screenshot import Screen


class Custom_exception(Exception):

    def __init__(self):
        self.screen = Screen()

    # 测试不通过的方法
    def test_fail(self,error_msg=None,test_item=None):
        test_name = inspect.stack()[1][3]
        self.screen.get_windows_img(test_name)
        if error_msg==None:
            error_msg='测试结果与预期结果不一致'
        raise AssertionError('测试用例未通过,%s。用例名称:%s,用例数据:%s'%(error_msg,test_name,test_item))






