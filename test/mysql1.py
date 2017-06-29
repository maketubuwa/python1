#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-09 20:50:07
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import pymysql

conn=pymysql.connect(user='root',password='123456789',database='test1')
# cursor=conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'caowei'])
# print(cursor.rowcount)
# conn.commit()
# cursor.close()
cursor=conn.cursor()
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# conn.commit()
cursor.execute('select * from user ')
values=cursor.fetchall()
print(values)
cursor.close()
conn.close()