# coding=utf-8
from __future__ import unicode_literals

from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        utm_labels = {
            arg_name: arg_value for arg_name, arg_value in request.GET.items() if arg_name.startswith('utm_')
        }
        request.session['utm_labels'] = utm_labels

        return super(LandingView, self).get(request, *args, **kwargs)
