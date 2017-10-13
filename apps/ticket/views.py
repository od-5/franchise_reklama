# coding=utf-8
from __future__ import unicode_literals

from django.views.generic import UpdateView

from .models import Ticket
from .forms import TicketCommentForm


class UpdateTicketCommentView(UpdateView):
    model = Ticket
    form_class = TicketCommentForm

    def get_success_url(self):
        return self.request.GET.get('next', '')
