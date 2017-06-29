#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-08 16:01:03
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import time,threading

def loop():
	print('current_thread:%s is running .' % threading.current_thread().name)
	n=0
	while n<5:
		n = n + 1
		print('current_thread:%s is running --- %s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('current_thread:%s is ended'% (threading.current_thread().name))

print('current_thread:%s is running .' % threading.current_thread().name)
l=threading.Thread(target=loop,name='LoopThread')
l.start()
l.join()
print('current_thread:%s is ended .' % threading.current_thread().name)

