#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from Page.Base_page import Basepage

class login_page(Basepage):


    login_button = 'id=>js-signin-btn'

    email = 'name=>email'
    password = 'name=>password'

    login = 'x=>//*[@id="signup-form"]/div[5]/input'




