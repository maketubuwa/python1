#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 19:40:23
# @Author  : mx (mengxiang@xiangcloud.com.cn)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$

class Student(object):
	pass

s=Student()
s.name='micheal'
print(s.name)

def set_age(self, age):
	self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)

s1=Student()

def set_score(self,score):
	self.score=score
Student.set_score=set_score

s.set_score(12)
s1.set_score(13)
print(s1.score,s.score)

class Student1(object):
	__slots__=('name','age')

s2=Student1()
s2.name='caowei'
s2.age=26
print(s2.name,s2.age)

