#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-06 19:20:59
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$


import logging
logging.basicConfig(level=logging.INFO)


class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
	def __setattr__(self,key,value):
		self[key]=value		

d=Dict(a=1,b='caowei')
print(d["a"])