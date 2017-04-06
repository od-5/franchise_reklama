# coding=utf-8
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse_lazy

from django.db import models

from core.base_model import CommonPage

__author__ = 'alexy'


class Article(CommonPage):
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
        app_label = 'blog'

    text = RichTextField(verbose_name=u'Описание')
    slug = models.SlugField(verbose_name=u'url')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article:detail', args=(self.slug,))
