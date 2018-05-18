#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-18 14:36:51
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

i=int(input("请输入利润总额："))
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=1
for idx in range(0,6):
	if i > arr[idx]:
		r+=(i-arr[idx])*rat[idx]
		print((i-arr[idx])*rat[idx])
		i=arr[idx]
print(r)
