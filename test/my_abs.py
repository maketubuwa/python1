Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=100
>>> if a >= 0:
	print(a)
	else:
		
SyntaxError: invalid syntax
>>> 
 RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python36/if.py 
100
>>> n= 123
>>> f= 456.789
>>> s1='hello world'
>>> s2='hello \'Adam\''
>>> s3=r'hello "Bart"'
>>> s4=r'''hello'''
>>> s5=r""""""
>>> n
123
>>> f
456.789
>>> s1
'hello world'
>>> s2
"hello 'Adam'"
>>> 
>>> s3
'hello "Bart"'
>>> s4
'hello'
>>> print(n)
123
>>> print(f)
456.789
>>> print(s1)
hello world
>>> print(s2)
hello 'Adam'
>>> print(s3)
hello "Bart"
>>> print(s4)
hello
>>> ord('a')
97
>>> ord('A')
65
>>> ord('国')
22269
>>> chr(66)
'B'
>>> 'hello,%s' % 'world'
'hello,world'
>>> 'hi,%s,you have $%d' % ('micheal','10000')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    'hi,%s,you have $%d' % ('micheal','10000')
TypeError: %d format: a number is required, not str
>>> 'hi,%s,you have $%d' % ('micheal',10000)
'hi,micheal,you have $10000'
>>> '%2d-%02d' % (3,1)
' 3-01'
>>> '%.3f' % 3.1415927
'3.142'
>>> classmates = ['micheal','bob','tom']
>>> classmates
['micheal', 'bob', 'tom']
>>> len(classmates)
3
>>> list(classmates)
['micheal', 'bob', 'tom']
>>> print(list(classmates))
['micheal', 'bob', 'tom']
>>> for i in classmates:
	print(i)

	
micheal
bob
tom
>>> classmates[-1]
'tom'
>>> classmates.append('jim')
>>> classm
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    classm
NameError: name 'classm' is not defined
>>> classmates
['micheal', 'bob', 'tom', 'jim']
>>> classmates.pop()
'jim'
>>> classmates
['micheal', 'bob', 'tom']
>>> classmates.insert(1,'lily')
>>> classmates
['micheal', 'lily', 'bob', 'tom']
>>> age = 20
>>> if age >= 18:
	print('you age is ', age)
	print('adult')

	
you age is  20
adult
>>> L = ['lily','lucy','tom']
>>> for i in L:
	print('hello,' i)
	
SyntaxError: invalid syntax
>>> for i in L:
	print('hello,' + i)

	
hello,lily
hello,lucy
hello,tom
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['micheal']
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    d['micheal']
KeyError: 'micheal'
>>> d['Michael']
95
>>> 'Michael' in d
True
>>> d['kyean']=99
>>> d['kyean']
99
>>> d.get('Thomas')
>>> d.get('Thomas',-1)
-1
>>> abs(100)
100
>>> abs(-12)
12
>>> max(1,2,-3,9)
9
>>> min(1,-2,8,9,-8)
-8
>>> n1=255
>>> n2
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    n2
NameError: name 'n2' is not defined
>>> n1= 255
>>> n2=1000
>>> print(hex(n1))
0xff
>>> print(hex(n2))
0x3e8
>>> print('n1转换成十六进制的字符串为：%s\nn2转换成十六进制的字符串为：%s' % (hex(n1),hex(n2)))
n1转换成十六进制的字符串为：0xff
n2转换成十六进制的字符串为：0x3e8
>>> print(type(hex(n1)))
<class 'str'>
>>> 
========================= RESTART: D:/python/定义函数.py =========================
请输入数字：2
>>> 
========================= RESTART: D:/python/定义函数.py =========================
请输入数字：-3
>>> 
========================= RESTART: D:/python/定义函数.py =========================
请输入数字：-2
-2
>>> def my_abs(x):
	if x>=0:
		return x
	else:
		return -x

	
>>> my_abs(-3)
3
>>> 
========================= RESTART: D:\python\定义函数.py =========================
请输入数字：9
>>> 
