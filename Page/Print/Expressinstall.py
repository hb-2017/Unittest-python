#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from Page.Page_base import Basepage

class expressinstall(Basepage):

    add = 'id=>addWaybillTemplateBtn'  #添加模板
    edit = 'id=>editWaybillTemplate'   #编辑模板
    GlobalSettings = 'id=>printGlobalSettings'   #全局设置

    select = 'id=>select2-imgType_selectVal-container'  #搜索框
    logistics_company = 'class_name=>select2-search__field' # 输入框

    template_img = 'class_name=>imgType_img' # 模板图片
    template_div = 'id=>printTypeDiv' # 所有模板的div
    template_label = 'label'
    Payment_mode_01 = 'class_name=>payTypeGroup_1' #寄付月结
    Payment_mode_02 = 'class_name=>payTypeGroup_2' #到付现结
    Payment_mode_03 = 'class_name=>payTypeGroup_3' #寄付现结
    Payment_mode_04 = 'class_name=>payTypeGroup_4' #第三方付月结
    PayCustId = 'id=>addTempPayCustId' #月结卡号
    Business_type = 'id=>expressTypeSelect'  # 业务类型下拉

    ZL_code_div = 'id=>imgType_02'


    savetemplate = 'id=>saveWaybillTemplateBtn' #添加按钮
    canceltemplate = 'id=>cancelWaybillTemplateBtn' #取消按钮

    save_tip = 'x=>/html/body/div[10]/p' # 保存提示
    tip_button = 'class_name=>confirm' # 提示框内的确认


    #点击添加模板
    def click_add(self):
        self.click(self.add)
        self.sleep(1)

    #点击搜索框
    def click_select(self):
        self.click(self.select)
        self.sleep(1)

    #输入物流公司
    def input_logistics_company(self,logistics_company):
        self.input(self.logistics_company,logistics_company)
        self.Send_keys_ENTER(self.logistics_company)
        self.sleep(1)

    # 查询当前物流公司的所有面单并去重
    def select_template_div(self):
        div = self.find_element(self.template_div)
        return div

    # 点击面单类型
    def click_template_img(self):
        self.click(self.template_img)
        self.sleep(1)

    # 选择付款方式
    def click_Payment_mode(self,payType):
        if payType=='寄付月结':
            self.click(self.Payment_mode_01)
        elif payType=='到付现结':
            self.click(self.Payment_mode_02)
        elif payType=='寄付现结':
            self.click(self.Payment_mode_03)
        elif payType=='第三方付月结':
            self.click(self.Payment_mode_04)
        else:
            self.click(self.Payment_mode_01)
        self.sleep(1)

    # 点击月结卡号
    def click_PayCustId(self,CustId):
        select = self.find_element(self.PayCustId)
        CustIds = select.find_elements_by_tag_name('option')
        for CustId_ in CustIds:
            CustId_text = CustId_.text
            if CustId_text ==CustId:
                try:
                    CustId_.click()
                    click_PayCustId_statu = True
                except:
                    click_PayCustId_statu = False
                break
        else:
            click_PayCustId_statu = None
        self.sleep(1)
        return click_PayCustId_statu


    # 选择业务类型
    def click_Business_type(self,Business_type):
        select = self.find_element(self.Business_type)
        options = select.find_elements_by_tag_name('option')
        for option in options:
            option_text = option.text
            if Business_type ==option_text:
                try:
                    option.click()
                    click_expressType_statu = True
                except :
                    click_expressType_statu = False
                break
        else:
            click_expressType_statu=None
        self.sleep(1)
        return click_expressType_statu

    # 填写直连商家信息
    def input_ZL_code(self,code_list):
        div = self.find_elements(self.ZL_code_div)[1]
        inputs = div.find_emelenet_by_tag_name('input')
        for item,input in enumerate(inputs):
            try:
                input.sen_keys(code_list[item])
            except:
                input_ZL_code_statu = False
        else:
            input_ZL_code_statu = True
        return input_ZL_code_statu












    # 添加模板
    def click_savetemplate(self):
        self.click(self.savetemplate)
        self.sleep(1)

    # 取消模板
    def click_canceltemplate(self):
        self.click(self.canceltemplate)
        self.sleep(1)

    # 获取保存提示
    def get_save_tip(self):
        tip = self.get_elemeent_text(self.save_tip)
        return tip

    # 点击提示内的确认
    def click_tip_button(self):
        self.click(self.tip_button)
        self.sleep(1)
