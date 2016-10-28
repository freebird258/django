from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('',
    url(r'^p_index', 'product.views.p_index'),
    url(r'^$', 'product.views.p_index'),
)
