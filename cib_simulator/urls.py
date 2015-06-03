from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

from sampleapp.views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'cib_simulator.views.login',name = "login"),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^index','cib_simulator.views.index123',name='index'),

    #url(r'^reg','cib_simulator.views.reg',name='reg'),

    url(r'^create/$', 'cib_simulator.views.create'),

    url(r'^login_view/$', 'cib_simulator.views.login_view'),

    #url(r'^registration',views.registration),
]
