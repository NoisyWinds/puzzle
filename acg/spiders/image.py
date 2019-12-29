#coding=utf-8
#update at 2019-12-29
from http.client import IncompleteRead
from acg.items import ImageItem
import scrapy
import numpy as np
import os

class acgimages(scrapy.Spider):
	"""docstring for acgimages"""
	name = 'images'
	start_urls = [
		"http://acg.fi/anime/page/1"
	]
	page = 1
	count = 0
	MAX_CATCH_PAGES = 1000
	item = ImageItem()
	def parse(self,response):
		next_page = response.xpath('//div[@class="site-content"]//a/@href').re(r'https://acg.fi/anime/([0-9]+)\.htm')
		used = set()
		for page in next_page:
			if page not in used:
				used.add(page)
		print('find %d secound pages' % len(used))
		for number in used:
			url = "https://acg.fi/anime/%s.htm" % number
			self.item['url'] = url
			yield scrapy.Request(url, callback = self.post_page)

		if self.page < self.MAX_CATCH_PAGES:
			self.page = self.page + 1
		next_url = "https://acg.fi/anime/page/%d" % self.page
		yield scrapy.Request(next_url, callback = self.parse)

	def post_page(self,response):
		images_url = response.xpath("//div[@id='entry-content']//img/@src").extract()
		print('find %d images' % len(images_url))
		self.item['images'] = images_url
		return self.item
