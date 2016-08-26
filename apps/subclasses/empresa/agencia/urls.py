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
from .views import AgenciaRegister, AgenciaEdit, AgenciaList, AgenciaDetail, AgenciaDelete
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^dashboard/agencia/register/$', login_required(AgenciaRegister.as_view()), name="agencia-register"),
	url(r'^dashboard/agencia/list/$', login_required(AgenciaList.as_view()), name="agencia-list"),
	url(r'^dashboard/agencia/detail/(?P<pk>\d+)/$', login_required(AgenciaDetail.as_view()), name="agencia-detail"),
	url(r'^dashboard/agencia/edit/(?P<pk>\d+)/$', login_required(AgenciaEdit.as_view()), name="agencia-edit"),
	url(r'^dashboard/agencia/delete/(?P<pk>\d+)/$', login_required(AgenciaDelete.as_view()), name="agencia-delete")
)
