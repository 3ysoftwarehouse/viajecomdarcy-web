#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.decorators import login_required
##################################################

##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .views import StartupRegister, StartupEdit, StartupList, StartupDetail, StartupDelete
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^dashboard/startup/register/$', login_required(StartupRegister.as_view()), name="startup-register"),
	url(r'^dashboard/startup/list/$', login_required(StartupList.as_view()), name="startup-list"),
	url(r'^dashboard/startup/detail/(?P<pk>\d+)/$', login_required(StartupDetail.as_view()), name="startup-detail"),
	url(r'^dashboard/startup/edit/(?P<pk>\d+)/$', login_required(StartupEdit.as_view()), name="startup-edit"),
	url(r'^dashboard/startup/delete/(?P<pk>\d+)/$', login_required(StartupDelete.as_view()), name="startup-delete")
)
