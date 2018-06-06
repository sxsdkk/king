

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request,parse
import  re
from bs4 import BeautifulSoup
url = 'http://s.weibo.com/top/summary?cate=realtimehot'
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    html = f.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
m = soup.find_all('a')
print(m)
title_pattern = r"(?<=span>\n).*?(?=<em><em>)"  #标题正则
url_pattern = r'(?<=href=")https.*?(?=>\n<strong)' # url正则
nums_pattern = r'(?<=<em><em>).*?(?=<\/em><\/em>)' #热度正则
titles = re.finditer(title_pattern, str(m), re.MULTILINE)
urls = re.finditer(url_pattern, str(m), re.MULTILINE)
nums = re.finditer(nums_pattern, str(m), re.MULTILINE)
num = [num.group() for num  in nums]
title =  [title.group() for title  in titles]
url =  [url.group() for url  in urls]
# print(num)
for i in range(len(title)):
    print(parse.unquote(url[i])+":"+title[i]+":"+num[i])

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
请记住这里的代码是自动生成的，并不保证一定可以。如果你发现语法错误，你可以随意提交一个bug报告。
完整Python正则表达式参考，请访问： https://docs.python.org/3/library/re.html