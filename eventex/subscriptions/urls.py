from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.subscriptions.views', 
		url(r'^$', 'subscribe', name='subscribe'),
		url(r'^(\d+)/$', 'success', name='success')
	)