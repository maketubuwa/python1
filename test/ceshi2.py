#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 21:41:33
# @Author  : mx (mengxiang@xiangcloud.com.cn)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$

class  A(object):
	def run():
		print('baba')

class B(A):
	def run():
		print('erzi')

class C(B):
	def run():
		print('sunzi')	

def f():
	run()
f(C())

						
		
		
