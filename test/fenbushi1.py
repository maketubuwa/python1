#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-09 12:20:23
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import sys,time,random,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr='127.0.0.1'
print('connect to server %s' % server_addr)	
m=QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()
task=m.get_task_queue()
result=m.get_result_queue()
for i in range(10):
	try:
		n=task.get(timeout=1)
		print('run task %s %s' % (n,n))
		r='%d * %d = %d' % (n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.empty:
		print('task queue is empty')
print('work exit')			
		