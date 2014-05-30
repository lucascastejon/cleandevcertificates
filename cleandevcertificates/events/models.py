# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import datetime


class Event(models.Model):
    name = models.CharField(_(u'name'), max_length=250)
    workload = models.IntegerField(_(u'carga horária'))
    date = models.DateTimeField(_(u'data e hora'))
    place = models.ForeignKey('core.Person', verbose_name=_(u'Local'),
                              related_name='place',
                              limit_choices_to={'kind__in': ['U', 'P']})
    complement = models.CharField(_(u'Complemento'), max_length=50, blank=True)
    speaker = models.ForeignKey('core.Person', verbose_name=_(u'Palestrante'),
                                related_name='speaker',
                                limit_choices_to={'kind': 'S'})
    post = models.URLField(_(u'Post'), blank=True)
    token = models.CharField(_(u'token'), max_length=50, blank=True)
    token_expirate = models.DateField(
        _(u'data de experação'), blank=True, null=True)
    is_active = models.BooleanField(_(u'ativo?'), default=True)
    created_at = models.DateTimeField(_(u'criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'alterador em'), auto_now=True)

    class Meta:
        verbose_name = _(u'Evento')
        verbose_name_plural = _(u'Eventos')
        ordering = ['-date']

    def __unicode__(self):
        return self.name

    def _generate_token(self):
        return False
        now = datetime.now()
        ordinal = u'{0}'.format(now.toordinal())

        token = u'{pk}{ordinal}{key}'.format(
            pk=self.pk, ordinal=ordinal, key=settings.SECRET_KEY)

        return token

    @property
    def persons(self):
        return self.certified.persons_set.filter(is_active=True)

    @property
    def rating(self):
        return self.certified_set.exclude(rating__isnull=True)\
            .aggregate(models.Sum('rating'))

    @property
    def comments(self):
        return self.certified_set.exclude(comment__isnull=True).all()


class Certified(models.Model):
    person = models.ForeignKey('core.Person', verbose_name=_(u'pessoa'))
    event = models.ForeignKey('Event', verbose_name=_(u'evento'))
    rating = models.IntegerField(_(u'classificação'), blank=True, null=True)
    observation = models.TextField(_(u'observação'), blank=True)
    is_active = models.BooleanField(_(u'ativo?'), default=True)
    created_at = models.DateTimeField(_(u'criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'alterador em'), auto_now=True)

    class Meta:
        verbose_name = _(u'Certificado')
        verbose_name_plural = _(u'Certificados')
        ordering = ['-event__date']

    def __unicode__(self):
        return self.person.name


def event_post_save(instance, **kwargs):
    instance.token = instance._generate_token()
models.signals.post_save.connect(event_post_save, sender=Event)
