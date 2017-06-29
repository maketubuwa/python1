#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 18:42:11
# @Author  : mx (mengxiang@xiangcloud.com.cn)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$

import types

def fn():
	pass

print(type(fn)==types.FunctionType)

a=isinstance('a',str)
print(a)
b=isinstance([1,2,3,4],(list,tuple))
print(b)
#print(dir('ABC'))
print('type(\'abc\')==str?', type('abc')==str)
