import pandas as pd 
from datetime import datetime 
import mysql.connector

conn = mysql.connector.connect(user='root', password='261190', database='world')
cursor = conn.cursor()
class Library(object):
    def __init__(self):
        
        s = [datetime.strftime(x,'%Y%m%d') for x in list(pd.date_range(start='20170301',end='20170307'))]
        v= [value for value in s]
        k = ["title" + repr(key) for key in range(1,len(s))]
        self.books = dict(list(zip(k,v)))

    def __getitem__(self, i):
        return self.books[i]

    def __iter__(self):
        # 方法1 使用生成器
        for titles in self.books:
            m =  cursor.execute ("SELECT COUNT(DISTINCT t.ustat) FROM  (SELECT ustat FROM usty WHERE dt = %s AND req LIKE 'http://sdd1')t INNER JOIN (SELECT ustat FROM usty WHERE dt != %s AND req LIKE 'http://sdd1')t1  ON t.ustat != t1.ustat",(self.books[titles],self.books[titles]))
            yield  (self.books[titles] + "的新增是:" ,cursor.fetchall())
           

    
library = Library()
# 3.迭代器
for book in library:
    print(book)