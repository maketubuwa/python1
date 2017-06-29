#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-09 12:05:30
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import time,random,queue
from multiprocessing.managers import BaseManager


task_queue=queue.Queue()
result_queue=queue.Queue()

class QueueManager(BaseManager):
	pass
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue
def test():
	QueueManager.register('get_task_queue',callable=return_task_queue)
	QueueManager.register('get_result_queue',callable=return_result_queue)

	manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
	manager.start()
	task=manager.get_task_queue()
	result=manager.get_result_queue()

	for i in range(10):
		n = random.randint(0,1000)
		print('put task %d' % n)
		task.put(n)

	print('try get result...')
	for i in range(10):
		r=result.get(timeout=10)
		print('result %s',r)

	manager.shutdown()
	print('master exit.')		
if __name__ == '__main__':
	test()