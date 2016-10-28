from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('',
    #url(r'^$', 'users.views.staff'),
	url(r'^$', 'users.views.u_index'),
	url(r'^u_index/', 'users.views.u_index'),
	url(r'^test/', 'users.views.test'),
)
