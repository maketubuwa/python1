#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-15 15:42:53
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

from tkinter import *
import requests
from tkinter import messagebox
import re
from PIL import Image,ImageTk

def download():

	startUrl="http://www.uustv.com/"
	# name=entry.get()
	# if not name:
	# 	messagebox.showinfo('提示',"请输入名字！")
	# else:
	data={
		'word':'曹伟',
		'sizes':'60',
		'fonts':'bzcs.ttf',
		'fontcolor':'#0000000',
	}
	result=requests.post(startUrl,data=data)
	result.encoding='utf-8'
	print(result.text)
	req='<div class="tu">﻿<img src="(.*?).gif"/></div>'
	name=re.findall(req,result.text)[0]
	imgUrl=startUrl+name
	response=requests.get(imgUrl).content
	with open('{}.png'.format(name[5:]),'wb') as f:
		f.write(response)

download()
root=Tk()
root.title("签名设计")
root.geometry("600x300+500+300")
label=Label(root,text="签名",font=("华文行楷",20),fg='red')
label.grid()
root.mainloop()
# entry=Entry(root)
# entry.grid()
# t =Text(root,height=2)
# t.grid()
# button=Button(root,text="设计签名")
# button.grid()
# canvas=Canvas(root,bg="blue")
# canvas.grid()
# image_file=PhotoImage(download())
# image=canvas.create_image(10,10,anchor="nw",image=image_file)
# root.mainloop()