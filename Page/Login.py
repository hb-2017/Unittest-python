#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from Page.Page_base import Basepage

class login_page(Basepage):

    username = 'id=>userName'
    password = 'id=>passWord'
    submit = 'id=>submit'

    error_tip = 'class=>error'  #错误提示
    captchaImg = 'id=>captchaImg'

    def input_userinfo(self,username,password):
        self.input(self.username,username)
        self.input(self.password,password)


    def click_submit(self,username,password):
        if username==None:
            self.click(self.submit)
        else:
            self.input_userinfo(username,password)
            self.click(self.submit)
            self.browser_wait(5)

    def login_error_tip(self):
        text = self.get_elemeent_text(self.error_tip)
        return text


    def captchaImg_is_exist(self):
        is_exist = self.element_is_dispalynd(self.captchaImg)
        return is_exist


