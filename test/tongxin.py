#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-08 15:28:23
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

from multiprocessing import Process, Queue
import os
import time
import random


def write(q):
    print('Process to write : %s ' % os.getpid())
    for value in ['A', "B", 'C']:
        print('put %s to Queue:' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read : %s ' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

def main():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    print(pw, pr)
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
if __name__ == '__main__':
	main()