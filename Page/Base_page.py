#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import time
from selenium.common.exceptions import NoSuchElementException
import os
from System_setting.Logger import Logger
from selenium.webdriver.common.action_chains import *       #用于鼠标事件
from selenium.webdriver.common.keys import Keys
from System_setting.Screenshot import Screen


#实例化日志类
logger = Logger(logger = 'Basepage').getlog()

class Basepage():
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类.
    """

    def __init__(self,driver):
        self.browser = driver
        self.Screen = Screen()


    #退出浏览器
    def quir_browser(self):
        self.browser.quit()

    #浏览器前进
    def browser_forward(self):
        self.browser.forward()
        logger.info('浏览器页面前进...')

    #浏览器后退
    def browser_back(self):
        self.browser.back()
        logger.info('浏览器页面后退...')

    def refresh(self):
        self.browser.refresh()
        logger.info('浏览器页面刷新...')

    #隐式等待
    def browser_wait(self,seconds):
        self.browser.implicitly_wait(seconds)
        logger.info('等待页面加载完成...最多等待%s秒'%seconds)

    # 获取网页标题
    def get_page_title(self):
        logger.info("获取当前页面标题为： %s" % self.browser.title)
        return self.browser.title


    # 判断网页标题和预期是否相符
    def is_page_title(self, title):
        page_title = self.browser.title
        if page_title == title:
            logger.info(' 预期页面标题：%s 与实际标题%s相符' % (title, page_title))
            return True
        else:
            logger.error(' 预期页面标题：%s 与实际标题%s不相符' % (title, page_title))
            return False


    # 获取当前窗口的句柄
    def current_browser_windows_handle(self):
        try:
            current_handle = self.browser.current_window_handle
            logger.info('获取当前窗口句柄成功,%s'%current_handle)
            return current_handle
        except NameError as e:
            logger.error('获取当前窗口的句柄失败,%s' % e)


    # 获取当前所有窗口句柄
    def all_borwser_windows(self):
        try:
            handles = self.browser.window_handles
            logger.info('获取所有窗口句柄成功,%s'%handles)
            return handles
        except NameError as e:
            logger.error('获取所有窗口的句柄失败,%s' % e)


    # 切换窗口
    def switch_browser_windows(self,handles,browser_num=None,handle_name=None):
        if handle_name==None:
            # 按数字切换
            if browser_num==None:
                # 什么都没填默认切换到下一个
                for item,ha in enumerate(handles):
                    if item==1:
                        self.browser.switch_to_window(ha)
                        logger.info('当前工作窗口已切换为%s' % ha)
                        break
            else:
                for item,ha in enumerate(handles):
                    if item==browser_num:
                        self.browser.switch_to_window(ha)
                        logger.info('当前工作窗口已切换为%s' % ha)
                        break
            # 按句柄切换
        else:
            try:
                for ha in handles:
                    if ha==handle_name:
                        self.browser.switch_to_window(ha)
                        logger.info('当前工作窗口已切换为%s'%ha)
                        break
            except BaseException as e:
                logger.error('切换窗口失败,%e'%e)


    #关闭当前窗口
    def browser_close(self):
        try:
            self.browser.colse()
            logger.info('关闭当前窗口页...')
        except NameError as e:
            logger.error('关闭浏览器窗口页失败： %s' % e)

    # #截图并且保存
    # def get_windows_img(self):
    #     """
    #         在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
    #     """
    #     file_path = os.path.dirname(os.path.abspath('.'))+'/screenshots/'
    #     rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    #     screenname = file_path+rq+'.png'
    #     try:
    #         self.browser.get_screenshot_as_file(screenname)
    #         logger.info('Had take screenshot and save to folder : /screenshots')
    #     except NameError as e:
    #         logger.error('Failed to take screenshot! %s' % e)
    #         self.get_windows_img()


    # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''

        #分割元素
        if '=>' not in selector:
            return self.browser.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.browser.find_element_by_id(selector_value)
                logger.info("通过键 %s 值 : %s "
                            "找到元素 ' %s ' 成功 "% (selector_by, selector_value,element.text))
            except NoSuchElementException as e:
                logger.error("寻找元素失败，元素未找到: %s" % e)
                self.Screen.get_windows_img('寻找元素失败')  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.browser.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.browser.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.browser.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.browser.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.browser.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.browser.find_element_by_xpath(selector_value)
                logger.info("通过键 %s 值 : %s "
                            "找到元素 ' %s ' 成功 " % (selector_by, selector_value, element.text))
            except NoSuchElementException as e:
                logger.error("寻找元素失败，元素未找到: %s" % e)
                self.Screen.get_windows_img('寻找元素失败')
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.browser.find_element_by_css_selector(selector_value)
        else:
            raise NameError("请输入一个有效的目标元素类型.")
        return element



    def find_elements(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        elements = ''
        #分割元素
        if '=>' not in selector:
            return self.browser.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == "i" or selector_by == 'id':
            try:
                elements = self.browser.find_elements_by_id(selector_value)
                logger.info("通过键 %s 值 : %s "
                            "找到元素成功 " % (selector_by, selector_value,))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.Screen.get_windows_img('寻找元素失败')  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            elements = self.browser.find_elements_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            elements = self.browser.find_elements_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            elements = self.browser.find_elements_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            elements = self.browser.find_elements_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            elements = self.browser.find_elements_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                elements = self.browser.find_elements_by_xpath(selector_value)
                logger.info("通过键 %s 值 : %s ""找到元素成功 " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.Screen.get_windows_img('寻找元素失败')  # take screenshot
        elif selector_by == "s" or selector_by == 'selector_selector':
            elements = self.browser.find_elements_by_css_selector(selector_value)
        else:
            raise NameError("请输入一个有效的目标元素类型.")
        return elements


    # 输入
    def input(self, selector, text):
        el = self.find_element(selector)
        el_text = el.text
        # el.clear()
        try:
            el.send_keys(text)
            logger.info("成功在%s框输入文字信息：%s" % (el_text,text))
        except NameError as e:
            logger.error("输入信息发生异常 %s" % e)
            self.Screen.get_windows_img('输入信息失败')  # take screenshot

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        el_text = el.text
        try:
            el.clear()
            logger.info("文本框信息：%s已被清除."%el_text)
        except NameError as e:
            logger.error("清除文本框发生异常 %s" % e)
            self.Screen.get_windows_img('清除文本框信息失败')  # take screenshot

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        el_text = el.text
        try:
            el.click()
            logger.info("元素：%s 被点击" % el_text)
        except NameError as e:
            logger.error("点击元素发生异常 %s" % e)
            self.Screen.get_windows_img('点击元素失败')  # take screenshot


    #判断元素是否存在
    def element_is_dispalynd(self,selector):
        # 分割元素
        if '=>' not in selector:
            try:
                return self.browser.find_element_by_id(selector)
            except:
                element_dispaly = False
                return element_dispaly
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        try:
            if selector_by == "i" or selector_by == 'id':
                element_dispaly = self.browser.find_element_by_id(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "n" or selector_by == 'name':
                element_dispaly = self.browser.find_element_by_name(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "c" or selector_by == 'class_name':
                element_dispaly = self.browser.find_element_by_class_name(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "l" or selector_by == 'link_text':
                element_dispaly = self.browser.find_element_by_link_text(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "p" or selector_by == 'partial_link_text':
                element_dispaly = self.browser.find_element_by_partial_link_text(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "t" or selector_by == 'tag_name':
                element_dispaly = self.browser.find_element_by_tag_name(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "x" or selector_by == 'xpath':
                element_dispaly = self.browser.find_element_by_xpath(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "s" or selector_by == 'selector_selector':
                element_dispaly = self.browser.find_element_by_tag_selector_selector(selector_value).is_displayed()
                return element_dispaly
        except:
            element_dispaly = False
            return element_dispaly


    #休眠
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("系统休眠%s秒" % seconds)


    #获取元素文本
    def get_elemeent_text(self,selector):
        el = self.find_element(selector)
        elemeent_text = el.text
        logger.info('获取元素文本信息 %s'%elemeent_text)
        return elemeent_text


    #鼠标悬浮
    def Mouse_suspension(self,selector):
        el = self.find_element(selector)
        el_text = el.text
        # 鼠标移到悬停元素上
        try:
            chain = ActionChains(self.browser)
            chain.move_to_element(el).perform()
            logger.info('鼠标移动并悬浮在元素：%s上'%el_text)
        except BaseException as e:
            logger.error('鼠标悬浮发生异常 :%s'%e)
            self.Screen.get_windows_img('鼠标悬浮元素失败')  # take screenshot


    #键盘输入
    def Send_keys_ENTER(self,selector):
        el = self.find_element(selector)
        try:
            el.send_keys(Keys.ENTER)
        except BaseException as e:
            logger.error('输入ENTER键失败 %s' % e)

    #敲击ESC
    def Send_keys_esc(self,selector):
        el = self.find_element(selector)
        try:
            el.send_keys(Keys.ESCAPE)
        except BaseException as e:
            logger.error('输入%s键失败,%s' % ('ESC',e))

