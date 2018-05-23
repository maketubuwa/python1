#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#计算输入的日期是每年的第几天
# year=int(input('year:\n'))
# month=int(input('month:\n'))
# day=int(input('day:\n'))
#
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
#
# if 0<month <=12:
# 	sum=months[month-1]
# else:
# 	print('data error')
#
# sum+=day
# leap=0
# if (year%400==0) or ((year%100!=0) and (year%4==0)):
# 	leap=1
# if leap==1 and month>2:
# 	sum+=1
#
# print('这是一年的第{}天'.format(sum))

#数字排序
# l=[]
# for i in range(3):
# 	i=input('请输入第{}个数字:'.format(i+1))
# 	l.append(i)
# l.sort()
# print(l)

#斐波那契数列
# def fib(n):
# 	a,b=1,1
# 	for i in range(n-1):
# 		a,b=b,a+b
# 	return a
# print(fib(10))

# def fib(n):
# 	if n==1 or n==2:
# 		return 1
# 	return fib(n-1)+fib(n-2)
# print(fib(10))

# a=[1,2,3,45,6,7,8,9]
# c=a.copy()
# b=a[:]
# print(id(a),id(c),id(b))

#时间
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

#判断素数
# def func(a,b):
# 	l=[x for x in range(a,b+1)]
# 	print(l)
# 	for i in range(a,b+1):
# 		for j in range(2,i):
# 			if i%j==0:
# 				l.remove(i)
# 				break
# 	return l
# print(func(101,200))

#统计字符和数字
# import string
# s=input('请输入字符串：\n')
# letters=0
# space=0
# digit=0
# others=0
# i=0
# while i < len(s):
# 	c = s[i]
# 	i+=1
# 	if c.isalpha():
# 		letters+=1
# 	elif c.isdigit():
# 		digit+=1
# 	elif c.isspace():
# 		space+=1
# 	else:
# 		others+=1
# print('char={},space={},digit={},others={}'.format(letters,space,digit,others))

# from functools import reduce
# x1=1
# for day in range(0,9):
# 	x2=(x1+1)*2
# 	x1=x2
# print(x1)

# l1=['c','b','a']
# l2=['x','y','z']
# for i in l1:
# 	for j in l2:
# 		if (i=='a' and j=='x') or (i=='c' and j=='x') or (i=='c' and j=='z'):
# 			continue
# 		else:
# 			l2.remove(j)
# 			print(i ,"----",j)

#打印图形
# a=7
# for i in [x for x in range(a+1)][1::2]:
# 	print(' '*(int((a-i)/2)),'*'*i)
#
# for i in [x for x in range(a+1)][-3::-2]:
# 	print(' '*(int((a-i)/2)),'*'*i)
#
# n = int(input("请输入行数 n："))
# for i in range(0,n):
# 	a = abs(i - int(n/2))
# 	b = n - abs(i - int(n/2))
# 	print(" "*a+"*"*(b-a))

#求1-20阶乘的和
# from functools import reduce
# l=0
# for n in range(2,22):
# 	l+=reduce(lambda x,y:x*y,range(1,n))
# print(l)

#求数字的阶乘（递归方法）
# def fact(j):
# 	sum=0
# 	if j==0:
# 		sum=1
# 	else:
# 		sum=j*fact(j-1)
# 	return sum
#
# print(fact(6))

#倒序输出字符（递归）
# def output(s,l):
# 	if l==0:
# 		return
# 	print(s[l-1],end=' ')
# 	output(s,l-1)
#
# s=input('请输入字符：')
# l=len(s)
# output(s,l)

#倒序输出数字
# s=str(input('请输入数字：'))
# print('数字长度为{}'.format(len(s)))
# print(s[::-1])


# l=[1,2,3,4,65,77,22]
# l1=(',').join(str(n) for n in l)
# print(l1)

#输出颜色
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print (bcolors.OKBLUE + "警告的颜色字体?")

#按原规则插入数字
# L=[1,2,3,4,5,8,9]
# # L.insert(5,7)
# # print(L)
# print(L)
# n=int(input('请输入数字：'))
# L.append(n)
# for i in range(len(L)):
# 	if n>= L[i-1] and n<L[i] :
# 		for x in range(i+1,len(L))[::-1]:
# 			L[x],L[x-1]=L[x-1],L[x]
# 			print(i,x,L)
# 		break
# print(L)

# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

# X = [	[12,7,3],
#     	[4 ,5,6],
#     	[7 ,8,9]]
#
# Y = [	[5,8,1],
#     	[6,7,3],
#     	[4,5,9]]
# Z=[[],[],[]]
# for i in range(3):
# 	for j in range(3):
# 		Z[i].append(X[i][j]+Y[i][j])
# print(Z)