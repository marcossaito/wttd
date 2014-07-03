# coding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.core.views',
		url(r'^$','homepage', name='homepage'),
		url(r'^palestrantes/$','speakers', name='speakers'),
		url(r'^palestrantes/(?P<slug>[\w-]+)/$', 'speaker_detail', name='speaker_detail' )
	)