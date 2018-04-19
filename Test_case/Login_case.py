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

class loing_case(Load_drive):

    def login(self):
        data = Config().config_data('common_data',['zhihu'],['username','password'])
        username = data[0]
        password = data[1]
        login_pg = login_page(self.browser)
        login_pg.click_change_login_button()
        button_text = login_pg.get_change_login_button_text()
        if '登录' in button_text:
            logger.info('切换到登陆界面失败...')
        else:
            login_pg.input_user_name(username,password)
            login_pg.click_login()
            page_title = login_pg.get_page_title()
            if '首页' in page_title:
                logger.info('登陆成功...')
            else:
                logger.info('登陆失败...')



