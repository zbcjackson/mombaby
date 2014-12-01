# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from subprocess import Popen, PIPE

def send():
  print "get email info..."
  msg = MIMEText('TEst')
  msg["From"] = 'zbcjackson@gmail.com'
  msg["To"] = 'zbcjackson@odd-e.com'
  msg["Subject"] = '[母婴问答]' + '\n求助'
  p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
  res = p.communicate(msg.as_string())
  print 'mail sended ...'

if __name__ == "__main__":
  send()