# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class WoaiduCrawlerPipeline(object):
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'scrapy_default')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'root')

        self.db_conn = MySQLdb.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
            item['book_name'],
            item['author'],
            item['book_description'],
            item['book_covor_image_url'],
            #item['book_download'],
            item['original_url'],
    )

        sql = 'INSERT INTO books (book_name, author, book_description, book_covor_image_url, original_url) VALUES(%s, %s, %s, %s, %s)'
        self.db_cur.execute(sql, values)

