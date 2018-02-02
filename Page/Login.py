#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from Page.Page_base import Basepage

class login_page(Basepage):

    username = 'id=>userName'
    password = 'id=>passWord'
    submit = 'id=>submit'


    def input_userinfo(self,userinfo):
        self.input(self.username,userinfo[0])
        self.input(self.password,userinfo[1])


    def click_submit(self,userinfo=None):
        if userinfo==None:
            self.click(self.submit)
        else:
            self.input_userinfo(userinfo)
            self.click(self.submit)
            self.browser_wait(5)





