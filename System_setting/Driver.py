#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import  configparser
import os
from selenium import webdriver
from System_setting.Logger import Logger
from System_setting.Root_directory import Root_xpath

#实例化Logger类
logger = Logger(logger = "Driver").getlog()

class Driver():
    # 获取项目绝对路劲并且组合需要的新路径
    x = Root_xpath()
    dir = x.get_root_path()
    # 获取浏览器驱动的路径
    Chrome_driver_path = dir + '/tools/chromedriver.exe'
    Ie_driver_path = dir + '/tools/IEDriverServer.exe'

    # def __init__(self,driver):
    #     self.driver = driver

    def open_browser(self):
    # def open_browser(self):
        #实例化配置文件类
        config = configparser.ConfigParser()
        #获取配置文件路劲,并读取
        # driver_config_xpath = os.path.dirname(os.path.abspath('.'))+'/config/driver.ini'
        # url_manage_xpath = os.path.dirname(os.path.abspath('.'))+'/config/url.ini'
        driver_config_xpath = self.dir + '/Data/Configs/driver.ini'
        url_manage_xpath = self.dir + '/Data/Configs/url.ini'
        config.read(driver_config_xpath)
        #读取config的驱动,url信息
        browser = config.get('browserType','browserName')
        logger.info("即将启动的浏览器驱动为：%s 浏览器." % browser)

        config.read(url_manage_xpath)
        url = config.get("testServer", "URL")
        logger.info("即将进入的域名是: %s" % url)
        # 驱动启动，写日志
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("开始打开Firefox浏览器...")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.Chrome_driver_path)
            logger.info("开始打开Chrome浏览器...")
        elif browser == "IE":
            driver = webdriver.Ie(self.Ie_driver_path)
            logger.info("开始打开IE浏览器...")
        # 打开网址并且写入日志
        driver.get(url)
        logger.info("进入域名: %s" % url)
        driver.maximize_window()
        logger.info("浏览器窗口最大化.")
        driver.implicitly_wait(10)
        logger.info("浏览器最大等待时间为10秒")
        return driver

    # 退出浏览器
    def quit_browser(self):
        logger.info("退出浏览器...")
        self.driver.quit()


