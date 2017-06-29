import scrapy
from scrapy.http import Request
from qiubai.items import QiubaiItem

class  QiubaiSpider(scrapy.Spider):
	name='qiubai'

	start_urls=("https://www.qiushibaike.com/")

	def parse(self,response):
		item=QiubaiItem()
		for mb in response.xpath('//div[@class="article block untagged mb15"]'):
			author = mb.xpath('div[@class="author clearfix"]/a/h2/text()').extract()[0]
			author_logo = mb.xpath('div[@class="author clearfix"]/a/img/@src').extract()[0]
			content = mb.xpath('div[@class="content"]/text()').extract()[0]
			thumb = ""
			try:
				thumb = mb.xpath('div[@class="thumb"]/a/img/@src').extract()[0]
			except:
				pass
			item['author'] = author.encode('utf-8')     # 转码
			item['author_logo'] = author_logo
			item['content'] = content.encode('utf-8')
			item['thumb'] = thumb
			item['vote'] = vote
			item['comments'] = comments.encode('utf-8')
			yield item