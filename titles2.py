import requests
import json
kl ='http://interface.sina.cn/fetch_data.d.json?urlMatch=sina.cn&fl=url,title&solr=(editorGroupID:yd%20OR%20editorGroupID:top%20OR%20editorGroupID:sports%20)&thumb=0'
with open('E:/adh/sc.txt', 'r') as f:
     a =f.readlines()
url = []
for u  in a:
    url.append(u)
# print(url)
# print(type(urls))
for urls in url:
    # print(urls)
    # print(urls.strip())
    payload = {'url': urls.strip()}
    r = (requests.get(kl,params= payload ))
    # print(r.url)
    data=r.text
    ddata=json.loads(data)
    st = urls+":"+repr(ddata['data']['title'])
    print(st)
    with open('e:/sn.txt','a')as f:
        f.writelines(st)

