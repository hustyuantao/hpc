from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hpc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'portal.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^portal/', include('portal.urls', namespace="portal")),
	url(r'^top100/', include('top100.urls', namespace="top100")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
