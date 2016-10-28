from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('',
    url(r'^$', 'product.views.staff'),
)
