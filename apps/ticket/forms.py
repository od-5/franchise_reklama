# coding=utf-8
from django.forms import ModelForm
from .models import Ticket

__author__ = 'Rylcev Alexy'


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'mail', 'phone', 'theme',)


class TicketCommentForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticket_comment',)
