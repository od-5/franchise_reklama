# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .ajax import city_map

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', city_map, name='map'),
)
