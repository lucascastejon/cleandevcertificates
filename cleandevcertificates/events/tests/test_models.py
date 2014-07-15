# coding: utf-8
from django.test import TestCase
from datetime import datetime
from cleandevcertificates.core.models import Person
from ..models import Event


class EventModelTest(TestCase):

    def setUp(self):
        place = Person.objects.create(
            name=u'Unifran', email=u'contato@unifran.br')
        speaker = Person.objects.create(
            name=u'Matheus Oliveira', email=u'matheus@coder42.com')
        self.event = Event.objects.create(
            name=u'Introdução ao Python',
            workload=4,
            date=datetime(2014, 10, 07, 14, 00, 00),
            place=place,
            complement=u'',
            speaker=speaker,
            post=u'')

    def test_create(self):
        self.assertTrue(self.event.id)

    def test_unicode(self):
        self.assertEquals(u'Introdução ao Python', unicode(self.event))

    def test_exists_token(self):
        self.assertTrue(self.event.token)

    def test_has_token_expirate(self):
        self.assertIsInstance(self.event.token_expirate, datetime)

    def test_has_date(self):
        self.assertIsInstance(self.event.date, datetime)
