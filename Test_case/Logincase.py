#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from Page.Login import login_page
import configparser
import ddt
from System_setting.Logger import Logger
from System_setting.Config import Config
from System_setting.Exceldata import Exceldata
from Browser_statr.Driver_statr import Load_drive
from All_class.Decorator import Decorator
from All_class.Exception import Custom_exception
from System_setting.Screenshot import Screen

values = Exceldata().get_data('login')
excep = Custom_exception()
logger = Logger(logger='test1').getlog()
_Screen = Screen()

@ddt.ddt
class Test_login(Load_drive):


    @Decorator.Running_time()
    def get_userinfo(self):
        values = Exceldata().get_data('login')
        return values

#     def _test_login(self,values):
#
#         for value in values:
#             username =value[0]
#             password = value[1]
#             login_statu = value[2]
#             msg= value[3]
#             login_pa = login_page(self.browser)
#             if login_statu == 0:
#                 page_title = self.__login_success(username,password)
#                 if page_title==msg:
#                     logger.info('登录测试之:%s测试通过'%value[0])
#                 else:
#                     logger.info('登录测试之:%s测试失败' % value[0])
#                     excep.test_fail(value)  #自定义异常
#             else:
#                 error_tip = self.__login_fail(username,password)
#                 # 有验证码
#                 if login_pa.captchaImg_is_exist() == False:
#                     if error_tip == '请输入图片验证码':
#                         logger.info('登录测试之:%s测试通过' % value[0])
#                     else:
#                         logger.info('登录测试之:%s测试失败' % value[0])
#                         excep.test_fail(value)  # 自定义断言
#                 # 没有验证码
#                 else:
#                     if error_tip == msg:
#                         logger.info('登录测试之:%s测试通过' % value[0])
#                     else:
#                         logger.info('登录测试之:%s测试失败' % value[0])
#                         excep.test_fail(value)  # 自定义断言
#
#
#     # def test02(self):
#     #     print('这是一个测试text')
#


    @ddt.data(*values)
    @ddt.unpack
    def test_login(self,username,password,suc,msg):

        logger.info('登录数据为【%s,%s,%s,%s】'%(username,password,suc,msg))
        login_pa = login_page(self.browser)
        login_pa.click_submit(username,password)
        #正确用例
        if suc==0:
            is_login = login_pa.get_page_title()
        #错误用例
        else:
            is_login = login_pa.login_error_tip()
        if is_login==msg:
            logger.info('登录测试之:%s测试通过' % username)
        elif is_login=='请输入图片验证码':
            logger.info('登录测试之:%s测试通过' % username)
        else:
            logger.error('登录测试之:%s测试失败' % username)
            raise excep.test_fail(username)





