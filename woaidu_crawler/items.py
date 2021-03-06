# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WoaiduCrawlerItem(scrapy.Item):
    mongodb_id = scrapy.Field()
    book_name = scrapy.Field()
    alias_name = scrapy.Field()
    author = scrapy.Field()
    book_description = scrapy.Field()
    book_covor_image_path = scrapy.Field()
    book_covor_image_url = scrapy.Field()
    book_download = scrapy.Field()
    book_file_url = scrapy.Field()
    book_file = scrapy.Field()#only use for save tho single mongodb
    book_file_id = scrapy.Field()#only use for save to shard mongodb
    original_url = scrapy.Field()

