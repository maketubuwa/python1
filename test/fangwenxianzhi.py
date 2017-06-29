#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-02 18:55:00
# @Author  : mx (mengxiang@xiangcloud.com.cn)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$

class Student(object):
	"""dname,scoretring for Student"""
	def __init__(self, name,score):
		self.__name=name
		self.__score=score

	def get_name(self):
		return self.__name
	def set_name(self,name):
		if name is not null:
			self.__name=name
		else:
			raise ValueError('bad name')

	def set_score(self,score):
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('bad score')			
	def get_score(self):
		return self.__score	

	def print_score(self):
		print('%s %s' %(self.__name,self.__score))	

bart=Student('caowei',23)
print(bart.get_name())
print(bart.get_score())
bart.set_score(65)
print('修改后的年龄为:' + str(bart.get_score()))