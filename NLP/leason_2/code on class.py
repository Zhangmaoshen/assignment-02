#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
language Model
pandas.read_csv(file, encoding= ) 方法
'''

import os
import pandas as pd
database='D:/doct/leason/NLP/leason2/Corpus/export_sql_1558435/sqlResult_1558435.csv'
print(os.path.exists(database))#判断文件是否存在
dataframe=pd.read_csv(database, encoding='gb18030')   #读csv文件
#print(dataframe)
all_articles=dataframe['content'].tolist()#把数组或矩阵等变为list
print(all_articles[:10])

import re
def token(string):
    return ' '.join(re.findall('[\w|\d]+', string))
#正则表达式，\w字母，\d数字,表示只要字母和数字
#过滤掉字符


all_articles = [token(str(a)) for a in all_articles]#更新了all_articles
print(all_articles[:10])

'''
text=''
for a in all_articles:
#所有字符串连接到一起，统计字符串长度
    text+=a
#print(len(text))
#.formate的作用：length of text: {len(text)}
'''

from functools import reduce
txt_from_reduce=reduce(lambda a1, a2:a1+a2, all_articles[:10])
#返回a1+a2，跟a的类型相同
print(type(txt_from_reduce))
print(txt_from_reduce)

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

import jieba
def cut(string):
    return list(jieba.cut(string))
print(cut('这是一个测试'))
text=''
for a in all_articles:
    text+=a
TEXT=text
print(TEXT)

