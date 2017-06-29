#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 22:33:28
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$


import pickle
d= dict(name='caowei',age='26',score='80')
print(pickle.dumps(d))

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)