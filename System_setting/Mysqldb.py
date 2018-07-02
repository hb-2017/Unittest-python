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


class Mysql():

    def __init__(self):
        cnf = Config()
        self.db_data = cnf.config_data('DB',['Alitest'],['ip','user','password','port','db'])
        print(self.db_data)


    def Connect_db(self):
        # 打开数据库连接
        try:
            self.db = pymysql.connect(host=self.db_data[0],user=self.db_data[1],passwd=self.db_data[2],db=self.db_data[4])
            # 使用cursor()方法获取操作游标
            self.cursor = self.db.cursor()
            logger.info('数据库【%s】连接成功'%self.db_data[4])
            return True
        except Exception as e:
            logger.info('数据库【%s】连接失败：%s' % (self.db_data[3],e))
            return False


    def implement_sql(self,sql):
        logger.info('即将执行sql【%s】'%sql)
        try:
            sql_satatu = self.cursor.execute(sql)
            # sql_statu2 = self.cursor.fetchall()
            self.db.commit()
            return sql_satatu
        except Exception as e:
            logger.error('执行sql【%s】，发生异常：%s,开始回滚' % (sql, e))
            self.db.rollback()
            return False


    # 增
    def add(self,table_name,value_str,field_str=None):
        '''
        :param table_name: 数据库表名
        :param field_str: 增加的字段
        :param value_str: 增加字段对应值
        :return:
        '''
        db_state = self.Connect_db()
        if db_state==True:
            if field_str!=None:
                sql = 'INSERT INTO %s (%s) VALUES (%s)'%(table_name,field_str,value_str)
            else:
                sql = 'INSERT INTO %s  VALUES (%s)' % (table_name, value_str)
            # 返回sql执行状态
            sql_satatu = self.implement_sql(sql)
            return sql_satatu
        else:
            logger.info('数据库未连接，无法执行sql')


    # 删
    def delete(self,table_name,condition):
        '''
        :param table_name: 数据库表名
        :param condition: 删除条件
        :return:
        '''
        if condition==None or len(condition)<1:
            logger.info('删除数据条件为必填，需要删除全表请用delete_all')
        else:
            db_state = self.Connect_db()
            if db_state == True:
                sql = 'delete from %s where %s'%(table_name,condition)
                # 返回sql执行状态
                sql_satatu = self.implement_sql(sql)
                return sql_satatu
            else:
                logger.info('数据库未连接，无法执行sql')


    # 删除全部
    def delete_all(self,table_name):
        '''
        :param table_name: 数据库表名
        :return:
        '''
        db_state = self.Connect_db()
        if db_state == True:
            sql = 'delete from %s '%(table_name)
            # 返回sql执行状态
            sql_satatu = self.implement_sql(sql)
            return sql_satatu
        else:
            logger.info('数据库未连接，无法执行sql')


    # 改
    def updata(self,table_name,set_str,condition):
        '''
        :param table_name: 数据库表名
        :param set_str: 修改的字段名和值
        :param condition: 修改条件
        :return:
        '''
        if set_str!=None and len(condition)>1: #判断set数据是否成立
            if condition == None or len(condition) < 1:  #判断是否有where条件
                logger.info('修改数据条件为必填，需要删除全表请用updata_all')
            else:
                db_state = self.Connect_db()
                if db_state == True:
                    sql = 'updata from %s set %s where %s' % (table_name, set_str, condition)
                    # 返回sql执行状态
                    sql_satatu = self.implement_sql(sql)
                    return sql_satatu
                else:
                    logger.info('数据库未连接，无法执行sql')
        else:
            logger.info('修改数据条件为必填，且长度大于1')


    # 改
    def updata_all(self, table_name, set_str):
        '''
        :param table_name: 数据库表名
        :param set_str: 修改的字段名和值
        :return:
        '''
        if set_str != None and len(set_str) > 1:  # 判断set数据是否成立
            db_state = self.Connect_db()
            if db_state == True:
                sql = 'updata from %s set %s ' % (table_name, set_str)
                # 返回sql执行状态
                sql_satatu = self.implement_sql(sql)
                return sql_satatu
            else:
                logger.info('数据库未连接，无法执行sql')
        else:
            logger.info('修改数据条件为必填，且长度大于1')


    # 查
    def selete(self,table_name,check_field='*',condition=None):
        '''
        :param table_name: 数据库表名
        :param check_field: 查找的字段
        :param condition: 查找条件
        :return: 查找的结果
        '''
        if table_name!=None and len(table_name)>1:
            db_state = self.Connect_db()
            if db_state == True:
                if condition==None:
                    sql = 'select %s from %s'%(check_field,table_name)
                else:
                    sql = 'select %s from %s where %s' % (check_field, table_name,condition)
                sql_satatu = self.implement_sql(sql)
                select_satatu = self.cursor.fetchall()
                return select_satatu
            else:
                logger.info('数据库未连接，无法执行sql')


    # 开放性接口，sql自己定义
    def open_sql(self,sql):
        '''
        :param sql:自定义的sql
        :return:sql执行状态或查询结果
        '''
        db_state = self.Connect_db()
        if db_state == True:
            sql_satatu = self.implement_sql(sql)
        else:
            logger.info('数据库未连接，无法执行sql')


