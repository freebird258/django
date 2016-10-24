from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), 
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'mysite.views.first_page'),
	url(r'^users/', include('users.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
