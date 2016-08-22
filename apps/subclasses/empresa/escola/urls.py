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
from .views import EscolaRegister, EscolaEdit, EscolaList, EscolaDetail, EscolaDelete
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^dashboard/escola/register/$', login_required(EscolaRegister.as_view()), name="escola-register"),
	url(r'^dashboard/escola/list/$', login_required(EscolaList.as_view()), name="escola-list"),
	url(r'^dashboard/escola/detail/(?P<pk>\d+)/$', login_required(EscolaDetail.as_view()), name="escola-detail"),
	url(r'^dashboard/escola/edit/(?P<pk>\d+)/$', login_required(EscolaEdit.as_view()), name="escola-edit"),
	url(r'^dashboard/escola/delete/(?P<pk>\d+)/$', login_required(EscolaDelete.as_view()), name="escola-delete")
)
