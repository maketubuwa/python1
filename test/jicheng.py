#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-02 19:35:51
# @Author  : mx (mengxiang@xiangcloud.com.cn)
# @Link    : http://www.xiangcloud.com.cn/
# @Version : $Id$

class Animal(object):
	"""docstring for Animal"""
	def __init__(self, leg,food):
		self.__leg = leg
		self.__food=food

	def get_leg(self):
		return self.__leg
	def get_food(self):
		return self.__food

	def set_leg(self,leg):
		self.__leg=leg

	def set_food(self,food):
		self.__food=food
	def run(self):
		print("Animal is running")
		
Animal1=Animal(3,'meat')		
Animal1.run()

class Dog(Animal):
	pass

dog=Dog(4,'meat')
dog.run()
