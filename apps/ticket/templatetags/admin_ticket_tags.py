# coding=utf-8
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.inclusion_tag('admin/ticket/tags/modal_utm_labels.html')
def modal_utm_labels(cl):
    return {
        'instances': cl.result_list
    }


@register.inclusion_tag('admin/ticket/tags/modal_comment.html', takes_context=True)
def modal_comment(context, cl):
    return {
        'instances': cl.result_list,
        'path': context['request'].path
    }
