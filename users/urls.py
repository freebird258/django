from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('',
    url(r'^$', 'users.views.staff'),
#	url(r'^$', 'users.views.first_page'),
)
