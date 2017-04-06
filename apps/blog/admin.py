# coding=utf-8
from django.contrib import admin

from .models import Article

__author__ = 'alexy'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'meta_title')
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
        (None, {
            'fields': ['title', 'text', ]
        }),
        (u'SEO', {
            'classes': ('collapse',),
            'fields': ['meta_title', 'meta_key', 'meta_desc', 'slug']
        }),
    ]


admin.site.register(Article, ArticleAdmin)
