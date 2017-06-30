#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-30 15:55:14
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import os
f=open('test8.txt','r')
c=f.readlines()
l=[]
for i in c:
	l.append(i)
sum=0
l1=[]
l2=[]
for z in l:
	a=z.split(',')
	if int(a[2])<60:
		l1.append(a[0])
	if a[0].find('L')==0:
		l2.append(a[0])
	sum += int(a[2])
print(l1)
print(l2)	
print(sum)

k=[]
for i in list(f):
	i=i.capitalize()
	k.append(i)
fp=open('test8.txt','w')
fp.writelines(k)
f.close()