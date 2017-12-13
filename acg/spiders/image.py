import scrapy
import urllib.request,urllib.parse
import numpy as np
import cv2

class acgimages(scrapy.Spider):
	"""docstring for acgimages"""
	name = 'images'
	start_urls = [
		"http://m.52dmtp.com/tupiandaquan/index_2.html"
	]
	count = 1
	page = 2
	def parse(self,response):
		def imageSave(item,path):
			try:
				maxsize = 512
				res = urllib.request.urlopen(item).read()
				print(res)
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
			except:
				print('image save error')

		image_url = response.xpath("//div[@class='grid-wrap']//img/@src").extract()
		for item in image_url:
			item = item.split('?')[0]
			item = urllib.parse.quote(item,safe='/:?=.')
			if 'jpg' in item:
				self.count = self.count + 1
				path = 'img/'+ str(self.count) + ".jpg"
				imageSave(item,path)
			if 'png' in item:
				self.count = self.count + 1
				path = 'img/'+ str(self.count) + ".png"
				imageSave(item,path)
		if self.page < 1180:
			self.page = self.page + 1
			next_url = "http://m.52dmtp.com/tupiandaquan/index_%d.html"%self.page
			yield scrapy.Request(next_url,callback = self.parse)


	
