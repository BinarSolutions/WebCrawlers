# -*- coding: utf-8 -*-
import string
from unidecode import unidecode
import sys

def str_to_collection(com1):
        com3 = com1.encode('utf-8').lower().strip().split()
        com2 = [str(i) for i in com3]
        com4 = [s.translate(None, string.punctuation) for s in com2]
        return com4
#print str_to_collection("Labas.., kaip..'")

def fltr_stopw(col):
    filename = "en_stopwords.txt"
    f =open(filename, "r")
    lines = [a.strip() for a in  f.readlines()]
    f.close()
    com2 = [a for a in col if not a in lines]
    return com2

def fltr_double(seq):
        result = []
        for item in seq:
            if item in result: continue
            result.append(item)
        return result

def fltr_latin(com):
    #txt1 = com.decode('utf-8')
    txt2 = unidecode(com)
    return txt2
