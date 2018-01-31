#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import datetime
starttime = datetime.datetime.now()
kl ='http://i.feed.mix.sina.com.cn/api/news/get?'   
with open('D:/adh/wr.txt', 'r+') as f:
     a =f.readlines()
urls = []
for u  in a:
    urls.append(u)
# print(urls)
# print(type(urls))
for url in urls:
#     print(url)
    urlt = url.strip()
#     print(type(urlt))
    urll = (str(urlt)).replace('https', 'http')
    print(urll)
    payload = {'urls':urll,'fields':'title'}
    r = (requests.get(kl,params= payload ))
    data=r.text
    ddata=json.loads(data)
    for k in ddata['result']['data']:
#         print(url+":"+ ddata['result']['data'][k]['title'])
        Minsd = url + "-->"+ ddata['result']['data'][k]['title']
        with open('d:/sn.txt','a') as f:
            f.writelines(Minsd)
#long running

endtime = datetime.datetime.now()
print(str((endtime - starttime).seconds) + "s")