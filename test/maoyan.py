#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-04 18:29:59
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import requests
from requests.exceptions import RequestException
import re
from multiprocessing import Pool
import json
import pymysql


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?">(.*?)</i>.*?data-src="(.*?)".*?data-val.*?'
                         + '">(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for i in items:
        yield{
            'index': i[0],
            'image': i[1],
            'title': i[2],
            'star': i[3].strip()[3:],
            'time': i[4].strip()[5:],
            'score': i[5]+i[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
	for i in range(10):
		main(i*10)
   	#pool=Pool()
   	#pool.map(main,[i*10 for i in range(10)])