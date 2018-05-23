#!/usr/bin/env python
# -*- coding: utf-8 -*-
#爬取豆瓣文章下的评论


import requests
from requests.exceptions import RequestException
import re
import json

def get_one_page(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern=re.compile('<h4>.*?href=.*?">(.*?)</a>.*?pubtime">(.*?)</span>.*?">(.*?)</p>',re.S)
	items=re.findall(pattern, html)
	for item in items:
		yield{
		'name':item[0],
		'time':item[1],
		'content':item[2]
		}


def write_in_file(content):
	with open('东邪西毒.txt','a',encoding='utf-8') as f:
		f.write(json.dumps(content,ensure_ascii=False)+'\n')
		f.close()



def main(start):
	url='https://www.douban.com/group/topic/1316973/?start='+str(start)
	html=get_one_page(url)
	for i in parse_one_page(html):
		write_in_file(i)

if __name__ == '__main__':
	for i in range(2):
		main(i*100)