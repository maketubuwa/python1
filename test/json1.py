#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 22:46:21
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$


import json

import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'

f = open('dump1.txt', 'wb')
pickle.dump(d, f)
f.close()
