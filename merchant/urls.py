from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^m_index/', 'merchant.views.m_index'),
    url(r'^send_post/', 'merchant.views.send_post'),
    url(r'^handle_post/', 'merchant.views.handle_post'),
    url(r'^handle_post', 'merchant.views.handle_post'),
    url(r'^$', 'merchant.views.m_index'),
)

