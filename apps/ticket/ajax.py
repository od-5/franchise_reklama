# coding=utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from core.models import Setup
from .forms import TicketForm
from .signals import new_ticket

__author__ = 'alexy'


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
            new_ticket.send(sender=ticket, email=ticket.mail, name=ticket.name)

    return HttpResponseRedirect(reverse('landing:thnx'))
    # else:
    #     return {
    #         'error': u'Заявка не была отправлена. Обновите страницу и попробуйте ещё раз.'
    #     }


def new_ticket_send(sender, **kwargs):
    """
    Обработка сигнала result_received
    """
    name = kwargs['name']
    email = kwargs['email']
    subject = u'Новое письмо'
    setup = Setup.objects.first()
    if setup and setup.video:
        video = setup.video
    else:
        video = None
    # msg_plain = render_to_string('email.txt', {'name': name})
    msg_html = render_to_string('ticket/mail.html', {'video': video})
    try:
        send_mail(
            subject,
            msg_html,
            settings.DEFAULT_FROM_EMAIL,
            [email, ],
            html_message=msg_html,
        )
    except:
        pass

new_ticket.connect(new_ticket_send)
