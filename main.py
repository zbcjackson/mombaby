from twisted.internet import reactor
from twisted.internet import task
from scrapy.crawler import Crawler
from scrapy import log, signals
from mombaby.spiders.babytree import BabytreeSpider
from scrapy.utils.project import get_project_settings

def crawl():
  spider = BabytreeSpider()
  settings = get_project_settings()
  crawler = Crawler(settings)
  # crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
  crawler.configure()
  crawler.crawl(spider)
  crawler.start()

l = task.LoopingCall(crawl)
l.start(3600) # call every hour

log.start()
reactor.run() # the script will block here until the spider_closed signal was sent
