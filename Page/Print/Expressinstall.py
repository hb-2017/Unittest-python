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
    ZL_code_div = 'id=>imgType_02' # 直连商家信息的div
    CN_shop_div = 'class_name=>isCaiNiaoShop' # 选择菜鸟店铺的div
    AddCainiaoShops = 'id=>addTempCainiaoShops' # 菜鸟店铺下拉
    Cainiaoaddress = 'x=>//*[@id="cainiaoShopAddress"]/div[2]/div[2]/div[2]' #菜鸟店铺的地址

    del_template_div = 'id=>nestable' # 删除模板的div
    del_template_li = 'class_name=>dd-item' #删除模板的li
    delete_confirm = 'class_name=>confirm' #删除模板提示的删除按钮
    delete_cancel = 'class_name=>cancel' # 删除模板提示的取消按钮
    del_template_name = 'class_name=>dd-handle' # 模板的名称

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
        div = self.find_elements(self.ZL_code_div)
        inputs = div[1].find_elements_by_tag_name('input')
        for item,input in enumerate(inputs):
            try:
                input.send_keys(code_list[item])
            except:
                input_ZL_code_statu = False
                break
        else:
            input_ZL_code_statu = True
        self.sleep(1)
        return input_ZL_code_statu

    # 判断是否有菜鸟店铺
    def is_CaiNiaoShop(self):
        dispalynd = self.element_is_dispalynd(self.CN_shop_div)
        if dispalynd==False:
            Shop_statu='feitao'
        else:
            Shop_statu='cainiao'
        return Shop_statu

    # 选择菜鸟店铺
    def click_cainiao_shop(self,cainiao_shop):
        e = ''
        select= self.find_element(self.AddCainiaoShops)
        options = select.find_elements_by_tag_name('option')
        for option in options:
            option_text = option.text
            if option_text==cainiao_shop:
                try:
                    option.click()
                    click_cainiao_shop_statu = True
                except BaseException as e:
                    click_cainiao_shop_statu = False
                break
        else:
            click_cainiao_shop_statu=None
        self.sleep(1)
        return click_cainiao_shop_statu,e

    # 点击菜鸟地址
    def click_cainiao_adress(self,Cainiao_address):
        if len(Cainiao_address)==0:
            Cainiao_address=0
        e = ''
        if isinstance(Cainiao_address,int):

            div = self.find_element(self.Cainiaoaddress)
            label = div.find_elements_by_tag_name('label')[Cainiao_address]
            try:
                label.click()
                click_cainiao_adress_statu = True
            except BaseException as e:
                click_cainiao_adress_statu = False
        else:
            e = '菜鸟地址数据类型错误，请使用int...'
            click_cainiao_adress_statu = False
        self.sleep(1)
        return click_cainiao_adress_statu,e

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

    # 全局设置
    def click_GlobalSettings(self):
        self.click(self.GlobalSettings)
        self.sleep(1)

    # 删除模板的lis
    def get_del_template_li(self):
        lis = self.find_elements(self.del_template_li)
        return lis

    # 获取第一个模板的名称
    def get_01template_name(self):
        lis = self.get_del_template_li()
        template_list = lis[0].find_element_by_class_name(self.del_template_name)
        template_name = template_list.text
        return template_name

    # 点击删除模板
    def click_del_template_li(self,li):
        try:
            li.find_element_by_tag_name('i').click()
        except:
            pass

    # 删除模板的取消按钮
    def click_cancel(self):
        self.click(self.delete_cancel)
        self.sleep(0.5)

    # 删除模板的删除按钮
    def click_delete(self):
        self.click(self.delete_confirm)
        self.sleep(0.5)