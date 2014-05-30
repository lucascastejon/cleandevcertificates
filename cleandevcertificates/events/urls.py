# coding: utf-8
from django.conf.urls import url, patterns
from .views import CertifiedListView, CertifiedFormView


urlpatterns = patterns('cleandevcertificates.views',
    url(r'^certified/$', CertifiedFormView.as_view(), name='certified'),
    url(r'^certified/(?P<token>\w+)/$', CertifiedFormView.as_view(),
        name='certified'),
    url(r'^$', CertifiedListView.as_view(), name='certificates'),
)
