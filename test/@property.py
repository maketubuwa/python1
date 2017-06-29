#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 20:57:59
# @Author  : mx (mengxiang@xiangcloud.com.cn)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$

class Screen(object):
	
	@property
	def width(self):
		return self.width1

	@width.setter
	def width(self,width1):
		self.width1=width1

	@property
	def length(self):
		return self.length1

	@length.setter
	def length(self,length1):
		self.length1=length1

	@property
	def resolution(self):
		return s.width1 * s.length1

		
s=Screen()
s.width1=67
s.length1=45
print(s.width,s.length)
print(s.resolution)