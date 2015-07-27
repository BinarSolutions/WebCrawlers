# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:35:32 2015

@author: Gediminas
"""
import string
import sys
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

def manof(a):
    return a.lower()
    
def str_to_collection(com1): # sita funkcija visas raides padarys maziosiomis, istrins visus skyrybos zenklus, ir pavers zodzius kolectionu.
     #for com1 in collection.find({ }): # nurodau, kad paimtu viska is colleciono ||||||||||||||
    com3 = com1.translate(None, string.punctuation).encode('utf-8').lower().strip().split() # nurodau, kad tik komentarus paimtu, ir suformatuoju teksta |||||||||||||
    com2 = [str(i) for i in com3]
    #com4 = [s.translate(None, string.punctuation) for s in com2]
    return com2
    
    
def cen(col): # stop words
    filename = "en_stopwords.txt"
    f =open(filename, "r")
    lines = [a.strip() for a in f.readlines()]
    f.close()
    com2 = [a for a in col if not a in lines]
    return com2
    
def repeat(seq): # pasikartojancius zodzius istrina
        result = []
        for item in seq:
            if item in result: continue
            result.append(item)
        return result
        
