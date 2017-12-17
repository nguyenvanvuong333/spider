import time
import requests
from  lxml import html
class CommicCrawler:
	def __init__(self, urls, xpath_name, xpath_last_chap, xpath_published_date):
		self.urls = urls		
		self.xpath_name = xpath_name
		self.xpath_last_chap=xpath_last_chap
		self.xpath_published_date = xpath_published_date
		self.name = "xpath_name"
		self.last_chap="xpath_last_chap"
		self.published_date = "xpath_published_date"

	def crawl(self):
		for url in self.urls:
			page = requests.get(url)
			tree = html.fromstring(page.text)
			self.name = tree.xpath(self.xpath_name)[0].split('–')[0]
			self.last_chap = tree.xpath(self.xpath_last_chap)[0].split(' ')
			self.published_date = tree.xpath(self.xpath_published_date)[0]
			#checking new chap
			if time.strptime(time.strftime("%d-%m-%Y"),"%d-%m-%Y") <= time.strptime(self.published_date,"%d-%m-%Y"):
				print('New chap/ '+' name: '+self.name+'\n');
			print('name: '+self.name+'; last_chap: '+self.last_chap+'; published_date: ' + self.published_date+'\n')

print(time.strftime("%d-%m-%Y"))
xpath_name = '//div[@class= "chapter-list"]//div[@class="row"]/span/a/text()'
xpath_last_chap = '//div[@class= "chapter-list"]//div[@class="row"]/span/a/text()'
xpath_published_date = '//div[@class= "chapter-list"]//div[@class="row"]/span/text()'
urls = ['http://mangak.info/kingdom-vuong-gia-thien-ha/',
	'http://mangak.info/attack-on-titan-2r/',
	'http://mangak.info/one-piece-dao-hai-tac-r/',]
crawler = CommicCrawler(urls, xpath_name, xpath_last_chap, xpath_published_date)
crawler.crawl()
