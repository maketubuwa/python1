#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-09 21:17:13
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class User(Base):
	__tablename__='user'
	id=Column(String(20),primary_key=True)
	name=Column(String(20))

#创建数据库链接
engine = create_engine('mysql+pymysql://root:123456789@localhost:3306/test1')
DBSession=sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()	
user=session.query(User).filter(User.id==2).one()
print('type:',type(user))
print('name:',user.name)
session.close()