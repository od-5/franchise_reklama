# coding=utf-8
from django.forms import ModelForm

from suit.widgets import EnclosedInput, AutosizedTextarea

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


class TicketAdminForm(ModelForm):
    class Meta:
        widgets = {
            'comment': AutosizedTextarea,
            'ticket_comment': AutosizedTextarea,
        }


class SaleAdminForm(ModelForm):
    class Meta:
        widgets = {
            'price': EnclosedInput(append=u'руб.'),
            'comment': AutosizedTextarea,
            'ticket_comment': AutosizedTextarea,
        }
