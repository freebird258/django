# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
 
def first_page(request):
    #return HttpResponse("世界好")
	context          = {}
	context['label'] = 'Hello World!'
	return render(request, 'test.html', context)
