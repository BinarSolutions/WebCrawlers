# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 17:49:25 2015

@author: Gediminas
"""
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://213.197.167.222:27317/')
db = client.SPYDERS
collection = db.LRytas_1

print unicode(collection.find_one()['comment'])
all_comments = [[unicode(comment['comment'])] for comment in collection.find()]

