# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:34:38 2017

@author: bhuang
"""

import os
import string
from autocorrect  import spell
cwd = os.getcwd()
print cwd
#os.chdir('C:/Users/bhuang/Documents/Python')
os.chdir('C:/Users/YuBo/Dropbox/Pyhon')
file = open("misspell.txt",'r')
txt = file.read().split()
txt1 = file.read()
txt_without_punc = []
a = list()
for word in txt:
    tmp = word.strip(string.punctuation)
    cor_text = spell(tmp)
    a = a + cor_text.split()


