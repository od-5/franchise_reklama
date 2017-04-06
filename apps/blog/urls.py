# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from .models import Article

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view(model=Article), name='list'),
    url(r'^(?P<slug>[\w-]+)$', DetailView.as_view(model=Article), name='detail'),
)
