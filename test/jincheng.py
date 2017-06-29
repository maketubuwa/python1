#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-08 12:33:09
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

# 多进程
# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
# 	print('run task %s (%s)...' % (name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random()*3)
# 	end=time.time()
# 	print('task %s runs %0.2f seconds .' % (name,(end-start)))

# if __name__ == '__main__':
# 		print('parent process %s.' % os.getpid())
# 		p=Pool(4)
# 		for i in range(5):
# 			p.apply_async(long_time_task,args=(i,))
# 		print('waiting for all subprocesses done...')
# 		p.close()
# 		p.join()
# 		print('all subprocesses done.')	



#单进程
# import os
# from multiprocessing import Process
# def run_proc(name):
# 	print(r'run child process %s (%s)...' % (name,os.getpid()))

# if __name__ == '__main__':
# 	print(r'parent process %s.' % os.getpid())
# 	p=Process(target=run_proc,args=('test',))
# 	print(r'child process will start.')
# 	p.start()
# 	p.join()
# 	print(r'child process end.')


# 子进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)