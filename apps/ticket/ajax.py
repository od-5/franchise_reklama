# coding=utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from core.models import Setup
from .forms import TicketForm

__author__ = 'alexy'


@ajax_request
@csrf_exempt
def ticket_send(request):
    try:
        email = Setup.objects.all().first().email
        if not email:
            email = 'od-5@yandex.ru'
    except:
        email = 'od-5@yandex.ru'
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.save()
            mail_theme_msg = u'franchise.reklamadoma.com - %s' % ticket.theme
            message = u'Тема: %s\nИмя: %s\nТелефон: %s\nE-mail: %s\n' % \
                      (ticket.theme, ticket.name, ticket.phone, ticket.mail)
            send_mail(
                mail_theme_msg,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email, ]
            )
        return {
            'success': u'Ваша заявка принята!'
        }
    else:
        return {
            'error': u'Заявка не была отправлена. Обновите страницу и попробуйте ещё раз.'
        }
