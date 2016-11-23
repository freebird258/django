# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from django.core.cache import caches
from django.views.decorators.csrf import csrf_exempt

import memcache,json

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

@csrf_exempt 
def handle_post(request):
	ctx ={}
#	ctx.update(csrf(request))
	if request.method == 'POST':
		data = eval(request.body)
		ctx['rlt'] = data["staff"]
	else:
		ctx['rlt'] = "nothing"
	return HttpResponse(ctx['rlt'])
	#return HttpResponse(json.dumps(request.body),content_type="application/json")	
