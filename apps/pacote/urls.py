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
from .views import PacoteRegister, PacoteEdit, PacoteList, PacoteDetail, PacoteDelete
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^dashboard/pacote/register/$', login_required(PacoteRegister.as_view()), name="pacote-register"),
	url(r'^dashboard/pacote/list/$', login_required(PacoteList.as_view()), name="pacote-list"),
	url(r'^dashboard/pacote/detail/(?P<pk>\d+)/$', login_required(PacoteDetail.as_view()), name="pacote-detail"),
	url(r'^dashboard/pacote/edit/(?P<pk>\d+)/$', login_required(PacoteEdit.as_view()), name="pacote-edit"),
	url(r'^dashboard/pacote/delete/(?P<pk>\d+)/$', login_required(PacoteDelete.as_view()), name="pacote-delete")
)
