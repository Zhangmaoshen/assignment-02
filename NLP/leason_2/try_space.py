#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import jieba
def cut(string):
    a=list(jieba.cut(string))
    return [t for t in a if t.strip() and t != 'n']
print('  '.strip())


sentences = """
这是一个比较正常的句子
这个一个比较罕见的句子
小明毕业于清华大学
小明毕业于秦华大学
""".split()
print(sentences)

for _ in range(10):
    print(1)