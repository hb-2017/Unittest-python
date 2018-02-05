#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)
from System_setting.Logger import Logger

logger = Logger(logger='common_class').getlog()

class common_class():

    '''
    参数：
    obj 需要转换类型的对象
    type_ 需要转换的类型
    返回：
    obj 转换后的对象
    '''
    def change_type(self,obj,type_):
        _type = type(obj)
        if _type ==type_:
            return obj
        else:
            try:
                obj = type_(obj)
                return obj
            except BaseException as e:
                logger.error('object类型转换出错：%s'%e)
                return obj
