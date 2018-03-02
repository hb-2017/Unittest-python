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

    # 模板数据处理
    def get_template_data(self):
        excel = Exceldata()
        data = excel.get_data('template')
        return data

    # 直连商家信息处理
    def ZL_info_list(self,data):
        code_list = []
        ZL_code_01 = data['ZL_code_01']
        ZL_code_02 = data['ZL_code_02']
        ZL_code_03 = data['ZL_code_03']
        code_list.append(ZL_code_01)
        code_list.append(ZL_code_02)
        code_list.append(ZL_code_03)
        return code_list

    # 添加顺丰模板
    def add_SF_template(self,data):
        # 数据处理
        Template_name = data['Template']
        Freight_Payment = data['Freight_Payment']
        CustId = data['CustId']
        Business_type = data['Business_type']
        # 选择面单类型
        Choice_template_statu = self.Choice_template(Template_name)
        if Choice_template_statu:
            # 选择付款方式
            self.express.click_Payment_mode(Freight_Payment)
            if Freight_Payment=='寄付月结' or Freight_Payment =='第三方付月结' and len(CustId)!=0:
                click_PayCustId_statu = self.express.click_PayCustId(CustId)
                if click_PayCustId_statu==False or click_PayCustId_statu==None:
                    logger.info('月结卡号【%s】不存在，或选择月结卡号出错'%CustId)
            # 选择业务类型
            click_expressType_statu = self.express.click_Business_type(Business_type)
            if click_expressType_statu==None:
                logger.info('【%s】业务类型不存在，默认为顺丰标快'%Business_type)
            # 添加模板
            self.express.click_savetemplate()
            # 判断是否添加成功
            save_statu,save_tip = self.save_statu()
            if save_statu==True:
                add_SF_template_statu=True
                logger.info('添加SF模板【%s】成功~' % Template_name)
            else:
                add_SF_template_statu = False
                logger.info('添加SF模板【%s】失败，%s' % (Template_name,save_tip))
        else:
            # 取消添加
            self.express.click_canceltemplate()
            add_SF_template_statu = False
        return add_SF_template_statu

    # 添加直连模板
    def add_ZL_template(self,data):
        Template_name = data['Template']
        # 选择面单类型
        Choice_template_statu = self.Choice_template(Template_name)
        if Choice_template_statu:
            # 填写直连商家信息
            code_list = self.ZL_info_list(data)
            input_ZL_code_statu = self.express.input_ZL_code(code_list)
            if input_ZL_code_statu:
                # 添加模板
                self.express.click_savetemplate()
                # 判断是否添加成功
                save_statu, save_tip = self.save_statu()
                if save_statu == True:
                    add_ZL_template_statu = True
                    logger.info('添加ZL模板【%s】成功~' % Template_name)
                else:
                    add_ZL_template_statu = False
                    logger.info('添加ZL模板【%s】失败，%s' % (Template_name, save_tip))
            else:
                add_ZL_template_statu = False
                logger.info('填写ZL商家信息失败...')
        else:
            self.express.click_canceltemplate()
            add_ZL_template_statu = False
        return add_ZL_template_statu

    # 添加菜鸟模板
    def add_CN_template(self,data):
        Template_name = data['Template']
        Cainiao_shop = data['Cainiao_shop']
        Cainiao_address = data['Cainiao_address']
        # 选择面单类型
        Choice_template_statu = self.Choice_template(Template_name)
        if Choice_template_statu:
            # 判断是菜鸟面单还是非淘面单
            Shop_statu = self.express.is_CaiNiaoShop()
            if Shop_statu=='feitao':
                logger.info('暂时不支持非淘电子面单测试，已跳过...')
                self.express.click_canceltemplate()
                add_CN_template_statu = False
            else:
                # 选择菜鸟店铺
                click_cainiao_shop_statu,e = self.express.click_cainiao_shop(Cainiao_shop)
                if click_cainiao_shop_statu:
                    # 选择菜鸟地址
                    click_cainiao_adress_status= self.express.click_cainiao_adress(Cainiao_address)
                    if click_cainiao_adress_status:
                        # 添加模板
                        self.express.click_savetemplate()
                        # 判断是否添加成功
                        save_statu, save_tip = self.save_statu()
                        if save_statu == True:
                            logger.info('添加CN模板【%s】成功~' % Template_name)
                            add_CN_template_statu = True
                        else:
                            add_CN_template_statu = False
                            logger.info('添加CN模板【%s】失败，%s' % (Template_name, save_tip))
                elif click_cainiao_shop_statu==None:
                    logger.info('菜鸟店铺【%s】不存在..跳过该模板'%Cainiao_shop)
                    self.express.click_canceltemplate()
                    add_CN_template_statu = False
                else:
                    logger.info('选择菜鸟店铺【%s】失败,%e,跳过该模板'%(Cainiao_shop,e))
                    add_CN_template_statu = False
        else:
            self.express.click_canceltemplate()
            add_CN_template_statu = False
            logger.info('添加CN模板【%s】失败' % Template_name)
        return add_CN_template_statu

    # 添加套打模板
    def add_TD_template(self,data):
        Template_name = data['Template']
        Choice_template_statu = self.Choice_template(Template_name)
        # 选择面单类型
        if Choice_template_statu:
            # 添加模板
            self.express.click_savetemplate()
            # 判断是否添加成功
            save_statu, save_tip = self.save_statu()
            if save_statu == True:
                add_TD_template_statu = True
                logger.info('添加TD模板【%s】成功~' % Template_name)
            else:
                add_TD_template_statu = False
                logger.info('添加TD模板【%s】失败，%s' % (Template_name, save_tip))
        else:
            add_TD_template_statu=False
        return add_TD_template_statu

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
            self.express.click_tip_button()
            save_statu = False
        return save_statu,save_tip

    # 添加模板
    def add_template_main(self):
        # 获取模板数据
        template_data = self.get_template_data()
        # 加载页面方法
        self.home_pg.click_Express()
        for data in template_data:
            Logistics_company = data['Logistics_company']  #物流公司
            Template_name = data['Template']  #模板
            self.express.click_add()
            self.express.click_select()
            self.express.input_logistics_company(Logistics_company)

            # 当前模板在模板列表中才进行下一步操作，否则跳过
            # if Temlpalte_name in label_text:
            if '顺丰' in Template_name:
                self.add_SF_template(data)
            elif '直连' in Template_name:
                self.add_ZL_template(data)
            elif '菜鸟' in Template_name:
                self.add_CN_template(data)
            elif '套打' in Template_name:
                self.add_TD_template(data)
            else:
                logger.info('当前模板%s,未在模板列表中已跳过该模板...'%Template_name)
            self.express.sleep(1)



class delete_template(Load_drive):

    def setUp(self):
        self.express = expressinstall(self.browser)
        self.home_pg = home_page(self.browser)

    def get_wait_delete_template_count(self):
        template_count=0
        lis = self.express.get_del_template_li()
        for li in lis:
            template_count = template_count+1
        return template_count

    #删除模板主方法
    def delete_template_main(self):
        self.home_pg.click_Express()
        self.express.click_GlobalSettings()
        template_count = self.get_wait_delete_template_count()
        logger.info('待删除的模板总数为%s个'%template_count)
        # 循环删除所有模板
        for item in range(template_count-1):
            lis = self.express.get_del_template_li()
            template_text_before =self.express.get_01template_name()
            logger.info('当前待删除的模板为%s'%template_text_before)
            self.express.click_del_template_li(lis[0])
            self.express.click_delete()
            template_text_after = self.express.get_01template_name()
            if template_text_before!=template_text_after:
                delete_template_statu = True
                logger.info('删除模板%s成功'%template_text_before)
            else:
                delete_template_statu = False
                logger.info('删除模板%s失败' % template_text_before)

