from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
import re, urllib
import json
import urlparse
from cgi import escape
#from .models import Post2
# Create your views here.
import feedparser



def Post(content, created_at):
    Post.content = []
    Post.created_at = 234234

def post_upload(request):
    return render(request,'personal/Main.html')

def index1(request):
    return render(request,'personal/Taller1_1.html')

def index2(request):
    return render(request,'personal/Taller1_2.html')

def index(request):
    if request.method == 'GET':
        return render(request, 'personal/Main.html', {})
    elif request.method == 'POST':
        #post1 = request.POST['content']
        post1 =""
        #urls = Crawl()
        urls = "asda"
        rss()
        # No need to call post.save() at this point -- it's already saved.
        #return HttpResponseRedirect(reverse('GET',"sdfsdfsdf"))
        #return render(request, 'personal/Main.html', post1)
        return render(request, "personal/Taller1_2.html", {'time': post1 ,'urls': urls})

def Crawl():
    myurl = "http://www.uniandes.edu.co/"
    url = "prueba"
    urls=[]
    #for n in range(1, 10):
    for i in re.findall('''(\w+[^w]\.\w+\....\.co)''', urllib.urlopen(myurl).read(), re.I):
    #for i in re.findall('''href=["'](?!/)[\w]+[:/]+(.[^"'w]+)["'/]''', urllib.urlopen(myurl).read(), re.I):
    #i = re.findall('''href=["']http://(.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I)
        #print i
        url = urlparse.urljoin(url, escape(i))
        if url not in urls:
            urls.append(url)
        #print long ( i )
                #for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                #print ee
    print "-------------\n"
    return urls
    #for i, url in enumerate(urls):
        #print "%d. %s" % (i, url)

def rss():
    e = feedparser.parse('http://www.elespectador.com/rss.xml')
    h = feedparser.parse('http://www.huffingtonpost.es/feeds/verticals/spain/index.xml')

    datos_e_title = []
    datos_e_link = []
    datos_e_descrip = []

    cont_e = 0
    cont_h = 0
    count_e = 0

    # defino una clase tipo Rss
    class rss:
        def __init__(self, title, link, description):
            self.title = title
            self.link = link
            self.description = description

    # funcion para crear un objeto Rss de diccionario de datos serializado
    def as_rss(rssdict):
        nuevorss = rss(rssdict['title'], rssdict['link'], rssdict['description'])
        return nuevorss

    # crear los rss y agregarlos a una lista
    rsslist = []
    for post_e in e.entries:
        # datos_e_title.insert(cont_e,post_e.title)
        # datos_e_link.insert(cont_e,post_e.link)
        # datos_e_descrip.insert(cont_e,post_e.description)
        myrss = rss(post_e.title, post_e.link, post_e.description)
        rsslist.append(myrss)
        # cont_e += 1

    for post_h in h.entries:
        # datos_h_title.insert(cont_h,post_h.title)
        # datos_h_link.insert(cont_h,post_h.link)
        # datos_h_descrip.insert(cont_h,post_h.description)
        myrss = rss(post_h.title, post_h.link, post_h.description)
        rsslist.append(myrss)
        # cont_h += 1
    # create list of vm dictionaries
    rssdictlist = []
    for myrss in rsslist:
        rssdictlist.append(myrss.__dict__)

    # convert dictionary list to json
    jsondata = json.dumps(rssdictlist)
    #print "objects serialized: " + jsondata

    # later - convert json into vm objects again
    # newvmlist=json.loads(jsondata, object_hook=as_rss)


    # ver la informacion
    f = open('C:\Users\lenovo\Documents\GitHub\BigData\personal\static\data2.json', 'w')
    f.write("{\n" + '"data"' + "    : \n")
    print >> f, jsondata
    f.write("}")
    f.close()