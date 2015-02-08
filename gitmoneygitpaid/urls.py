from django.conf.urls import patterns, include, url
from django.contrib import admin
from login import views

urlpatterns = patterns('',
	url(r'^$', views.windex, name='windex'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^accounts/profile/$', views.accountHome, name='account')
)
