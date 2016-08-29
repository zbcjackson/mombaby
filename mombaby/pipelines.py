# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.exporter import JsonItemExporter

from email.mime.text import MIMEText
from email.header import Header
from subprocess import Popen, PIPE
import MySQLdb

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

class EmailPipeline(object):
    def process_item(self, item, spider):
      print "get email info..."
      msg = MIMEText(item['question'] + '<br/>' + item['url'] + '<br/>' + item['answers'], 'html', 'utf-8')
      msg["From"] = 'zbcjackson@gmail.com'
      msg["To"] = 'zbcjackson@gmail.com;ace0918@126.com;qinwen.shi@gmail.com;tengzhenyu@gmail.com'
      msg["Subject"] = Header(u"[母婴问答]" + item['question'], 'utf-8')
      p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
      res = p.communicate(msg.as_string())
      print 'mail sended ...'

      return item

class MySQLPipeline(object):
  def __init__(self):
    self.conn = MySQLdb.connect(user='ttq', passwd='ttq', db='mombaby', host='192.168.59.103', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

  def process_item(self, item, spider):
    try:
      self.cursor.execute("""INSERT INTO questions(question, answers) VALUES (%s, %s)""", (item['question'], item['answers']))
      self.conn.commit()
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        return item

