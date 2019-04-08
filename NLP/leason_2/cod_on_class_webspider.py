#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import re
url = 'https://movie.douban.com/'
response=requests.get(url)
image_pattern=re.compile('https://img3.doubanio.com/view/photo/s_ratio_poster/public/\w\d+.\w+')
html_content=response.text
image_url=image_pattern.findall(html_content)
image_url=set(image_url)
#set强制变成集合
print(image_url)