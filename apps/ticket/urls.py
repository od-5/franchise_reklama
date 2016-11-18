# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.ticket.ajax',
    url(r'^$', 'ticket_send', name='send'),
    url(r'^mail/$', TemplateView.as_view(template_name='ticket/mail.html'), name='mail'),
)
