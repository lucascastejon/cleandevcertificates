# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from datetime import datetime
from ..models import Person


class PersonModelTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(
            kind=u'S',
            name=u'Matheus Oliveira',
            cpf=u'364.622.978-08',
            email=u'oliveira.matheusde@gmail.com',
            course=u'Sistemas de Informação'
        )

    def test_create(self):
        self.assertTrue(self.person.pk)

    def test_unicode(self):
        self.assertEquals(u'Matheus Oliveira', unicode(self.person))

    def test_student(self):
        person = self.make_person(kind='S').save()

        self.assertTrue(person)

    def test_university(self):
        person = self.make_person(kind='U').save()

        self.assertTrue(person)

    def test_place(self):
        person = self.make_person(kind='P').save()

        self.assertTrue(person)

    def test_kind(self):
        person = self.make_person(kind='L')

        self.assertRaises(ValidationError, person.full_clean)

    def test_default_is_active_true(self):
        self.assertTrue(self.person.is_active)

    def test_has_created_at(self):
        self.assertIsInstance(self.person.created_at, datetime)

    def test_has_updated_at(self):
        self.assertIsInstance(self.person.updated_at, datetime)

    def test_unique_cpf(self):
        person = self.make_person()

        self.assertRaises(IntegrityError, person.save)

    def test_unique_email(self):
        person = self.make_person()

        self.assertRaises(IntegrityError, person.save)

    def make_person(self, **kwargs):
        data = dict(
            kind=u'S',
            name=u'Matheus Oliveira',
            cpf=u'364.622.978-08',
            email=u'oliveira.matheusde@gmail.com',
            course=u'Sistemas de Informação'
        )
        data.update(kwargs)
        person = Person(**data)

        return person
