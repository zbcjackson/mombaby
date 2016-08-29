# -*- coding: utf-8 -*-

import MySQLdb

def save():
    conn = MySQLdb.connect(user='ttq', passwd='ttq', db='mombaby', host='192.168.59.103', charset="utf8", use_unicode=True)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO questions(question, answers) VALUES (%s, %s)""", ("求开奶师", "电话号码13912348903"))
    conn.commit()

if __name__ == "__main__":
  save()