# coding: utf-8
from django.conf.urls import url, patterns


urlpatterns = patterns('cleandevcertificates.core.views',
    url(r'^courses/courses_by_uniservity/(?P<pk>\d+)/$', 'courses_by_uniservity',
        name='courses_by_uniservity'),
)
