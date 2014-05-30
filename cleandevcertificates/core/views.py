# coding: utf-8
from django.http import HttpResponse
from django.core import serializers
from .models import Person


def courses_by_uniservity(self, pk):
    try:
        university = Person.objects.get(pk=pk)
        json = serializers.serialize('json', university.courses())

        return HttpResponse(json)
    except:
        return HttpResponse(None)
