from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

from views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.login),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^index',views.index123),

    url(r'^registration',views.registration),
]
