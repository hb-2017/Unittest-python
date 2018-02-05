#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02 11:20:44
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import pymysql
import traceback
from System_setting.Config import Config
from System_setting.Logger import Logger

logger = Logger(logger='Mysql').getlog()

class Mysql(object):

    def __init__(self):
        data = self.get_mysql_info()
        data = data[0]
        print(data)
        Mysql_ip = data[0]   # 数据库ip
        Mysql_name = data[1] #用户名
        Mysql_password = data[2]  #密码
        db_name = data[3]  #数据库名
        db_port = data[4]  #端口号
        db_encode = data[5]  #编码
        try:
            # 打开数据库连接
            self.db = pymysql.connect(Mysql_ip,Mysql_name,Mysql_password,db_name)
            # 使用cursor()方法获取操作游标
            self.cursor = self.db.cursor()
            logger.info('连接数据库:%s成功...' %db_name )
        except Exception as e:
            logger.error('数据库链接异常,%s' % e)


    def get_mysql_info(self):
        config_value = ['Mysql_ip','Mysql_name','Mysql_password','db_name','db_port','db_encode']
        config = Config()
        data = config.config_data('db_info',['my_sql'],config_value)
        return data


    def add(self,sql):
        try:
            # 执行sql并返回执行状态
            sql_satatu = self.cursor.execute(sql)
            self.db.commit()
            logger.info('正在执行add sql：%s'%sql)
            sql_data = self.cursor.fetchall()
            return sql_satatu,sql_data
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
            logger.info('正在执行delete sql：%s' % sql)
            return sql_satatu
        except BaseException as e:
            logger.error('执行sql:%s 发生异常%s,开始回滚' % (sql, e))
            # 异常则回滚
            self.db.rollback()


    def updata(self, sql):
        try:
            # 执行sql并返回执行状态
            sql_satatu = self.cursor.execute(sql)
            self.db.commit()
            logger.info('正在执行updata sql：%s' % sql)
            return sql_satatu
        except BaseException as e:
            logger.error('执行sql:%s 发生异常%s,开始回滚' % (sql, e))
            # 异常则回滚
            self.db.rollback()


    def selete(self, sql):
        try:
            # 执行sql并返回执行状态
            sql_satatu = self.cursor.execute(sql)
            self.db.commit()
            logger.info('正在执行selete sql：%s' % sql)
            return sql_satatu
        except BaseException as e:
            logger.error('执行sql:%s 发生异常%s,开始回滚' % (sql, e))
            # 异常则回滚
            self.db.rollback()

