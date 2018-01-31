#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import datetime
starttime = datetime.datetime.now()
kl ='http://i.feed.mix.sina.com.cn/api/news/get?' 
with open('d:/adh/wr.txt') as f:
    a = f.readlines()
    for i in range(len(a)):
        s = (str(a[i]).split("\t"))
        urll = str((s[2]).replace("https","http")).strip()
#         print(urll)
        payload = {'urls':urll,'fields':'title'}
        r = (requests.get(kl,params= payload ))
        print(r.url)
        data=r.text
        ddata=json.loads(data)
        for k in ddata['result']['data']:
#            print(urll+":"+ ddata['result']['data'][k]['title'])
            Minsd =  ddata['result']['data'][k]['title'] + "-->"+ urll+ "-->" + s[0] + "-->" + s[1]
            with open('d:/sn.txt','a') as f:
                try:
                    f.writelines(Minsd+"\n")
                except:
                    pass
# #long running
count = len(open("d:/sn.txt",'r').readlines())  
print(count)
endtime = datetime.datetime.now()
print(str((endtime - starttime).seconds) + "s")
