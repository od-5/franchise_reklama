# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import LandingView

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.landing.views',
    url(r'^$', LandingView.as_view(), name='index'),
    url(r'^confidentiality/$', TemplateView.as_view(template_name='confidentiality.html'), name='confidentiality'),
    url(r'^thnx/$', TemplateView.as_view(template_name='ok.html'), name='thnx'),
)
