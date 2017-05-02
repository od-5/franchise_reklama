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
    preview = models.TextField(verbose_name=u'Анонс', blank=True, null=True)
    cover = models.ImageField(verbose_name=u'Обложка', blank=True, null=True, upload_to='blog/')
    slug = models.SlugField(verbose_name=u'url')

    def pic(self):
        if self.cover:
            return '<img src="%s" width="100"/>' % self.cover.url
        else:
            return '----'

    pic.short_description = u"миниатюра"
    pic.allow_tags = True

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article:detail', args=(self.slug,))

    def get_preview_text(self):
        if self.preview:
            return self.preview
        else:
            return self.text[:300]
