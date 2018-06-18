#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from datetime import datetime 
import mysql.connector


conn = mysql.connector.connect(user='root', password='261190', database='world')
cursor = conn.cursor()
class Library(object):
    def __init__(self):

        s = [datetime.strftime(x,'%Y%m%d') for x in list(pd.date_range(start='20170101',end='20170417'))]
        v= [value for value in s]
        k = ["title" + repr(key) for key in range(1,len(s))]
        self.books = dict(list(zip(k,v)))

       

    def __getitem__(self, i):
        return self.books[i]

    def __iter__(self):
        # 方法1 使用生成器
        for titles in self.books:
            m =  cursor.execute ('select COUNT(DISTINCT uid) from uid  where dt>=%s and dt <= %s',('20170101',self.books[titles]))
            yield cursor.fetchall()
           

            # 方法2 使用迭代器


# return self.books.itervalues()

library = Library()
# 3.迭代器
for book in library:
    print(book)
# import datetime
# import mysql.connector
# conn = mysql.connector.connect(user='root', password='261190', database='world')
# cursor = conn.cursor()
# date1 = '20170401'
# cursor.execute ('select dt,COUNT(DISTINCT uid) from uid  where dt = %s',(date1,))
# values = cursor.fetchall()
# print(values)
# # for m in values:
#     print(m)
# for (uid, dt) in cursor:
#   print(uid, dt)
#
# for (dt,uid) in cursor:
#     print(dt)

cursor.close()
conn.close()

