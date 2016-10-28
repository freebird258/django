#!/usr/bin/env python

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), 

	url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'mysite.views.first_page'),

	url(r'^product/', include('product.urls')),
	url(r'^merchant/', include('merchant.urls')),
	url(r'^users/', include('users.urls')),
]
