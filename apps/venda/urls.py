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
from .views import ReservaRegister, ReservaList, ReservaDetail, ReservaEdit, ReservaDelete, ExcursaoPacoteJson, PacoteMoedaJson
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^dashboard/reserva/register/$', login_required(ReservaRegister.as_view()), name="reserva-register"),
	url(r'^dashboard/reserva/pacote_json/(?P<pk>\d+)/$', ExcursaoPacoteJson.as_view(), name="pacote_json"),
	url(r'^dashboard/reserva/pacote_moeda_json/(?P<pk>\d+)/$', PacoteMoedaJson.as_view(), name="pacote_moeda_json"),    
	url(r'^dashboard/reserva/list/$', login_required(ReservaList.as_view()), name="reserva-list"),
	url(r'^dashboard/reserva/detail/(?P<pk>\d+)/$', login_required(ReservaDetail.as_view()), name="reserva-detail"),
	url(r'^dashboard/reserva/edit/(?P<pk>\d+)/$', login_required(ReservaEdit.as_view()), name="reserva-edit"),
	url(r'^dashboard/reserva/delete/(?P<pk>\d+)/$', login_required(ReservaDelete.as_view()), name="reserva-delete")
)
