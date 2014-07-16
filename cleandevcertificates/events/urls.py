# coding: utf-8
from django.conf.urls import url, patterns
from .views import CertifiedListView, CertifiedView, CertifiedDetailView, CertifiedSuccessView


urlpatterns = patterns('cleandevcertificates.views',
    url(r'^certified/success/$', CertifiedSuccessView.as_view(),
        name='certified_success'),
    url(r'^certified/(?P<pk>\d+)/$', CertifiedDetailView.as_view(),
        name='certified_detail'),
    url(r'^certified/$', CertifiedView.as_view(), name='certified'),
    url(r'^$', CertifiedListView.as_view(), name='certified_list'),
)
