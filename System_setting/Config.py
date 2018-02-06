#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-31 18:33:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import configparser
from System_setting.Logger import Logger
from System_setting.Root_directory import Root_xpath

logger = Logger(logger='Config').getlog()

class Config():
    def __init__(self):
        self.config = configparser.ConfigParser()
        xpath = Root_xpath()
        self.xpath = xpath.get_root_path()

    '''
        参数
        config_xpath 配置文件路劲 类型为str
        config_title 配置文件组名 类型为list
        config_value 配置文件键名 类型为list

        返回值
        False 获取配置文件失败，值为空
        values 配置文件信息
    '''
    def config_data(self, config_name, config_title, config_value):
        values = []
        try:
            if len(config_name) > 0:
                config_xpath = self.xpath+'/Data/Configs/'+config_name+'.ini'
                self.config.read(config_xpath, encoding="utf-8-sig")
                # 单组配置读取
                if len(config_title) == 1:
                    value = []
                    for item in config_value:
                        item = self.config.get(''.join(config_title), item)
                        value.append(item)
                    values.append(value)
                    values = values[0]
                    logger.info('获取单组配置信息：%s 成功' % values)
                # 多组配置读取
                elif len(config_title) > 1:
                    for title in config_title:
                        value = []
                        for item in config_value:
                            item = self.config.get(title, item)
                            value.append(item)
                        values.append(value)
                        logger.info('获取多组配置信息：%s 成功 ' % values)
                elif len(config_title) == 0 or len(config_title) == None or len(config_value) == 0 or len(
                        config_value) == None:
                    logger.error('配置文件组名或组键为空,获取配置失败...')
                    return False
                else:
                    logger.error('配置文件路劲为空,获取配置失败...')
                    return False
            else:
                logger.error('配置文件名称长度小于1，请检查...')
                return False
            return values
        except Exception as e:
            logger.error('获取配置信息失败:%s' % e)
            return False

		




