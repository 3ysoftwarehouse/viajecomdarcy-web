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
from .views import AcomodacaoRegister, AcomodacaoEdit, AcomodacaoList, AcomodacaoDetail, AcomodacaoDelete
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^dashboard/acomodacao/register/$', login_required(AcomodacaoRegister.as_view()), name="acomodacao-register"),
	url(r'^dashboard/acomodacao/list/$', login_required(AcomodacaoList.as_view()), name="acomodacao-list"),
	url(r'^dashboard/acomodacao/detail/(?P<pk>\d+)/$', login_required(AcomodacaoDetail.as_view()), name="acomodacao-detail"),
	url(r'^dashboard/acomodacao/edit/(?P<pk>\d+)/$', login_required(AcomodacaoEdit.as_view()), name="acomodacao-edit"),
	url(r'^dashboard/acomodacao/delete/(?P<pk>\d+)/$', login_required(AcomodacaoDelete.as_view()), name="acomodacao-delete")
)
