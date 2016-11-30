# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from django.core.cache import caches
from django.views.decorators.csrf import csrf_exempt
from celery import Celery

import memcache,json,urllib2,urllib

def http_get(url,headers=None):
    req = urllib2.Request(url)
    if headers :
        for k,v in headers.iteritems():
            req.add_header(k,v)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError,e:
        print e
        #print e.read()
    else:
        the_page = response.read()
        print the_page


def m_index(request):
	#mc = memcache.Client(['127.0.0.1:11211'])
	#telnet 127.0.0.1 11211
	#stats items
	#stats cachedump 7 0  //本例中为7，第2个参数为列出的长度，0为全部列出
	cache = caches['default']
#	cache.set('key1', 'test',1000000)
	context          = {}
	context['hello'] = cache.get('key1')
	context['a'] = 'aaaa'
	print context['hello']
	return render(request, 'merchant.html', context)

def send_post(request):
	return render(request, "investigate.html")

app = Celery('view',bloker='redis://localhost:6379/1')

@csrf_exempt
@app.task
def handle_post(request):
	ctx ={}
#	ctx.update(csrf(request))
#	if request.method == 'POST':
#		data = eval(request.body)
#		ctx['rlt'] = data["staff"]
#	else:
	ctx['rlt'] = "nothing"
	#http_get("http://127.0.0.1:8001")
	#return HttpResponse(ctx['rlt'])
	return HttpResponse(json.dumps(ctx),content_type="application/json")	
