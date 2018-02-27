#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import ddt
from Browser_statr.Driver_statr import Load_drive
from System_setting.Logger import Logger
from System_setting.Exceldata import Exceldata
from System_setting.Screenshot import Screen
from Page.Print.Expressinstall import expressinstall
from Page.Print.Home_page import home_page

logger = Logger('add_template').getlog()


class add_template(Load_drive):

    def setUp(self):
        self.express = expressinstall(self.browser)
        self.home_pg = home_page(self.browser)


    def get_template_data(self):
        excel = Exceldata()
        data = excel.get_data('template')
        return data

    # 添加顺丰模板
    def add_SF_template(self,data):
        # 数据处理
        Template_name = data['Template']
        Freight_Payment = data['Freight_Payment']
        Business_type = data['Business_type']
        # 选择面单类型
        Choice_template_statu = self.Choice_template(Template_name)
        if Choice_template_statu:
            # 选择付款方式
            self.express.click_Payment_mode(Freight_Payment)
            # 选择业务类型
            click_expressType_statu = self.express.click_Business_type(Business_type)
            if click_expressType_statu==None:
                logger.info('%s业务类型不存在，默认为顺丰标快'%Business_type)
            # 添加模板
            self.express.click_savetemplate()
            # 判断是否添加成功
            save_statu = self.save_statu()
            if save_statu==True:
                add_SF_template_statu=True
            else:
                add_SF_template_statu = False
        else:
            # 取消添加
            self.express.click_canceltemplate()
            add_SF_template_statu = False
        return add_SF_template_statu



    def add_ZL_template(self,data):
        pass

    def add_CN_template(self,data):
        pass

    def add_TD_template(self,data):
        pass

    # 选择模板类型
    def Choice_template(self,Template_name):
        div = self.express.select_template_div()
        label = div.find_elements_by_tag_name('label')
        for item in label:
            item1 = item.text
            if Template_name==item1:
                try:
                    item.click()
                    Choice_template_statu = True
                except BaseException as e:
                    Choice_template_statu = False
                    logger.error('选择模板出错%s'%e)
                break
        else:
            Choice_template_statu = None
            logger.info('当前模板&s,不在模板列表中'%Template_name)
        return Choice_template_statu

    # 判断保存状态
    def save_statu(self):
        save_tip = self.express.get_save_tip()
        if save_tip == '设置保存成功':
            self.express.click_tip_button()
            save_statu = True
        else:
            logger.info('添加模板失败，%s' % save_tip)
            self.express.click_tip_button()
            save_statu = False
        return save_statu


    # 添加模板
    def add_template_main(self):
        # 获取模板数据
        template_data = self.get_template_data()
        # 加载页面方法
        self.home_pg.click_Express()
        for data in template_data:
            Logistics_company = data['Logistics_company']  #物流公司
            Temlpalte_name = data['Template']  #模板
            self.express.click_add()
            self.express.click_select()
            self.express.input_logistics_company(Logistics_company)

            # 当前模板在模板列表中才进行下一步操作，否则跳过
            # if Temlpalte_name in label_text:
            if '顺丰' in Temlpalte_name:
                self.add_SF_template(data)
            elif '直连' in Temlpalte_name:
                self.add_ZL_template(data)
            elif '菜鸟' in Temlpalte_name:
                self.add_CN_template(data)
            elif '套打' in Temlpalte_name:
                self.add_TD_template(data)
            else:
                logger.info('当前模板%s,未在模板列表中已跳过该模板...'%Temlpalte_name)

