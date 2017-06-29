#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 22:05:01
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import os

def find_files(dir=os.curdir,key='python'):
    adrs=[]
    for root,folders,files in os.walk(dir):
        for file in files:
            tfile=file.partition('.')[0]
            if key in tfile:
                adrs.append(os.path.relpath(os.path.join(root,file),dir))
    print('Current direction:%s' % os.path.abspath(dir))
    print('Find Files: %s'% adrs)

find_files(key='p')
