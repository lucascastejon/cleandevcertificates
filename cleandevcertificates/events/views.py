# coding: utf-8
from django.shortcuts import render
from django.views.generic import base, ListView
from .models import Certified


class CertifiedListView(ListView):
    model = Certified
    template_name = "certified_list.html"


class CertifiedFormView(base.View):
    template_name = 'certified_form.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
