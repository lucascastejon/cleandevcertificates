# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime
from django.conf import settings


class Event(models.Model):
    name = models.CharField(_(u'nome'), max_length=250)
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
    token_expirate = models.DateTimeField(
        _(u'data de expiração'), blank=True, null=True)
    is_active = models.BooleanField(_(u'ativo?'), default=True)
    created_at = models.DateTimeField(_(u'criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'alterado em'), auto_now=True)

    class Meta:
        verbose_name = _(u'Evento')
        verbose_name_plural = _(u'Eventos')
        ordering = ['-date']

    def __unicode__(self):
        return self.name

    def _generate_token(self):
        token = u'{pk}{date}{now}'.format(pk=self.pk,
                                          date=self.date.toordinal(),
                                          now=datetime.now().toordinal())[:8]
        return u''.join(sorted(token))

    def _generate_token_expirate(self):
        dat = datetime.fromordinal(self.date.toordinal() + 2)

        return dat

    def persons(self):
        return self.certified.persons_set.filter(is_active=True)

    def rating(self):
        return self.certified_set.exclude(rating__isnull=True)\
            .aggregate(models.Sum('rating'))

    def comments(self):
        return self.certified_set.exclude(comment__isnull=True).all()


class Certified(models.Model):
    person = models.ForeignKey('core.Person', verbose_name=_(u'pessoa'))
    event = models.ForeignKey('Event', verbose_name=_(u'evento'))
    rating = models.IntegerField(_(u'classificação'), blank=True, null=True)
    observation = models.TextField(_(u'observação'), blank=True)
    is_active = models.BooleanField(_(u'ativo?'), default=True)
    created_at = models.DateTimeField(_(u'criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'alterado em'), auto_now=True)

    class Meta:
        verbose_name = _(u'Certificado')
        verbose_name_plural = _(u'Certificados')
        ordering = ['-event__date']

    def __unicode__(self):
        return self.person.name

    def get_download_url(self):
        uri = '/events/certified/download/%s-%s' % (self.person.pk, self.event.pk)
        return '%s%s' % (settings.SITE_URL, uri)


def event_pre_save(signal, sender, instance, **kwargs):
    # generate token
    if not instance.token:
        token = instance._generate_token()
        new_token = token
        while Event.objects.filter(token=new_token).exclude(pk=instance.pk).count() > 0:
            new_token = instance._generate_token()

        instance.token = new_token
        instance.token_expirate = instance._generate_token_expirate()
models.signals.pre_save.connect(event_pre_save, sender=Event)
