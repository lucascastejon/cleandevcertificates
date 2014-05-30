# coding: utf-8
from django.conf.urls import url, patterns
from .views import HomeView, LoginView, PersonUpdateView


urlpatterns = patterns('cleandevcertificates.core.views',
    url(r'^core/courses/courses_by_uniservity/(?P<pk>\d+)/$', 'courses_by_uniservity',
        name='courses_by_uniservity'),
    url(r'^person/$', PersonUpdateView.as_view(), name='person_edit'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', HomeView.as_view(), name='home'),
)
