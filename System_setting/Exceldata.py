#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import os
import time
import math
from System_setting.Logger import Logger
from System_setting.Root_directory import Root_xpath
import xlrd
from All_class.Decorator import Decorator

logger = Logger(logger='exceldata').getlog()
class Exceldata():

    def __init__(self):
        xpath = Root_xpath()
        self.excel_path = xpath.get_root_path()+'/Data/Excel/'

    @Decorator.Running_time()
    def get_data(self,excel_name,excel_sheet=None):
        excel_path = self.excel_path+excel_name+'.xls'
        try:
            excel = xlrd.open_workbook(excel_path)
            logger.info('正在打开excel文件%s'%excel_name)
        except BaseException as e:
            logger.error('打开excel文件【%s】出错%s'%(excel_name,e))
            return False
        if excel_sheet==None:
            logger.info('没有填写sheet名字，默认读取第一页')
            table = excel.sheets()[0]  # 通过索引顺序获取
            # table = excel.sheet_by_index(0)  # 通过索引顺序获取
        else:
            logger.info('正在打开%s页签'%excel_sheet)
            table = excel.sheet_by_name(excel_sheet)  # 通过名称获取
        # 获取行数和列数
        nrows = table.nrows
        ncols = table.ncols
        logger.info('当前页签数据行数：%s,列数为：%s'%(nrows,ncols))
        # 循环行列表数据
        values = []
        for i in range(nrows-1): # 去掉第一行的标题
            va = table.row_values(i+1)
            values.append(va)
        values = self.change_datatype(values)
        logger.info('获取到excel表数据：%s'%values)
        # print(values)
        return values


    # 对excel的数据进行处理，小数全部转换为整数
    def change_datatype(self,values):
        _values = []
        for item in values:
            value = []
            for it in item:
                if type(it) ==float:
                    try:
                        # print('%s的类型为%s'%(it,type(it)))
                        it = int(math.floor(it))
                    except BaseException as e:
                        logger.error('excel数据格式转换出错:%s'%e)
                    value.append(it)
                else:
                    value.append(it)
            _values.append(value)
        return _values


