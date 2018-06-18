import requests
import json
kl ='http://i.feed.mix.sina.com.cn/api/news/get?'   
with open('D:/adh/sc.txt', 'r') as f:
     a =f.readlines()
urls = []
for u  in a:
    urls.append(u)
print(urls)
# print(type(urls))
for url in urls:
    print(url)
    print(url.strip())
    payload = {'urls': url.strip(),'fields':'title'}
    r = (requests.get(kl,params= payload ))
    data=r.text
    ddata=json.loads(data)
    for k in ddata['result']['data']:
        print(url+":"+ ddata['result']['data'][k]['title'])
        Minsd = url+":"+ ddata['result']['data'][k]['title']
        with open('d:/sn.txt','a')as f:
            f.writelines(Minsd)
          

