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
from .views import ClienteRegister, ClienteList, ClienteDetail, ClienteDelete, ClienteEdit
##################################################


urlpatterns = (
	# CLIENTE URLS
	url(r'^dashboard/cliente/register/$', login_required(ClienteRegister.as_view()), name="cliente-register"),
	url(r'^dashboard/cliente/list/$', login_required(ClienteList.as_view()), name="cliente-list"),
	url(r'^dashboard/cliente/detail/(?P<pk>\d+)/$', login_required(ClienteDetail.as_view()), name="cliente-detail"),
	url(r'^dashboard/cliente/edit/(?P<pk>\d+)/$', login_required(ClienteEdit.as_view()), name="cliente-edit"),
	url(r'^dashboard/cliente/delete/(?P<pk>\d+)/$', login_required(ClienteDelete.as_view()), name="cliente-delete"),
)
