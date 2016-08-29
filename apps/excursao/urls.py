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
from .views import ExcursaoRegister, ExcursaoList, ExcursaoDetail, ExcursaoDelete, ExcursaoEdit
from .views import CidadeRegister, CidadeList, CidadeDetail, CidadeDelete, CidadeEdit
##################################################


urlpatterns = (
	# EXCURSAO URLS
	url(r'^dashboard/excursao/register/$', login_required(ExcursaoRegister.as_view()), name="excursao-register"),
	url(r'^dashboard/excursao/list/$', login_required(ExcursaoList.as_view()), name="excursao-list"),
	url(r'^dashboard/excursao/detail/(?P<pk>\d+)/$', login_required(ExcursaoDetail.as_view()), name="excursao-detail"),
	url(r'^dashboard/excursao/edit/(?P<pk>\d+)/$', login_required(ExcursaoEdit.as_view()), name="excursao-edit"),
	url(r'^dashboard/excursao/delete/(?P<pk>\d+)/$', login_required(ExcursaoDelete.as_view()), name="excursao-delete"),

	# EXCURSAO URLS
	url(r'^dashboard/cidade/register/$', login_required(CidadeRegister.as_view()), name="cidade-register"),
	url(r'^dashboard/cidade/list/$', login_required(CidadeList.as_view()), name="cidade-list"),
	url(r'^dashboard/cidade/detail/(?P<pk>\d+)/$', login_required(CidadeDetail.as_view()), name="cidade-detail"),
	url(r'^dashboard/cidade/edit/(?P<pk>\d+)/$', login_required(CidadeEdit.as_view()), name="cidade-edit"),
	url(r'^dashboard/cidade/delete/(?P<pk>\d+)/$', login_required(CidadeDelete.as_view()), name="cidade-delete"),
)
