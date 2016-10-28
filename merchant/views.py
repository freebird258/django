# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from django.core.cache import caches

import memcache

def staff(request):
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
