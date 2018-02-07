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

values = Exceldata().get_data('login')
logger = Logger(logger='test1').getlog()

@ddt.ddt
class Test_login(Load_drive):


    @Decorator.Running_time()
    def get_userinfo1(self):
        config_value = ['username','password']
        config = Config()
        data = config.config_data(config_name='common_data.ini',config_title=['code_01'],config_value=config_value)
        return data


    @ddt.data(*values)
    @ddt.unpack
    def test_login(self,username,password,statu,msg):
        login_pa = login_page(self.browser)
        if statu==0:
            page_title=self.__login_success(msg)
            self.assertEqual(page_title, msg)
        else:
            error_tip = self.__login_fail(msg)
            if login_pa.captchaImg_is_exist() ==False:
                self.assertEqual(error_tip, '请输入图片验证码')
            # 没有验证码
            else:
                self.assertEqual(error_tip,msg)


    # 成功登录用例
    def __login_success(self,msg):
        login_pa = login_page(self.browser)
        login_pa.click_submit(values)
        page_title = login_pa.get_page_title()
        return page_title


    #失败登录用例
    def __login_fail(self,msg):
        login_pa = login_page(self.browser)
        login_pa.click_submit(values)
        error_tip = login_pa.login_error_tip()
        return error_tip
        # # 出现验证码就判断验证码的提示是不是正确的
        # if login_pa.captchaImg_is_exist() ==False:
        #     if error_tip=='请输入图片验证码':
        #         return True
        #     else:
        #         return False
        # # 没有验证码
        # else:
        #     if error_tip == msg:
        #         return True
        #     else:
        #         return False




