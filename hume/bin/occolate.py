#!/usr/bin/python
import sys
import re
from itertools import izip

# This is a comment line
inpf1 = sys.argv[1]
fp1 = open(inpf1)
inpf2 = sys.argv[2]
fp2 = open(inpf2)
out_file="occolate_out.txt"
#print "\n"
#print "occolate: Choose best result out of two"
#print "        :    1. occropy output for normal letters"
#print "        :    2. occropy output for italics letters"
print "input  files = %s,  %s" % (inpf1, inpf2)
#print "output file = %s" % (out_file)
ofp = open(out_file,'w')

def is_punctuation(letter):
    ol=ord(letter)
    if ol>32 and ol<48:
        return 1;
    if ol>57 and ol<65:
        return 1;
    if ol>90 and ol<97:
        return 1;
    return 0;

for line1, line2 in izip(fp1, fp2):
    line1=line1.strip('\n')
    line2=line2.strip('\n')
    print "line1= %s" % (line1)
    print "line2= %s" % (line2)
    is_punc1=[]
    is_punc2=[]
    linelist1=line1.split(" ")
    linelist2=line2.split(" ")
    len1=len(linelist1)
    len2=len(linelist2)
    nfor=max(len1,len2)
    for ii in range(0,nfor):
        if ii < len1:
            linestr1=linelist1[ii]
        else:
            linestr1=";;;;;;;;;;;;"
        if ii < len2:
            linestr2=linelist2[ii]
        else:
            linestr2=";;;;;;;;;;;;"
        #print
        #print "linestr1=%s" % (linestr1)
        #print "linestr2=%s" % (linestr2)
        is_punc1.append(0)                  # Default is_punc=0
        is_punc2.append(0)                  # Default is_punc=0
        #if len(linestr1) < 2:
        #    print "Warning: Single letter word"
        #print "Converting alpha letters"
        is_punc_s1=0
        is_punc_s2=0
        for letter1 in linestr1[:-1]:
            #print "letter1=%c" % (letter1)
            is_punc_s1=is_punc_s1 + is_punctuation(letter1)
            #print "is_punc1=%d" % (is_punc1)
        for letter2 in linestr2[:-1]:
            #print "letter1=%c" % (letter1)
            is_punc_s2=is_punc_s2 + is_punctuation(letter2)
            #print "is_punc1=%d" % (is_punc1)
        is_punc1[ii]=is_punc_s1
        is_punc2[ii]=is_punc_s2
        #print "is_punc1=%d" % (is_punc1)
        ii=ii+1
    nstr=ii-1
    print "No of strings = %d" % (nstr+1)

    newline=""
    for ii in range(0, nstr):
        if is_punc1[ii] > is_punc2[ii]:
            newstr=linelist2[ii]
        else:
            newstr=linelist1[ii]
        newline=newline+newstr+" "
    if nstr > -1:
        if is_punc1[nstr] > is_punc2[nstr]:
            newline=newline+linelist2[nstr]
        else:
            newline=newline+linelist1[nstr]
    print "new line= %s" % (newline)
    ofp.write(newline)
    ofp.write("\n")
print "\n"
