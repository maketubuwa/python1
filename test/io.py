#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 17:27:40
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $I

# from io import StringIO


# w=StringIO('fafa\nfafa\nacowei\n')
# while  True:
# 	s=w.readline()
# 	if s=='':
# 		break
# 	print(s.strip())	

# from io import BytesIO

# w= BytesIO()
# w.write('曹伟'.encode('utf-8'))
# print(w.getvalue())

from io import StringIO
f = StringIO('hello!\nHi!\nGoodBye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())