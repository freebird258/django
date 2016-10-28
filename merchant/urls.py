from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^m_index/', 'merchant.views.m_index'),
    url(r'^$', 'merchant.views.m_index'),
)

