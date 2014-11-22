# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'accounts.views.log_in'),
    url(r'^logout/$', 'accounts.views.log_out'),
    url(r'^$', 'agrGIS.views.index'),
)
