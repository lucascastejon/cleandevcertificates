# coding: utf-8
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .managers import KindPersonManager


class Person(models.Model):
    KIND_CHOICES = (
        ('S', _(u'Aluno')),
        ('U', _(u'Universidade')),
        ('P', _(u'Local')),
    )

    kind = models.CharField(_(u'tipo'), max_length=1,
                            choices=KIND_CHOICES, default="S")
    university = models.ForeignKey('self', verbose_name=_(
        u'faculdade'), blank=True, null=True,
        limit_choices_to={'kind__in': ['U', 'P']})
    course = models.CharField(_(u'curso'), max_length=100, blank=True)
    semester = models.IntegerField(_(u'semestre'), blank=True, null=True)
    name = models.CharField(_(u'nome'), max_length=100)
    cpf = models.CharField(_(u'CPF'), max_length=20, blank=True, null=True)
    email = models.EmailField(_(u'e-mail'), max_length=100, unique=True)
    city = models.CharField(_(u'cidade'), max_length=50, blank=True)
    facebook = models.URLField(_(u'facebook'), blank=True)
    twitter = models.CharField(_(u'twitter'), max_length=50, blank=True)
    image = models.URLField(_(u'URL imagem'), blank=True)
    is_active = models.BooleanField(_(u'ativo?'), default=True)
    created_at = models.DateTimeField(_(u'criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'alterador em'), auto_now=True)

    objects = models.Manager()
    students = KindPersonManager('S')
    universities = KindPersonManager('U')
    places = KindPersonManager(['U', 'P'])

    class Meta:
        verbose_name = _(u'Pessoa')
        verbose_name_plural = _(u'Pessoas')
        ordering = ['name']

    """
    def save(self, *args, **kwargs):
        if Person.objects\
                .filter(cpf=self.cpf)\
                .count():
            raise ValidationError(_(u'Pessoa com este CPF já existe.'))

        if Person.objects\
                .filter(email=self.email)\
                .count():
            raise ValidationError(_(u'Pessoa com este E-mail já existe.'))

        return super(Person, self).save(*args, **kwargs)
    """

    def __unicode__(self):
        return self.name

    def verify(self):
        try:
            self = Person.objects.get(cpf=self.cpf, email=self.email)
            return self
        except:
            return None

    def courses(self):
        return self.person_set.all().order_by('course').distinct('course')

    def events(self):
        return self.certfied.events_set.filter(is_active=True)

    def certficates(self):
        return self.certfied_set.filter(is_active=True)
