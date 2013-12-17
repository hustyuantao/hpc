from django.conf.urls import patterns, url
from top100 import views

urlpatterns = patterns('',
	url(r'^(?P<nth>\d+)/$', views.detail, name="detail"),
)