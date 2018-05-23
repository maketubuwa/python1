#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#爬取学校排名
import time
import requests
from bs4 import BeautifulSoup
import bs4


#获取网页页面信息
def getHtmlText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print("出现异常！")
#解析网页信息
def	fillUnivList(ulist,html):
	soup=BeautifulSoup(html,"html.parser")
	for tr in soup.find("tbody").children:
		if isinstance(tr,bs4.element.Tag):
			tds=tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUnivList(ulist,num):
	print("{0:^10}\t{1:{3}^10}\t{2:^10}".format("排名","学校名称","总分",chr(12288)))
	for i in range(num):
		u=ulist[i]
		print("{0:^10}\t{1:{3}^10}\t{2:^10}".format(u[0],u[1],u[2],chr(12288)))




def main():
	uinfo=[]
	url="http://www.zuihaodaxue.cn/keyanguimopaiming2018.html"
	html=getHtmlText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,20)
main()