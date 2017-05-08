#
'''needs python3, must install autocorrect program via "sudo pip install autocorrect" 
Usage:
* put text to be corrected in "misspell.txt" 
* run script with output to output file ("python3 spell.py> out.txt") which will give original text from misspell.txt on one line, the correction, if any, on the next, with a ~~~ separator between each compared word. 
*If we can clean up the segmentation of words better, it would work better.
Rich Rath update of Bosco Huang's initial script'''

import os
import string
from autocorrect  import spell
#cwd = os.getcwd()
#print (cwd)

file = open("misspell.txt",'r')
txt = file.read().split()
txt1 = file.read()
txt_without_punc = []
a = list()
sep1 = "~~~~~~~~~~~~~~~~~~~"
for word in txt:
    tmp = word.strip(string.punctuation)
    cor_text = spell(tmp)
    a = a + cor_text.split()
    print (sep1)
    print (tmp)
    print (cor_text) 
