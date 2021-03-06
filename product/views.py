# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
from merchant.models import Product

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


def p_index(request):
	limit = 3
	topics_list = Product.objects.all()
	paginator = Paginator(topics_list, limit)

	page = request.GET.get('page')  # 获取页码
	try:
		topics = paginator.page(page)  # 获取某页对应的记录
	except PageNotAnInteger:  # 如果页码不是个整数
		topics = paginator.page(1)  # 取第一页的记录
	except EmptyPage:  # 如果页码太大，没有相应的记录
		topics = paginator.page(paginator.num_pages)  # 取最后一页的记录

	return render(request,'product.html', {'topics': topics})
