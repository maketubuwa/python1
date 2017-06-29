#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 13:46:35
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import unittest
from ceshi4 import Dict

class TsetDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d,dict))
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')
	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']
	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value=d.empty

if __name__ == '__main__':
	unittest.main()
