# coding: utf-8
from django.shortcuts import render
from django.views.generic import base, TemplateView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse as r
from django.core import serializers
from .models import Person
from .forms import PersonForm, FormLogin


def home(request):
    return render(request, "index.html")


class HomeView(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:login'))

        return super(HomeView, self).dispatch(request, *args, **kwargs)


class LoginView(base.View):
    template_name = 'login.html'
    form_class = FormLogin

    def get(self, request):
        if logged(request):
            return HttpResponseRedirect(r('core:home'))

        form = self.form_class()

        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.full_clean()
        form.errors['non_field_errors'] = form.error_class(
            ['Usuário não encontrado. Verifique CPF ou Email.'])

        person = Person(cpf=request.POST.get('cpf'),
                        email=request.POST.get('email')).verify()

        if person:
            if set_session(request, person):
                return HttpResponseRedirect(r('core:home'))

        return render(request, self.template_name, locals())


class LogoutView(base.View):

    def get(self, request, *args, **kwargs):
        del request.session['person']

        return HttpResponseRedirect(r('core:login'))


class PersonCreateView(CreateView):
    template_name = 'person_form.html'
    form = PersonForm()
    model = Person

    def dispatch(self, request, *args, **kwargs):
        if logged(request):
            return HttpResponseRedirect(r('core:home'))

        return super(PersonCreateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        set_session(self.request, self.object)
        return r('core:home')


class PersonUpdateView(UpdateView):
    template_name = 'person_form.html'
    form = PersonForm
    model = Person

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:home'))

        return super(PersonUpdateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        set_session(self.request, self.object)

        return r('core:home')


def courses_by_uniservity(self, pk):
    try:
        university = Person.objects.get(pk=pk)
        json = serializers.serialize('json', university.courses())

        return HttpResponse(json)
    except:
        return HttpResponse(None)


def set_session(request, person):
    request.session['person'] = dict(pk=person.pk,
                                     name=person.name,
                                     email=person.email)
    request.session.save()
    return True


def logged(request):
    try:
        person = Person.objects.get(pk=request.session.get('person')['pk'])

        return person
    except:
        return False
