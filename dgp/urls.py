from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.run_list, name='run_list'),
    url(r'^run/(?P<pk>[0-9]+)/$', views.run_detail, name='run_detail'),
    url(r'^newRun/$', views.newRun, name='newRun'),
]
