# coding: utf-8
from django.shortcuts import render
from django.views.generic import base, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse as r
from django.core import serializers
from .models import Person
from .forms import PersonForm


class HomeView(TemplateView):
    template_name = "index.html"


class PersonUpdateView(base.View):
    template_name = 'person_form.html'
    form_class = PersonForm

    def get(self, request):
        logged()

        form = self.form_class(instance=request.user)

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logged()

        form = self.form_class(request.POST, instance=request.user)

        if not form.is_valid():
            return render(request, self.template_name)

        form.save()
        return HttpResponseRedirect(r('core:home'))


class LoginView(base.View):
    template_name = 'login.html'
    form_class = FormLogin

    def get(self, request):
        logged()

        form = self.form_class()

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logged()
        form = self.form_class(request.POST)

        person = Person(cpf=request.POST.get('cpf'),
                        email=request.POST.get('email'))
        if not person.verify():
            return render(request, self.template_name, locals())

        # Set person in session
        set_session(request, person)
        return HttpResponseRedirect(r('core:home'))


def courses_by_uniservity(self, pk):
    logged()

    try:
        university = Person.objects.get(pk=pk)
        json = serializers.serialize('json', university.courses())

        return HttpResponse(json)
    except:
        return HttpResponse(None)


def set_session(request, person):
    request.session['person'] = person


def logged():
    try:
        person = Person.objects.get(pk=request.session.get('person').pk)

        return person
    except Exception as e:
        return HttpResponseRedirect(r('core:login'))
