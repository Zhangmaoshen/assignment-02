#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
language Model
pandas.read_csv(file, encoding= ) 方法
.formate的作用：length of text: {len(text)}
'''
import os
import pandas as pd
import re
database='D:/doct/leason/NLP/leason2/Corpus/on_class-export_sql_1558435/sqlResult_1558435.csv'
#print(os.path.exists(database))#判断文件是否存在
dataframe=pd.read_csv(database, encoding='gb18030')   #读csv文件
print(dataframe)
all_articles=dataframe['content'].tolist()#把数组或矩阵等变为list
#print(all_articles[:10])

def token(string):
    return ' '.join(re.findall('[\w|\d]+', string))
#正则表达式，\w字母，\d数字,表示只要字母和数字
#过滤掉字符

all_articles = [token(str(a)) for a in all_articles]#更新了all_articles
print(all_articles[:10])

text=''
for a in all_articles[:10]:
    text+=a
#所有字符串连接成一个str，统计字符串长度，电脑原因，只取list:all_articles的前十个词条
#print(len(text))  共有12164个字

from functools import reduce
txt_from_reduce=reduce(lambda a1, a2:a1+a2, all_articles[:10])
#返回a1+a2，跟a的类型相同
print(type(txt_from_reduce))
print(txt_from_reduce)
#这其实跟for循环模块作用是一样的
TXT=txt_from_reduce

import jieba
def cut(string):
    return list(jieba.cut(string))
#定义切词函数cut
ALL_TOKENS=cut(TXT)
valida_tokens = [t for t in ALL_TOKENS if t.strip() and t != 'n']
#.strip()是去掉空格，t!='n'是去掉n
#valida_tokens是有效的分词后的list

from collections import Counter
words_count = Counter(valida_tokens)
frequences = [f for w, f in words_count.most_common(20)]
#Counter()返回dict，统计不同元素的出现频率，按频率由大到小排列
#frequences是频率排在前20的字的频率
#################################
'''
import matplotlib.pyplot as plt
x = [i for i in range(len(frequences))]
plt.plot(x, frequences)
plt.show()#使图像显示，关闭图像才能继续执行后面的语句
#画图，横坐标x，纵坐标frequences
'''
######################################3
frequences_all=[f for w, f in words_count.most_common()]
frequences_sun=sum(frequences_all)
print(frequences_sun)
#sum函数把list中int元素加起来，只能加int不然报错
#统计cut后词出现的总频率

def get_pro(word):
    if word in words_count:
        return words_count[word]/frequences_sun
    else:
        return 'beyond'
#得到词出现概率的函数get_pro(word)

#language_model_one_gram实现
#定义乘积函数
#把出现词的概率乘起来
def product(numbers):
    return reduce(lambda a1, a2:a1*a2, numbers)#numbers需要可迭代

def language_model_one_gram(string):
    words=cut(string)
    return product([get_pro(w) for w in words])

print(language_model_one_gram('我们一起'))

#2_Gram
all_2_grams_words = [''.join(valida_tokens[i:i+2]) for i in range(len(valida_tokens[:-2]))]
_2_gram_sum = len(all_2_grams_words)
_2_gram_counter = Counter(all_2_grams_words)
def get_combination_prob(w1, w2):
    if w1 + w2 in _2_gram_counter: return _2_gram_counter[w1+w2] / _2_gram_sum
    else:
        return 1 / _2_gram_sum
#prob(w1, w2)
def get_prob_2_gram(w1, w2):
    return get_combination_prob(w1, w2)/get_pro(w1)
#prob(w1, w2)/prob(w1)
print(get_prob_2_gram('我们', '吃'))

def langauge_model_of_2_gram(sentence):
    sentence_probability = 1
    words = cut(sentence)
    for i, word in enumerate(words):#enumerate(),i表示第几个（0,1...）word是对应的元素
        if i == 0:
            prob = get_pro(word)
        else:
            previous = words[i - 1]
            prob = get_prob_2_gram(previous, word)
        sentence_probability *= prob
    return sentence_probability
#句子的概率
print(langauge_model_of_2_gram('小明今天'))
