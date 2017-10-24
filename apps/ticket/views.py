# coding=utf-8
from __future__ import unicode_literals

from django.views.generic import CreateView
from django.shortcuts import get_object_or_404

from .models import Ticket, TicketComment
from .forms import TicketCommentForm


class TicketCommentCreateView(CreateView):
    model = TicketComment
    form_class = TicketCommentForm

    def get_form(self, form_class=None):
        ticket = get_object_or_404(Ticket, pk=self.kwargs.get('pk'))
        form = super(TicketCommentCreateView, self).get_form(form_class)
        form.instance.ticket = ticket
        return form

    def form_valid(self, form):
        ticket = form.instance.ticket
        ticket.contact_date = form.cleaned_data['contact_date']
        ticket.save()
        return super(TicketCommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '')
