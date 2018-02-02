#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02 11:20:44
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import MySQLdb
import traceback
from System_setting.Logger import Logger

logger = Logger(logger='Mysql').getlog()

class Mysql(object):

    def __init__(self, Mysql_ip, Mysql_name, Mysql_password, db_name):
        try:
            # 打开数据库连接
            self.db = MySQLdb.connect(Mysql_ip, Mysql_name, Mysql_password, db_name)
            # 使用cursor()方法获取操作游标
            self.cursor = self.db.cursor()
            logger.info('数据库%s连接成功...' % db_name)
        except Exception as e:
            logger.error('数据库链接异常,%s' % e)

    def add(self,sql):
        try:
            # 执行sql并返回执行状态
            sql_satatu = self.cursor.execute(sql)
            self.db.commit()
            return sql_satatu
        except BaseException as e :
            logger.error('执行sql:%s 发生异常%s,开始回滚'%(sql,e))
            # 方法二：采用traceback模块查看异常
            # traceback.print_exc()
            # 方法三：采用sys模块回溯最后的异常
            # 输出异常信息
            # info = sys.exc_info()
            # print(info[0], ":", info[1])

            # 异常则回滚
            self.db.rollback()

    def delete(self, sql):
        try:
            # 执行sql并返回执行状态
            sql_satatu = self.cursor.execute(sql)
            self.db.commit()
            return sql_satatu
        except BaseException as e:
            logger.error('执行sql:%s 发生异常%s,开始回滚' % (sql, e))
            # 方法二：采用traceback模块查看异常
            # traceback.print_exc()
            # 方法三：采用sys模块回溯最后的异常
            # 输出异常信息
            # info = sys.exc_info()
            # print(info[0], ":", info[1])

            # 异常则回滚
            self.db.rollback()



