# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from datetime import datetime

from mombaby.items import QuestionItem

class BabytreeSpider(CrawlSpider):
    name = "babytree"
    allowed_domains = ["babytree.com"]
    start_urls = (
        'http://www.babytree.com/s.php?q=%E5%BC%80%E5%A5%B6&c=',
    )
    rules =[
        Rule(LinkExtractor(allow=('/ask/detail/')), callback='parse_question'),
        # Rule(LinkExtractor(allow=('pg=\\d+')))
    ]

    def parse_question(self, response):
        question = QuestionItem()
        question['question'] = response.css('h1::text').extract()[0]
        question['question_time'] = response.css('div.qa-contributor abbr::text').extract()[0]
        question['last_updated'] = datetime.now()
        question['url'] = response.url
        return question
