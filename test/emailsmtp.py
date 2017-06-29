#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-09 15:21:00
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

# from email.mime.text import MIMEText
# msg=MIMEText('hello send by caowei ','plain','utf-8')

# from_address=input('From:')
# password=input("Password:")
# to_addr=input("To:")
# smtp_server=input("SMTP server:")

# import smtplib
# server=smtplib.SMTP(smtp_server,587)
# server.set_debuglevel(1)
# server.login(from_address,password)
# server.sendmail(from_address, to_addr, msg.as_string())
# server.quit()

import smtplib
from email.mime.text import MIMEText
from email.header import Header
server = smtplib.SMTP('smtp.163.com', 25)
server.login('18656553267@163.com', '123456789ab')
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = '18656553267@163.com <18656553267@163.com>'
msg['Subject'] = Header(u'text', 'utf8').encode()
msg['To'] = u' <caocaosze@qq.com>'
server.sendmail('18656553267@163.com', ['caocaosze@qq.com'], msg.as_string())