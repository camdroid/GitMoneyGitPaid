from django.conf.urls import patterns, include, url
from django.contrib import admin

uurlpatterns = patterns('',
    url(r'^login/', include('login.urls')),
)
