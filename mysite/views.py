# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
 
def first_page(request):
#    return HttpResponse("世界好")
	context          = {}
	context['label'] = 'hello000000'
	context['test'] = 'hello test'
	return render(request, 'mysite.html', context)

