#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-08 16:46:18
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import threading

local_school=threading.local()
def process_student():
	std=local_school.student
	print('hello %s  in %s' % (std,threading.current_thread().name))

def process_thread(name):
	local_school.student=name
	process_student()

t1=threading.Thread(target=process_thread,args=('caowei',),name='thread-1')
t2=threading.Thread(target=process_thread,args=('caocao',),name='thread-2')
t1.start()
t2.start()
t1.join()
t2.join()