from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

import settings


import uebungen

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_digisys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^digisys/', include('uebungen.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
