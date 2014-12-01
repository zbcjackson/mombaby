# -*- coding: utf-8 -*-

# Scrapy settings for mombaby project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mombaby'

SPIDER_MODULES = ['mombaby.spiders']
NEWSPIDER_MODULE = 'mombaby.spiders'

ITEM_PIPELINES = {
    'mombaby.pipelines.JsonExportPipeline': 300,
    'mombaby.pipelines.EmailPipeline': 800
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mombaby (+http://www.yourdomain.com)'
