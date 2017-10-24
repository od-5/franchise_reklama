# coding=utf-8
from __future__ import unicode_literals

from django.contrib import admin
from django.template.loader import render_to_string
from django.conf.urls import patterns, url

from .models import Ticket, Sale
from .views import TicketCommentCreateView
from .forms import TicketAdminForm, SaleAdminForm


class _TicketModalsMixin(admin.ModelAdmin):

    class Media:
        css = {
            'all': (
                'css/jquery.datetimepicker.min.css',
            )
        }
        js = (
            'js/jquery.datetimepicker.full.min.js',
            'ticket/js/ticket_modal.js',
        )

    def get_urls(self):
        urls = super(_TicketModalsMixin, self).get_urls()
        urls = patterns(
            '',
            url(r'^(?P<pk>\d+)/create_comment/$', self.admin_site.admin_view(TicketCommentCreateView.as_view()),
                name='ticket_ticket_create_comment')
        ) + urls
        return urls

    def utm_modal_button(self, obj):
        return render_to_string('admin/ticket/utm_labels_button.html', {'instance': obj})
    utm_modal_button.short_description = 'Метки utm'

    def comment_modal_button(self, obj):
        return render_to_string('admin/ticket/comment_button.html', {'instance': obj})
    comment_modal_button.short_description = 'Комментарий менеджера'


class TicketAdmin(_TicketModalsMixin, admin.ModelAdmin):
    list_display = ('name', 'phone', 'mail', 'status', 'contact_date', 'manager', 'comment_modal_button', 'city',
                    'time_zone', 'utm_modal_button')
    list_filter = ['mail', 'created', 'status', 'manager', 'contact_date']
    search_fields = ['mail', 'manager']
    date_hierarchy = 'created'
    readonly_fields = ('country', 'city', 'time_zone')
    fields = ('name', 'phone', 'mail', 'country', 'city', 'time_zone', 'status', 'contact_date',
              'manager', 'ticket_comment', 'sale')
    form = TicketAdminForm

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            qs = Ticket.objects.filter(sale=False)
        else:
            qs = Ticket.objects.filter(manager=user, sale=False)
        return qs


class SaleAdmin(_TicketModalsMixin, admin.ModelAdmin):

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return self.model.objects.filter(sale=True)
        else:
            return self.model.objects.filter(manager=user, sale=True)

    def has_add_permission(self, request, obj=None):
        return False

    list_display = ('name', 'phone', 'mail', 'created', 'price', 'comment_modal_button', 'utm_modal_button')
    list_filter = ['mail', 'created', 'status', 'manager']
    search_fields = ['mail', 'manager']
    date_hierarchy = 'created'
    readonly_fields = ('country', 'city', 'time_zone')
    fields = ('name', 'phone', 'mail', 'country', 'city', 'time_zone', 'manager', 'ticket_comment', 'price')
    form = SaleAdminForm


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sale, SaleAdmin)
