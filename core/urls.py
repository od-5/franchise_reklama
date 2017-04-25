# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

__author__ = 'alexy'


urlpatterns = patterns(
    'core.views',
    url(r'^googlecadc02ecd2bbe3fb\.html', TemplateView.as_view(template_name='googlecadc02ecd2bbe3fb.html')),
    url(r'^robots\.txt', 'get_robots_txt', name='robots'),
    url(r'^sitemap\.xml', 'get_sitemap_xml', name='sitemap'),
)
