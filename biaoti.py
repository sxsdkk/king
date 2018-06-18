#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
starttime = datetime.datetime.now()
import requests
import json
kl ='http://interface.sina.cn/fetch_data.d.json?urlMatch=sina.cn&fl=url,title&solr=(editorGroupID:yd%20OR%20editorGroupID:top%20OR%20editorGroupID:sports%20)&thumb=0'
with open('d:/adh/wr.txt') as f:
    a = f.readlines()
    for i in range(len(a)):
        s = (str(a[i]).split("\t"))
        # print(s[0])
        urll = str((s[0]).replace("https","http")).strip()
        payload = {'url':urll}
        r = (requests.get(kl,params= payload ))
        data=r.text
        ddata=json.loads(data)
        Minsd =  ddata['data']['title'] + "-->"+ urll+ "-->" #+ s[0] + "-->" + s[1]
        with open('d:/sn.txt','a') as f:
            try:
                f.writelines(Minsd+"\n")
            except:
                pass
#成功写入多少行
count = len(open("d:/sn.txt",'r').readlines())
print(count)
endtime = datetime.datetime.now()
print(str((endtime - starttime).seconds) + "用时s")