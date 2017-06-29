#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 18:34:40
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import os


# def get_fileAbs_Path(url):
# 	L1 = os.listdir(url)
# 	L2 = os.path.abspath(url)
# 	print(L1)

# def get_next_dir(url):
# 	L1 = os.listdir(url)
# 	for i in L1:
# 		if os.listdir(url) is None:
# 			continue
# 		get_fileAbs_Path()	

def open_file(url):
	L1 = os.listdir(url)
	L2 = os.path.abspath(url)
	L3=open_next_file(L1,L2)
	

def open_next_file(L1,L2):
	L3 = []
	for i in L1:
		j=os.path.splitext(i)		
		if j[1] == '':
			L3.append(os.path.join(L2,i))
		elif '1' in j[0]:  			
			print('文件的绝对路径：',os.path.join(L2,i)) 
	for x in L3:
		L4 = os.listdir(x)
		L5 = os.path.abspath(x)
		open_next_file(L4, L5)		

def main():
	url="G:/迅雷下载/"
	open_file(url)	

if __name__ == '__main__':
	main()	

# L = os.listdir('G:/平时')
# print('L:',L)
# for i in L:
# 	if len(os.listdir('G:/平时/'+i))>0:
# 		print(i)

# L1 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print("L1:",L1)
# L2 = os.path.abspath('.')
# print('L2:',L2)
# for i in L1:
# 	j=os.path.splitext(i)
# 	if 'n' in j[0]:
# 		print(os.path.join(L2,i))


# print(os.listdir('D:/'))