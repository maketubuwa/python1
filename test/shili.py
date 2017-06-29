#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 19:22:23
# @Author  : mx (mengxiang@xiangcloud.com.cn)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$

class Student(object):
	"""docstring for Student"""
	def __init__(self,name):
		self.name=name

s=Student('bob')
s.score=90

print(s.name,s.score)

class Student1(object):
	name='Student1'

s=Student1()
print(s.name)	
print(Student1.name)
s.name='michael'
print(s.name)
print(Student1.name)
