# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse as r
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import base, ListView
from datetime import datetime
from cleandevcertificates.core.views import logged
from .models import Event, Certified

import simplejson


class CertifiedListView(ListView):
    model = Certified
    template_name = "certified_list.html"

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:login'))

        return super(CertifiedListView, self).dispatch(request, *args, **kwargs)


class CertifiedView(base.View):
    template_name = 'certified_form.html'
    model_event = Event
    certified = None
    event = None

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:login'))

        return super(CertifiedView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        self.event = self.get_event(request)
        self.certified = self.get_certified(request)

        if request.is_ajax():
            return HttpResponse(self.get_success_url(), status=300)

        return HttpResponseRedirect(self.get_success_url())

    def get_event(self, request):
        return get_object_or_404(self.model_event,
                                 token=request.POST.get('token'),
                                 token_expirate__lte=datetime.now())

    def get_certified(self, request):
        certified, created = Certified.objects.get_or_create(
            event=self.event, person=request.session['person']['pk'])
        return certified

    def get_success_url(self):
        return r("event:certified_detail", args=[],
                 kwargs={'pk': self.certified.pk})


class CertifiedDetailView(base.View):
    model = Certified
    template_name = "certified_detail.html"

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:login'))

        return super(CertifiedDetailView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        certified = get_object_or_404(self.model, pk=kwargs.get('pk'))

        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        action = request.POST.get("_action")

        if action == "rating":
            return self.rating(request, *args, **kwargs)

    def rating(self, request, *args, **kwargs):
        certified = get_object_or_404(self.model, pk=kwargs.get('pk'))
        certified.rating = request.POST.get("rating")
        certified.observation = request.POST.get("observation")
        certified.save()

        if request.is_ajax():
            return HttpResponse("ok", status=200)

        return render(request, self.template_name, locals())

    def send_certified(self, certified):
        pass
