# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.exporter import JsonItemExporter

class JsonExportPipeline(object):
    def __init__(self):
      self.file = open('babytree.json', 'w+b')

    def open_spider(self, spider):
      self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
      self.exporter.start_exporting();

    def close_spider(self, spider):
      self.exporter.finish_exporting()
      self.file.close()

    def process_item(self, item, spider):
      self.exporter.export_item(item)
      return item
