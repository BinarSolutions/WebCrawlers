import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import re
import itertools
import string
import unicodedata
import sys
#import Censor
#import Repeat_2_working
client = MongoClient('mongodb://213.197.167.222:27317/') # prisijungia prie db
db = client.SPYDERS
collection = db.Reddit_1

def lower(): # sita funkcija visas raides padarys maziosiomis, istrins visus skyrybos zenklus, ir pavers zodzius kolectionu.
     for com1 in collection.find({ }): # nurodau, kad paimtu viska is colleciono ||||||||||||||
        com3 = com1['comment'].encode('utf-8').lower().strip().split() # nurodau, kad tik komentarus paimtu, ir suformatuoju teksta |||||||||||||
        com2 = [str(i) for i in com3]
        com4 = [s.translate(None, string.punctuation) for s in com2]
        return com4
print "Sveiki, ar noretumet teksta paversti mazosiomis raidemis, ir paversti tuos zodzius collectionu?"
print "T\N?"
anw = raw_input()
if "T" in anw:
    print lower()
else:
    pass


def cen(): # stop words
    filename = "C:/Python/Text formatting/Dictionary.txt"
    f =open(filename, "r")
    lines = f.readlines()
    f.close()
    com2 = [a for a in lower() if not a in lines]
    return com2
print "Dabar, ar noretumet pasalinti zodzius is duoto zodyno?"
print "T\N?"
anw2 = raw_input()
if "T" in anw2:
    print cen()
else:
    pass

rcom = cen()
def repeat(seq, idfun=None): # pasikartojancius zodzius istrina
        if idfun is None:
            def idfun(x): return x
        seen = {}
        result = []
        for item in seq:
            marker = idfun(item)
            if marker in seen: continue
            seen[marker] = 1
            result.append(item)
        return result
print "Ir galiausiai ar noretumet pasalinti zodziu pasikartojimus?"
print "T\N?"
anw3 = raw_input()
if "T" in anw3:
    print repeat(rcom)
else:
    pass
stuff = repeat(rcom)
save = open("Isfiltruotas_tekstas.txt", "w") # sukuria tekstini faila, kuris isaugo suformatuota teksta
for item in stuff:
    save.write("%s\n" % item)
save.close()