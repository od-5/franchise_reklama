# coding=utf-8
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

__author__ = 'alexy'


class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data()
        last_article = Article.objects.all()[:3]
        context.update({
            'last_article': last_article
        })
        return context
