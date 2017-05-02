# coding=utf-8
from django.contrib import admin

from .models import Article

__author__ = 'alexy'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'meta_title', 'pic')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('pic', )
    fieldsets = [
        (None, {
            'fields': ['title', 'cover', 'pic', 'preview', 'text', ]
        }),
        (u'SEO', {
            'classes': ('collapse',),
            'fields': ['meta_title', 'meta_key', 'meta_desc', 'slug']
        }),
    ]


admin.site.register(Article, ArticleAdmin)
