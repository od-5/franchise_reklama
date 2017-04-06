# coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import debug_toolbar
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',

    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('core.urls')),
    url(r'', include('apps.landing.urls', namespace='landing')),
    url(r'ticket/', include('apps.ticket.urls', namespace='ticket')),
    url(r'city/', include('apps.city.urls', namespace='city')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'blog/', include('apps.blog.urls', namespace='article')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
