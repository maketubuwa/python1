#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 17:06:08
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$


f=open('D:/python/test/东邪西毒.txt','r',encoding='utf-8', errors='ignore')

for line in f.readlines():
	print(line.strip())