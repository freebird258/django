# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
 
def first_page(request):
#    return HttpResponse("世界好")
	context          = {}
	context['label'] = 'HELL00OWORlD0000'
	context['test'] = 'hello test'
	return render(request, 'MysiteIndex.html', context)
