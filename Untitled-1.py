#!/usr/bin/python3
#-*- coding:utf-8 -*-
import  requests
from lxml import etree
import mysql.connector
import time
from bs4 import  BeautifulSoup
url = 'http://pc.youku.com/iku/2018worldCup?spm=a2hww.11359951.m_26658.5~1~3!6'
r =requests.get(url)
data = r.text
#ddata = data.replace("window.jQuery111205574701889781417_1528969194016 && jQuery111205574701889781417_1528969194016(","").replace(")","").replace(";","")
sdata = data.encode('latin1').decode('utf-8')
selector = etree.HTML(sdata)
surl = selector.xpath('//*//li[1]/a/@href')
rt = ['//www.youku.com/','https://','https://v.youku.com/v_show/id_XMzY1MjY1NDg5Ng==.html','https://v.youku.com/v_show/id_XMzY1MjY1NDg5Ng==.html','https://v.youku.com/v_show/id_XMzY1MjY1NDg5Ng==.html','https://v.youku.com/v_show/id_XMzY1MjY1NDg5Ng==.html','https://v.youku.com/v_show/id_XMzY1MjY1NDg5Ng==.html', '//www.youku.com/','https://v.youku.com/v_show/id_XMzY1MjY1NDg5Ng==.html','http://sc.youku.com/']
for urln in surl:
    for ur in rt:
        if ur in urln:
            pass
        else:
            rurl = "https:"+ urln

            try:
                r = requests.get(rurl)
                ddatas = r.text
                # print(ddatas)
                # print(ddatas.encode('latin1').decode('utf-8'))
                dart = []
                selector = etree.HTML(ddatas)
                cateory1 = selector.xpath('//div[@class="tvinfo"]/h2/a/@title')  #专辑名字
               
                cateory3 = selector.xpath('//*[@id="module_basic_dayu_sub"]//h2/a/text()') #KOL
                if cateory3 is  None:
                    cateory1 = selector.xpath('//div[@class="tvinfo"]/h2/a/@title')
                    cateory2 = selector.xpath('//*[@id="Drama"]/div[3]/h3') #相关视频
                    titles = selector.xpath('//*[@id="listitem_page1"]//a/div[2]/text()')
                    nums = selector.xpath('//*[@id="listitem_page1"]//a/div[3]/span/text()')
                    timelengths = selector.xpath('//*[@id="listitem_page1"]//span[2]/span/text()')
                ELSE:
                    cateory3 = selector.xpath('//div[@class="tvinfo"]/h2/a/@title')
                    cateory2 = selector.xpath('//*[@id="Drama"]/div[3]/h3') #相关视频
                    titles = selector.xpath('//*[@id="listitem_page1"]//a/div[2]/text()')
                    nums = selector.xpath('//*[@id="listitem_page1"]//a/div[3]/span/text()')
                    timelengths = selector.xpath('//*[@id="listitem_page1"]//span[2]/span/text()')


                


                


            except:
                pass
            for i in range(len(timelengths)):
                title = titles[i]  # 视频名字
                num = nums[i]  # 视频播放次数
                timelength = timelengths[i]  # 视频时长
                cateory = cateory
                dates = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                m = (repr(title), repr(num), repr(timelength), repr(dates),repr(cateory))
                # m = ("'" + title + "'","'" + num + "'","'" + timelength + "'","'" + dates + "'")
                dart.append(m)
            print(dart)
