#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-08 20:21:38
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

from tkinter import *

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()		
app=Application()
app.master.title('hello world')
app.mainloop()

