#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-31 18:23:36
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

#项目路劲
class Root_xpath():
    '''
    返回值
    root_path 系统根目录路劲
    '''
    def get_root_path(self):
        root_path = os.path.dirname(os.path.abspath('.'))
        return root_path



