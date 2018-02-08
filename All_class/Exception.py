#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import inspect

class Custom_exception():

    def test_fail(self,error_msg=None,test_item=None):
        if error_msg==None:
            error_msg='测试结果与预期结果不一致'
        test_name =inspect.stack()[1][3]
        raise AssertionError('测试用例未通过,%s。用例名称:%s,用例数据:%s'%(error_msg,test_name,test_item))






