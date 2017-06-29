#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-06 15:53:07
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$
from enum import Enum,unique

class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>100:
			raise StopIteration()
		return self.a


class Fib1(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a	




class Student(object):
	def __init__(self,name):
		self.name=name
	def __getattr__(self,attr):
		if attr=='score':
			return 99
s=Student('caowei')


class num(object):
	def __init__(self,name):
		self.name=name
	def __call__(self):
		print(r"my name is %s" % self.name)

n=num('caowei')

class Chain(object):
	def __init__(self,path='http://study.163.com/category/python#/?ot=50'):
		self._path=path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))
	def __str__(self):
		return self._path
	__repr__ = __str__	
# L=Chain().ot
# print(L)


Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#for name,member in Month.__members__.items():
#	print(name,'=>',member,',',member.value)

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(Weekday(1))
print(Weekday.Thu.value)

#for name,member in Weekday.__members__.items():
#	print(name,'=>',member,',',member.value)