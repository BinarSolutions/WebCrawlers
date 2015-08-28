# -*- coding: utf-8 -*-
import string
import json
from pymongo import MongoClient
from unidecode import unidecode
import sys
client = MongoClient('mongodb://213.197.167.222:27317/')
db = client.SPYDERS
collection = db.bandymas

def str_to_collection(com1):
        com3 = com1.encode('utf-8').lower().strip().split()
        com2 = [str(i) for i in com3]
        return com2
#print str_to_collection("Labas.., kaip..'")

def punctuation(col):
    com4 = [s.translate(None, string.punctuation) for s in col]
    return com4

def col_stop(lang):
    if lang == 'lt':
        filename = "lt_stopwords.txt"
    elif lang == 'en':
        filename = "en_stopwords.txt"
    f1 =open(filename, "r")
    stop = [a.strip() for a in  f1.readlines()]
    f1.close()
    return stop

def fltr_stopw(col, stop):
    com2 = [a for a in col if not a in stop]
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

def insert_json(data):
    client = MongoClient('mongodb://213.197.167.222:27317/')
    db = client.SPYDERS
    collection = db['Spyder_List']
    with open(data) as data_file:
        data_c = json.load(data_file)
    collection.insert(data_c)


