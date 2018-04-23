#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from Page.Base_page import Basepage

class login_page(Basepage):


    login_button = 'id=>js-signin-btn' # 登陆

    email = 'name=>email'     # 账号
    password = 'name=>password'  # 密码
    login = 'x=>/html/body/div[7]/div[2]/div/div/form/div[5]/input'  # 登录

    QQ_login = 'c=>icon-qq' #qq登陆

    # 点击首页的登陆按钮
    def clikc_login_button(self):
        self.click(self.login_button)

    # 输入账号密码
    def input_email_password(self,email,password):
        self.input(self.email,email)
        self.sleep(0.5)
        self.input(self.password,password)

    # 点击登陆按钮
    def click_login(self):
        self.click(self.login)

    # 判断登陆按钮是否可见
    def login_is_dispaly(self):
        dispaly = self.element_is_dispalynd(self.email)
        if dispaly==False:
            return False
        else:
            return True


