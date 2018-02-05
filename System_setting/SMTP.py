#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
port = 0                   # 端口
sender="m18664594496@163.com"   #用户名
psw="wwwhubiao165++"   #密码
receiver = 'www.165hubiao.cn@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# ----------2.编辑邮件的内容------
subject = "这个是主题163"
body = '<p>这个是发送的163邮件</p>'  # 定义邮件正文为html格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "www.165hubiao.cn@qq.com"
msg['subject'] = subject


# ----------3.发送邮件------
smtp = smtplib.SMTP()
smtp.connect(mail_host)                                  # 连服务器
a= smtp.login(sender, psw)                                     # 登录
print(a)
smtp.sendmail(sender, receiver, msg.as_string())  # 发送

smtp.quit()


