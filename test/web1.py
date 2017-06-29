#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-11 20:51:00
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return [b'<h1>hello world</h1>']