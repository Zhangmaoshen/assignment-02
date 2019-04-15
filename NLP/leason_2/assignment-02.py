#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
database_00=open('D:/doct/leason/NLP/leason2/Corpus/extracted/AA_simple/wiki_00',  'r', encoding='UTF-8')
database_01=open('D:/doct/leason/NLP/leason2/Corpus/extracted/AA_simple/wiki_01',  'r', encoding='UTF-8')
'''
database_02=open('D:/doct/leason/NLP/leason2/Corpus/extracted/AA_simple/wiki_02',  'r', encoding='UTF-8')
'''
data_00=database_00.read()
data_01=database_01.read()
'''
data_02=database_02.read()
'''
database_00.close()
database_01.close()
'''
database_02.close()
import  re
import jieba
def token(string):
    return ' '.join(re.findall('[\w|\d]+', string))
'''
data_00_clear_str=token(data_00)
data_01_clear_str=token(data_01)
'''
data_02_clear_str=token(data_02)
'''
data_00_clear_gen=jieba.cut(data_00_clear_str)
data_01_clear_gen=jieba.cut(data_01_clear_str)
'''
data_02_clear_gen=jieba.cut(data_02_clear_str)
'''
data_00_clear_list=list(data_00_clear_gen)
data_01_clear_list=list(data_01_clear_gen)
'''
data_02_clear_list=list(data_02_clear_gen)

data_full_clear_list=data_02_clear_list
                     #+data_01_clear_list+data_00_clear_list
#太大读不出来，只用最小的一个文件试一下
##########################

#词频，总词频
##################################################
from collections import Counter
words_count = Counter(data_full_clear_list)#返回一个dict，统计词重复出现的次数
frequency_list = [f for w, f in words_count.most_common()]#w是词，f是频率
frequency_sum=sum(frequency_list)
####################################

#概率
##########################################################3
def get_pro(word):#某个词的概率
    if word in words_count:
        return words_count[word]/frequency_sum
    else:
        return 'beyond'
def product(numbers):#数的累乘
    return reduce(lambda a1, a2:a1*a2, numbers)
##############################################################################
'''
2_gram
'''
def Numerator_2gram(w1, w2):
    if w1 in words_count and w2 in words_count:
        return product([get_pro(w1), get_pro(w2)])
    else:
        return 'out of range'
def language_model_2gram(sentence):
    pro_2gram=1
    sentence_gen=jieba.cut(sentence)
    sentence_list = list(sentence_gen)
    for i, word in enumerate(sentence_list):
        if i==0:
            return get_pro(word)
        else:
            Numerator=Numerator_2gram(word, sentence_list[i-1])
            Denominator = get_pro(sentence_list[i - 1])
            pro_2gram *=Numerator/Denominator
        return pro_2gram
#################################################################


#3_gram
########################################################################
def Numerator_3gram(w1, w2, w3):
    if w1 in words_count and w2 in words_count and w3 in words_count:
        return product([get_pro(w1), get_pro(w2), get_pro(w3)])
    else:
        return 'out of range'
def Denominator_3gram(w1, w2):
    if w1 in words_count and w2 in words_count:
        return product([get_pro(w1), get_pro(w2)])
    else:
        return 'out of range'

def language_model_3gram(sentence):
    pro_3gram = 1
    sentence_gen = jieba.cut(sentence)
    sentence_list = list(sentence_gen)
    for i, word in enumerate(sentence_list):
        if i == 0:
            return get_pro(word)
        elif i == 1:
            return get_pro([sentence_list[0], sentence_list[1]])
        else:
            Numerator = Numerator_3gram(word, sentence_list[i - 1], sentence_list[i-2])
            Denominator=Denominator_3gram(sentence_list[i-1], sentence_list[i-2])
            pro_3gram *= Numerator/Denominator
        return pro_3gram
##################################################################

#测试
#####################################################################
pro_2gram=language_model_2gram('我们试一下看看效果')
pro_3gram=language_model_3gram('我们试一下看看效果')
print(pro_2gram)
print(pro_3gram)



