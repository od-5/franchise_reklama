# coding=utf-8
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.phone_inform import getphoneObject
from core.base_model import Common
from core.models import User

__author__ = 'alexy'


class Ticket(Common):
    TICKET_STATUS_CHOICE = (
        (0, u'В обработке'),
        (1, u'Новая заявка'),
        (2, u'Отклонена'),
        (3, u'Нет ответа'),
        (4, u'Предпродажа'),
    )

    manager = models.ForeignKey(to=User, verbose_name=u'Менеджер', blank=True, null=True)
    name = models.CharField(verbose_name=u'Имя', max_length=256)
    phone = models.CharField(verbose_name=u'Телефон', max_length=20)
    mail = models.EmailField(verbose_name=u'e-mail', max_length=100)
    status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки', choices=TICKET_STATUS_CHOICE, default=1)
    theme = models.CharField(verbose_name=u'Тема', max_length=256, blank=True, null=True)
    ticket_comment = models.TextField(verbose_name=u'Комментарий менеджера', blank=True, null=True)
    sale = models.BooleanField(verbose_name=u'Продажа', default=False)
    price = models.PositiveIntegerField(verbose_name=u'Сумма', blank=True, null=True)
    country = models.CharField(max_length=200, verbose_name=u'Страна', blank=True, null=True)
    city = models.CharField(max_length=200, verbose_name=u'Город', blank=True, null=True)
    time_zone = models.CharField(max_length=10, verbose_name=u'Часовой пояс', blank=True, null=True)
    contact_date = models.DateTimeField(verbose_name=u'Дата контакта', blank=True, null=True)

    utm_source = models.CharField(max_length=256, default='')
    utm_medium = models.CharField(max_length=256, default='')
    utm_campaign = models.CharField(max_length=256, default='')
    utm_content = models.CharField(max_length=256, default='')
    utm_term = models.CharField(max_length=256, default='')

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'ticket'
        ordering = ['-contact_date']

    def __unicode__(self):
        return self.name

    def performed_at(self):
        pass


class TicketComment(Common):
    ticket = models.ForeignKey(Ticket, verbose_name=u'Заявка', on_delete=models.CASCADE)
    text = models.TextField(verbose_name=u'Комментарий менеджера', blank=True, null=True)


class Sale(Ticket):
    class Meta:
        proxy = True
        verbose_name = u'Продажа'
        verbose_name_plural = u'Продажи'


@receiver(pre_save, sender=Ticket)
def get_geophone_info(sender, **kwargs):
    ticket = kwargs['instance']
    if not ticket.id:
        api_key = settings.HTMLWEB_API_KEY
        try:
            data = getphoneObject(ticket.phone, api_key)
            if data.has_key('country'):
                if data['country'].has_key('fullname'):
                    ticket.country = data['country']['fullname']
            elif data.has_key('fullname'):
                ticket.country = data['fullname']
            if data.has_key('0'):
                if data['0'].has_key('name'):
                    ticket.city = data['0']['name']
                if data['0'].has_key('time_zone'):
                    ticket.time_zone = data['0']['time_zone']
            if not ticket.time_zone and data.has_key('time_zone'):
                ticket.time_zone = data['time_zone']
        except:
            # ticket.country = data['0']['country']
            pass
