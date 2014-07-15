# coding: utf-8
from django.contrib import admin
from .models import Event, Certified


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'token', 'created_at')
    date_hierarchy = 'date'


class CertifiedAdmin(admin.ModelAdmin):
    list_display = ('person', 'event', 'created_at')
    date_hierarchy = 'created_at'


admin.site.register(Event, EventAdmin)
admin.site.register(Certified, CertifiedAdmin)
