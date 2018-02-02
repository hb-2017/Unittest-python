#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from Page.Login import login_page
import configparser
from System_setting.Logger import Logger
from System_setting.Config import Config
from Browser_statr.Driver_statr import Load_drive

logger = Logger(logger='test1').getlog()

class Test_login(Load_drive):

    def get_userinfo(self):
        config_value = ['username','password']
        config = Config()
        data = config.config_data(config_name='common_data.ini',config_title=['code_01'],config_value=config_value)
        return data


    def test_login(self):
        data = self.get_userinfo()
        login_pg = login_page(self.browser)
        login_pg.click_submit(data)







