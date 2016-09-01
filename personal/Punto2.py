#!/usr/bin/python

#
# from http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python
# installed feedparser with `pip`, after installing pip with apt-get
#

import feedparser
import time
import re
import json
from subprocess import check_output


e = feedparser.parse('http://www.elespectador.com/rss.xml')
h = feedparser.parse('http://www.huffingtonpost.es/feeds/verticals/spain/index.xml')

datos_e_title=[]
datos_e_link=[]
datos_e_descrip=[]

cont_e=0
cont_h=0
count_e=0

#defino una clase tipo Rss
class rss:
    def __init__(self,title,link,description):
        self.title=title
        self.link=link
        self.description=description

#funcion para crear un objeto Rss de diccionario de datos serializado
def as_rss(rssdict):
    nuevorss=rss(rssdict['title'],rssdict['link'],rssdict['description'])
    return nuevorss

#crear los rss y agregarlos a una lista
rsslist=[] for post_e in e.entries:
    #datos_e_title.insert(cont_e,post_e.title)
    #datos_e_link.insert(cont_e,post_e.link)
    #datos_e_descrip.insert(cont_e,post_e.description)
    myrss = rss(post_e.title, post_e.link, post_e.description)
    rsslist.append(myrss)
    #cont_e += 1

for post_h in h.entries:
    #datos_h_title.insert(cont_h,post_h.title)
    #datos_h_link.insert(cont_h,post_h.link)
    #datos_h_descrip.insert(cont_h,post_h.description)
    myrss = rss(post_h.title, post_h.link, post_h.description)
    rsslist.append(myrss)
    #cont_h += 1


#create list of vm dictionaries
rssdictlist= []
for myrss in rsslist:
    rssdictlist.append(myrss.__dict__)

#convert dictionary list to json
jsondata=json.dumps(rssdictlist)
#print "objects serialized: " + jsondata

#later - convert json into vm objects again
#newvmlist=json.loads(jsondata, object_hook=as_rss)


#ver la informacion
f = open('data2.json', 'w')
f.write("{\n"+ '"data"' + "    : \n")
print >> f, jsondata
f.write("}")
f.close()
