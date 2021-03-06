# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.contrib.loader.processor import Join

def encoding(value):
  return value.encode('utf-8').decode("unicode_escape")

def join_multiline(value):
  return '\n'.join(value)

class QuestionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question = scrapy.Field()
    question_time = scrapy.Field()
    answers = scrapy.Field()
    last_updated = scrapy.Field()
    url = scrapy.Field()
