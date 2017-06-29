#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-11 20:53:18
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

from web1 import application
from wsgiref.simple_server import make_server


httpd=make_server('localhost', 8000, application)
print('Serving HTTP on port 8000..')
httpd.serve_forever()