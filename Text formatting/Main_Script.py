# -*- coding: utf-8 -*-
import sys
import json
import csv
import pymongo
import urllib
import pygeoip
from collections import Counter
from collections import OrderedDict
from pprint import pprint
from itertools import izip
from pymongo.errors import BulkWriteError
from pymongo import MongoClient
from Formatting import str_to_collection
from Formatting import punctuation
from Formatting import fltr_stopw
from Formatting import fltr_double
from Formatting import fltr_latin
from Formatting import col_stop
from Formatting import insert_json

client = MongoClient('mongodb://213.197.167.222:27317/')
db = client.SPYDERS
collection = db['LRytas_1']


#Bulk upsert scriptas, kuris sukuria is komentaru, wb ir prideda prie tu zodziu skaicius, kuris parodo kiek kartu
#tas zodis kartojosi.
lt = col_stop('lt')
en = col_stop('en')
bulkop = collection.initialize_ordered_bulk_op()
for coll in collection.find({}):
    bulkop.find({'_id': coll['_id']}).update({'$set': {"wbdc": punctuation(Counter(str_to_collection(fltr_latin(
coll['comment']))))}})
    bulkop.find({'_id': coll['_id']}).update({'$set': {"wb": punctuation(fltr_stopw(fltr_double(str_to_collection(
coll['comment'])), lt))}})
    bulkop.find({'_id': coll['_id']}).remove()

try:
    result = bulkop.execute( )
    pprint(result)
except BulkWriteError as bre:
    pprint(bre.details)

# Isfiltruoja komentarus, sudarydamas atskira wb, is to wb sudaro top 50 labiausiai pasikartojancius zodzius,
# ir suskaiciuoja kiek aplamai yra komentaru.
words = []
number = 0
for coll in collection.find():
    words += fltr_stopw(str_to_collection(fltr_latin(coll['post'])),lt)
    number += 1
words_g = dict(Counter(words).most_common(50))
words_c = fltr_double(words)
words_c_c = dict(Counter(words))

# Sukuria json faila is duotos informacijos.
data = {
    "Collection" : collection.name,
    "Comments" : number,
    "Top 50" : words_g,
    "Full_Wb" :words_c_c,
}
with open('json_test.json', 'w') as outfile:
    json.dump(data, outfile)
insert_json('json_test.json')

# Pagal surasta ip, suranda geolokacija.
gi = pygeoip.GeoIP('GeoLiteCity.dat')
for coll in collection.find():
    bulkop.find({'_id': coll['_id']}).update({'$set': {"geo" : gi.record_by_addr(coll['ip'])}})

try:
    result = bulkop.execute( )
    pprint(result)
except BulkWriteError as bre:
    pprint(bre.details)


#Removing attributes
#collection.update({},{'$unset': {'coll2':1}},multi=True)

# Taip pat sukuria json faila, tik sikart is daugiau duotos informacijos.

#city = []
#wb = []
#wbdc = []
#words = []
#unlike= []
#like = []
#author = []
#time = []
#date = []
#location = []
#number = 0
#or coll in collection.find():
    #city += coll['geo'].distinct('city')
    #wb += coll['wb']
    #words += fltr_stopw(str_to_collection(fltr_latin(coll['comment'])),lt)
    #number += 1
    #author += punctuation(str_to_collection(fltr_latin(coll['author'])))
    #time += str_to_collection(coll['time'])
    #date += str_to_collection(coll['date'])
    #location += coll['geo']
    #wbdc += punctuation(fltr_stopw(str_to_collection(fltr_latin(coll['comment'])), lt))
#fltr_author = [item for item in author if not item.isdigit()]
#words_g = dict(Counter(words).most_common(50))
#words_c = fltr_double(words)
#words_c_c = dict(Counter(words))
#data = {
    #"Collection" : collection.name,
    #"Comments" : number,
    #"Unlike" : unlike,
    #"Like" : like,
    #"Name" : author,
    #"Time" : time,
    #"Date" : date,
    #"Word_C": words_c_c,
    #"Word_Top" : words_g,
    #"Words" : wbdc,
    #"City" : location_new,

#}
#with open('Lrytas.json', 'w') as outfile:
    #json.dump(data, outfile)
#insert_json('Lrytas.json')


#Tekstini faila pavercia csv

#fh = open('lrytas_121.txt', 'r')
#stuff = fh.read()
#words_stuff = stuff.decode('latin-1')
#words_stuff_2 = punctuation(str_to_collection(fltr_latin(words_stuff)))
#fh.close()
#ith open('article_text.csv', 'w') as csvfile:
    #wr = csv.writer(csvfile,lineterminator='\n')
    #or val in words_stuff_2:
        #wr.writerow([val])
#csvfile.close()