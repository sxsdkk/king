#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  requests
url = 'http://sports.sina.cn'
r = requests.get(url)
print(r.encoding)
data = r.text
print(data.encode('latin1').decode('utf-8'))
''''微博有可能是GBK''''
