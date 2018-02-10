#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import time
import inspect
from System_setting.Logger import Logger

logger = Logger(logger='Decorator').getlog()



class Decorator():

    #运行时间
    def Running_time(text=None):
        def _Running_time(func):
            def wrapper(*args,**kwargs):  #匹配任何参数
                logger.info('方法【%s】开始...'%func.__name__)
                statr_time = time.time()
                data = func(*args, **kwargs)
                end_time = time.time()
                runtime = (end_time-statr_time)
                logger.info('方法【%s】结束，共消耗时长为%.2f秒'%(func.__name__,runtime))
                return data
            return wrapper
        return _Running_time

