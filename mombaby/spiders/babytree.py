# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from datetime import datetime


from mombaby.items import QuestionItem

class BabytreeSpider(CrawlSpider):
    name = "babytree"
    allowed_domains = ["babytree.com"]
    start_urls = ['http://www.babytree.com/s.php?q=%s&c=&range=d' % keyword for keyword in ['开奶', '催奶', '催乳', '奶结', '追奶', '乳腺', '肿胀', '通乳', '通奶', '催奶', '回奶']]
    rules =[
        Rule(LinkExtractor(allow=('/ask/detail/'), restrict_xpaths=('//div[@class="search_col_2"]')), callback='parse_question'),
        # Rule(LinkExtractor(allow=('/community/.+\.html'), restrict_xpaths=('//div[@class="search_col_2"]')), callback='parse_community'),
        Rule(LinkExtractor(allow=('c=community'), restrict_xpaths=('//ul[@class="search_tab"]')))
        # Rule(LinkExtractor(allow=('pg=\\d+'), restrict_xpaths=('//div[@class="pagejump"]')))
    ]

    def parse_question(self, response):
        question = QuestionItem()
        question['question'] = response.css('h1::text').extract()[0]
        question['question_time'] = response.css('div.qa-contributor abbr::text').extract()[0]
        question['answers'] = '\n'.join(response.css('div.answer-text::text,ul.answer-comments li::text').extract())
        question['last_updated'] = datetime.now()
        question['url'] = response.url
        return question

    def parse_community(self, response):
        question = QuestionItem()
        question['question'] = response.css('h1::text').extract()[0].strip()
        # question['question_time'] = response.css('div.postTime::text').extract()[0]
        question['answers'] = '\n'.join(response.css('div.postContent').extract())
        question['last_updated'] = datetime.now()
        question['url'] = response.url
        return question
