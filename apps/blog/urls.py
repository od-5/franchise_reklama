# coding=utf-8
from django.conf.urls import patterns, url

from .views import ArticleList, ArticleDetail

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', ArticleList.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)$', ArticleDetail.as_view(), name='detail'),
)
