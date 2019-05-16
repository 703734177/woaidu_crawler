# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
import sys
sys.path.append(r'D:\work\woaidu_crawler\woaidu_crawler')
from items import WoaiduCrawlerItem


class WoaiduSpider(scrapy.Spider):
    name = 'woaidu'
    #allowed_domains = ['https://www.woaidu.org/sitemap_100.html']
    start_urls = ['https://www.woaidu.org/sitemap_1.html/']
    i = 27

    def parse_detail(self, response):
        woaidu_item = WoaiduCrawlerItem()

        sel = response.css('div.common-section-left.fl')

        woaidu_item['book_name'] = sel.xpath('.//div[1]/div[1]/h1/text()').extract_first()
        woaidu_item['author'] = sel.xpath('.//div[1]/div[1]/p[2]/text()').extract_first()[5:].strip()
        woaidu_item['book_description'] = sel.xpath('.//div[3]/p/text()').extract_first()									  
        woaidu_item['book_covor_image_url'] = sel.xpath('.//div[1]/a/img/@src').extract_first()

        download = []

        sel1 = response.css('div.common-section-left.fl > div:nth-child(9) > ul') 
        for x in sel1.xpath('.//li'):
            download_item = {}

            download_item['url'] = x.xpath('.//a[2]/@href').extract_first()
            download_item['update_time'] = x.xpath('.//a[1]/text()').extract_first()
            download_item['source_site'] = x.xpath('.//a[1]/span/text()').extract_first()[3:-1]

            download.append(download_item) 
        woaidu_item['book_download'] = download
        woaidu_item['original_url'] = response.url
        yield woaidu_item

    def parse(self, response):
    	self.i += 1
    	if self.i <=2:
    		next_url = 'https://www.woaidu.org/sitemap_' + str(self.i) +'.html'
    		yield scrapy.Request(url=next_url, callback=self.parse)

    	le = LinkExtractor(restrict_xpaths = '//div[@class="sousuolist huisebj"]/a')

    	for detail_url in le.extract_links(response):
    		yield scrapy.Request(url=detail_url.url, callback=self.parse_detail)
