#coding: utf-8
from django.dispatch import Signal

__author__ = 'alexy'


new_ticket = Signal(providing_args=["email", 'name'])
