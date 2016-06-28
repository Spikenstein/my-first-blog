from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.run_list, name='run_list'),
    url(r'^run/(?P<pk>[0-9]+)/$', views.run_detail, name='run_detail'),
    url(r'^newSelectionRun/$', views.newSelectionRun, name='newSelectionRun'),
    url(r'^newParametersRun/$', views.newParametersRun, name='newParametersRun'),
]
