# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.landing.views',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^confidentiality/$', TemplateView.as_view(template_name='confidentiality.html'), name='confidentiality'),
    url(r'^thnx/$', TemplateView.as_view(template_name='ok.html'), name='thnx'),
)
