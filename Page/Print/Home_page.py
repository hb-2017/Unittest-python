#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)


from Page.Page_base import Basepage

class home_page(Basepage):
    Express = 'id=>expressSet_os_btn' # 快递单设置

    # 点击快递单设置
    def click_Express(self):
        self.click(self.Express)
        self.sleep(1)
