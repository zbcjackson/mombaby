# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def encoding(value):
  return value.encode('utf-8').decode("unicode_escape")


class QuestionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question = scrapy.Field()
    question_time = scrapy.Field()
    last_updated = scrapy.Field()
    url = scrapy.Field()
