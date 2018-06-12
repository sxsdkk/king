#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector
import pandas as pd
# change root password to yours:
conn = mysql.connector.connect(user='root', password='123123', database='sd')

# cursor = conn.cursor()
# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
# print('rowcount =', cursor.rowcount)
# 提交事务:
# conn.commit()
# cursor.close()
df = pd.read_csv("d:/2.txt", low_memory=False,usecols=['hh_ua_raw'], header=0)
with open('d:/12.txt','w')  as f:
    f.write(str(df))

#多行插入
# cursor = conn.cursor()
# data = [
#   ('Jane', 12),
#   ('Joe', 25),
#   ('John', 66),
# ]
# stmt = "INSERT INTO user (id,name) VALUES (%s, %s)"
# cursor.executemany(stmt, data)
# print('rowcount =', cursor.rowcount)
#
# conn.commit()
# cursor.close()
# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# # 关闭Cursor和Connection:
# cursor.close()
# conn.close()