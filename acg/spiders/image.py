#coding=utf-8
import scrapy
import urllib.request,urllib.parse
import numpy as np
import cv2
import os

class acgimages(scrapy.Spider):
	"""docstring for acgimages"""
	name = 'images'
	start_urls = [
		"http://www.acg.fi/anime/page/1"
	]
	count = 0
	page = 1



	def parse3(self,response):

		image_url = response.xpath("//article[@class='article-content']//img/@src").extract()
		print(image_url)
		print("一共找到图片%d" % len(image_url))

		for item in image_url:
			#item = item.split('!')[0]
			item = urllib.parse.quote(item,safe='/:?=.')
			if 'jpg' in item:
				self.count = self.count + 1
				path = os.path.dirname(os.path.abspath(__file__))+ '/../img/' + str(self.count) + ".jpg"
				self.imageSave(item,path)
			if 'png' in item:
				self.count = self.count + 1
				path = os.path.dirname(os.path.abspath(__file__))+ '/../img/' + str(self.count) + ".png"
				self.imageSave(item,path)


	def parse2(self,response):

		pages_url = response.xpath("//div[@class='fenye']//a/@href").extract()
		num=1
		if len(pages_url)==0:
			pages = response.xpath("//h1[@class='article-title']//a/@href").extract()
			yield scrapy.Request(pages[0], callback=self.parse3)
		else:
			for pages in pages_url[:len(pages_url)-1]:
				pages=pages[:len(pages)-1]+str(num)
				num=num+1
				yield scrapy.Request(pages,callback=self.parse3)


	def parse(self,response):

		pages_url = response.xpath("//div[@class='card-item']//h3//a/@href").extract()
		print("一共找到二级页面%d" % len(pages_url))
		for pages in pages_url:
			yield scrapy.Request(pages, callback=self.parse2)
		if self.page < 1180:
			self.page = self.page + 1
		next_url = "http://www.acg.fi/anime/page/%d" % self.page
		yield scrapy.Request(next_url,callback = self.parse)

	def imageSave(self,item,path):
		maxsize = 512
		req = urllib.request.Request(item)
		req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
		req.add_header("GET",item)
		req.add_header("Host","img.gov.com.de")
		req.add_header("Referer",item)
		res = urllib.request.urlopen(req).read()
		image = np.asarray(bytearray(res),dtype="uint8")
		image = cv2.imdecode(image,cv2.IMREAD_COLOR)
		height,width = image.shape[:2]
		if height > width:
			scalefactor = (maxsize*1.0) / width
			res = cv2.resize(image,(int(width * scalefactor),(int(height * scalefactor))),interpolation = cv2.INTER_CUBIC)
			cutImage = res[0:maxsize,0:maxsize]
		if width >= height:
			scalefactor = (maxsize*1.0) / height
			res = cv2.resize(image,(int(width * scalefactor), int(height*scalefactor)), interpolation = cv2.INTER_CUBIC)
			center_x = int(round(width*scalefactor*0.5))
			cutImage = res[0:maxsize,int(center_x - maxsize/2):int(center_x + maxsize/2)]
		cv2.imwrite(path,cutImage)
		print('image is save in ' + path)

	print("pageend,total:%d" % count)

