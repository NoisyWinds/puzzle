# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class SaveImagesPipeline(ImagesPipeline): 
	headers = {
		"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
		"Accept-Encoding":" gzip, deflate",
		"Accept-Language":" en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
		"Cache-Control":" no-cache",
		"Host":" img.gov.com.de",
		"Pragma":" no-cache",
		"Proxy-Connection":" keep-alive",
		"User-Agent":" Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"
	}
	def get_media_requests(self, item, info):
		self.headers['Referer'] = item['url']
		for image_url in item['images']:
			yield scrapy.Request(image_url,headers = self.headers)