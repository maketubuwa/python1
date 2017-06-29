#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 21:16:12
# @Author  : mx (mengxiang@xiangcloud.com.cn)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$

class Screen(object):
    @property
    def size(self):
         return self._size
    @size.setter
    def size(self,width,height):
        self._size1=self.width
        self._size2=self.height
    @property
    def resolution(self):
        return (self.width)*(self.height)

s=Screen()
s.size.width=23
s.size.height=24
print(s.resolution)