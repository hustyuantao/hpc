from django.conf.urls import patterns, url
from rank import views

urlpatterns = patterns('',
	url(r'^top100/(?P<nth>\d+)/$', views.list)
)