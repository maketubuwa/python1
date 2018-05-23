#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#画图
# from tkinter import *
#
# canvas=Canvas(width=800,height=600,bg='pink')
# canvas.pack(expand=YES, fill=BOTH)
# k=1
# j=1
# for i in range(0,26):
# 	canvas.create_oval(310-k,250-k,310+k,250+k,width=1)
# 	k+=j
# 	j+=0.3
# canvas.mainloop()


# a=1,2,3,4,7,85,23,412,6,34,2547,134
# l=list(a)
# for i in range(len(l)):
# 	if l[i]==max(l):
# 		l[0],l[i]=l[i],l[0]
# 	if l[i]==min(l):
# 		l[-1], l[i] = l[i], l[-1]
# print(l)
#
#
# b=l[-3:]
# c=l[:-3]
# print(b+c)

# def circle(n):
# 	a=[x for x in range(1,n+1)]
# 	b=True
# 	while b:
# 		for i,j,k in zip(a[::3],a[1::3],a[2::3]):
# 			a.append(i)
# 			a.append(j)
# 			a.remove(k)
# 			a.remove(i)
# 			a.remove(j)
# 			if len(a)==2:
# 				b=False
# 				a.remove(a[0])
# 			print(a)
# 	print(a)
# circle(34)

#输入一个奇数，看下能被几个9组成的数整除
# n=int(input('请输入一个奇数：'))
# i=1
# z='9'
# while True:
# 	if (int(z*i))%n==0:
# 		print(i)
# 		break
# 	else:i+=1


# filename=input('请输入文件名：')
#
# with open(filename,'w') as f:
# 	ch=input('请输入字符：')
# 	while ch!='#':
# 		f.write(ch.upper())
# 		ch=input("")

with open('test.txt','r') as f:
	ch=f.read()
with open('test1.txt','r') as f:
	ch1=f.read()
ch2=list(ch+ch1)
print(ch2)
ch2.sort()
print(ch2)
with open('test2.txt','w') as f:
	f.write(('').join(ch2))
