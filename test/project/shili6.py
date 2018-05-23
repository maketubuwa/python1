#!/usr/bin/env python
# -*- coding: utf-8 -*-

#爬取淘宝相关相关信息

import requests
import re

#爬取页面
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print(" ")


#分析页面，并取出相关内容
def parsePage(infoList,html):
	try:
		tlt=re.findall(r'\"raw_title\":\".*?\"',html)
		plt=re.findall(r'\"view_price\":\"[\d\.]*\"',html)
		for i in range(len(tlt)):
			title=eval(tlt[i].split(':')[1])
			price = eval(plt[i].split(':')[1])
			infoList.append([title,price])
	except:
		print(' ')

#将获取的内容写入txt
def getInfo(infoList):
	with open('taobao.txt','w+',encoding='utf-8') as f:
		tplt = "{:4}\t{:8}\t{:16}"
		f.write(tplt.format("序号", "价格", "商品名称")+'\n')
		count=0
		for i in infoList:
			count+=1
			f.write(tplt.format(count, i[1],i[0])+'\n')

def main():
	goods="詹姆斯"
	start_url="https://s.taobao.com/search?q="+goods
	deepth=3
	infoList=[]
	for i in range(deepth):
		try:
			url=start_url+"&s="+str(44*i)
			html=getHTMLText(url)
			parsePage(infoList,html)
		except:
			continue
	getInfo(infoList)

main()