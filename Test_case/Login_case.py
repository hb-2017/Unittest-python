#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from Browser_statr import Driver_statr
from Page.Login_page import login_page
import configparser
from System_setting.Config import Config
from System_setting.Logger import Logger
from System_setting.Screenshot import Screen
from Browser_statr.Driver_statr import Load_drive


logger = Logger(logger="login_page").getlog()

class login_case(Load_drive):

    def setUp(self):
        self.login_pg = login_page(self.browser)

    def test_login(self):
        data = Config().config_data('common_data',['muke'],['username','password'])
        username = data[0]
        password = data[1]
        self.login_pg.clikc_login_button()
        self.login_pg.input_email_password(username,password)
        self.login_pg.click_login()
        self.login_pg.sleep(2)
        dispaly = self.login_pg.login_is_dispaly()
        if dispaly==True:
            raise ('登陆失败，当前处于登陆界面')


    def test_QQ_login(self):
        self.login_pg.clikc_login_button()

