#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-14 13:48:46
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import numpy as np
from numpy import *
import matplotlib.pyplot as plt

dataSet =[[1,2],[3,4],[5,6],[7,8],[9,10]]
dataMat=mat(dataSet).T
plt.scatter(dataMat[0],dataMat[1],c = 'red',marker = 'o') #绘制数据散点图

#绘制直线图形
X = np.linspace(-2,2,100)      #产生直线数据
#建立线性方程
Y = 2.8*X+9

plt.plot(X,Y)                   #绘制直线图
plt.show()                      #显示绘制效果