#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import time
import smtplib
from System_setting.Config import Config
from email.mime.text import MIMEText
from System_setting.Root_directory import Root_xpath
from email.mime.multipart import MIMEMultipart  #发送附件
from email.header import Header
from System_setting.Logger import Logger

logger = Logger('SMTP').getlog()


class Smtp():

    # 获取
    def __init__(self,report_path):
        self.report_path = report_path
        report = self.report_path.split('/')
        self.report = report[-1]


    #邮箱服务信息初始化
    def smtp_Initialization(self,config_title):
        try:
            config_value = ['service', 'port', 'sender', 'password', 'receiver']
            config = Config()
            data = config.config_data('SMTP',config_title, config_value)
            self.mail_host = data[0]
            self.port = data[1]
            self.sender = data[2]
            self.password = data[3]
            receiver = data[4]
            self.receiver = receiver.split(',')
            # self.receiver = list(receiver)
            logger.info('%s邮箱初信息初始化完成'%config_title)
        except BaseException as e:
            logger.info('%s邮箱信息初始化失败%s'%(config_title,e))


    # 读取附件
    def get_Enclosure(self,file_path):
        try:
            with open(file_path,'rb') as fp:
                emil_bady = fp.read()
            return emil_bady
        except BaseException as e:
            logger.error('读取附件异常：%s'%e)


    # 发送html信息
    def get_html(self,msg,mail_body):
        try:
            bodys = MIMEText(mail_body, "html", "utf-8")
            msg.attach(bodys)
        except BaseException as e:
            logger.error('读取文本信息异常：%s'%e)


    # 使用163邮箱发送
    def smtp163(self,conout=1):
        logger.info('邮箱发送已选择163邮箱...')
        conout = conout + 1
        try:
            self.smtp_Initialization(['163_smtp'])
            # 创建一个带附件msg实例
            msg = MIMEMultipart()
            # 构造附件
            emil_bady = self.get_Enclosure(self.report_path)
            att = MIMEText(emil_bady, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename=%s'%self.report
            msg.attach(att)
            self.get_html(msg, emil_bady)
            # 邮件头
            msg['from'] = self.sender
            msg['to'] = ','.join(self.receiver)
            msg['subject'] = '测试报告'
            # 开始发送邮件
            self.Send_email(msg)
        except BaseException as e:
            logger.error('邮箱发送失败，正在重新发送，已发送次数:%s'%(conout-1))
            if conout<4:
                self.smtp163(conout)
            else:
                logger.error('邮件发送错误次数超过3次，取消发送...')


    # 使用qq邮箱发送
    def smtpqq(self,conout=1):
        logger.info('邮箱发送已选择qq邮箱...')
        conout = conout + 1
        try:
            self.smtp_Initialization(['qq_smtp'])
            # 创建一个带附件msg实例
            msg = MIMEMultipart()
            # 构造附件
            emil_bady = self.get_Enclosure(self.report_path)
            att = MIMEText(emil_bady, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename=%s'%self.report
            msg.attach(att)
            self.get_html(msg, emil_bady)
            # 邮件头
            msg['from'] = self.sender
            msg['to'] = ';'.join(self.receiver)
            msg['subject'] = '测试报告'
            # 开始发送邮件
            self.Send_email(msg)
        except BaseException as e:
            logger.error('邮箱发送失败，正在重新发送，已发送次数:%s'%(conout-1))
            if conout<4:
                self.smtpqq(conout)
            else:
                logger.error('邮件发送错误次数超过3次，取消发送...')


    #发送邮件
    def Send_email(self,msg):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_host)  # 连服务器
            a = smtp.login(self.sender, self.password)  # 登录
            print(a)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())  # 发送
            smtp.quit()
            logger.info('邮件发送成功...')
        except BaseException as e:
            logger.info('邮件发送失败：%s...'%e)


    # 发送邮件2
    def Send_email2(self, msg):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_host)  # 连服务器
            a = smtp.login(self.sender, self.password)  # 登录
            print(a)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())  # 发送
            smtp.quit()
            logger.info('邮件发送成功...')
        except BaseException as e:
            logger.info('邮件发送失败：%s...' % e)





