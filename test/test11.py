#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-30 17:11:35
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import os
import re
import time 
import datetime as dt
from datetime import datetime

print(time.time())
print(time.clock())
# print('start')
# time.sleep(1)
# print('wake up')
# print(time.gmtime())
# print(time.localtime())
# print(time.mktime(time.localtime()))
	
t=dt.datetime(2012,3,4,20,1)
print(t)
format = "output-%Y-%m-%d-%H%M%S.txt" 
str    = "output-1997-12-23-030000.txt" 
t      = datetime.strptime(str, format)
print(t)
t_next = dt.datetime(2012,9,5,23,30)
print(t_next.strftime(format))