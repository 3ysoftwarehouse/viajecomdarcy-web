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
from .views import *
from apps.venda import views
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^dashboard/reserva/nova/$', login_required(views.ReservaNova.as_view()), name="reserva-register"),
	url(r'^dashboard/reserva/register/(?P<pk>\d+)/$', login_required(ReservaRegister.as_view()), name="reserva-register"),
	url(r'^dashboard/reserva/pacote_json/(?P<pk>\d+)/$', ExcursaoPacoteJson.as_view(), name="pacote_json"),
	url(r'^dashboard/reserva/pacote_moeda_json/(?P<pk>\d+)/$', PacoteMoedaJson.as_view(), name="pacote_moeda_json"),    
	url(r'^dashboard/reserva/list/$', login_required(ReservaList.as_view()), name="reserva-list"),
	url(r'^dashboard/reserva/detail/(?P<pk>\d+)/$', login_required(ReservaDetail.as_view()), name="reserva-detail"),
	url(r'^dashboard/reserva/edit/(?P<pk>\d+)/$', login_required(ReservaEdit.as_view()), name="reserva-edit"),
	url(r'^dashboard/reserva/delete/(?P<pk>\d+)/$', login_required(ReservaDelete.as_view()), name="reserva-delete"),
	url(r'^dashboard/passageiro/opcional/(?P<pk>\d+)/$', login_required(PassageiroOpc.as_view()), name="passageiro-opcional"),
	url(r'^dashboard/passageiro/opcional/passageiro_opcional_json/(?P<id_reserva>\d+)/(?P<id_passageiro>\d+)$', login_required(PassageiroOpcJson.as_view()), name="passageiro-opcional-json"),
	url(r'^dashboard/passageiro/opcional/passageiro_opcional_json/(?P<id_reserva>\d+)/(?P<id_passageiro>\d+)/(?P<id_pacote>\d+)$', login_required(PassageiroOpcJson.as_view()), name="passageiro-opcional-json"),
	url(r'^dashboard/passageiro/opcional/passageiro_opcional_moeda_json/(?P<id_reserva_passageiro>\d+)/(?P<id_opcional>\d+)$', login_required(PassageiroOpcMoedaJson.as_view()), name="passageiro-opcional-moeda-json"),
	url(r'^dashboard/passageiro/opcional/passageiro_opcional_moeda_json/(?P<id_reserva_passageiro>\d+)/(?P<id_opcional>\d+)/(?P<id_pacote>\d+)$', login_required(PassageiroOpcMoedaJson.as_view()), name="passageiro-opcional-moeda-json"),
	url(r'^dashboard/reservapassageiro/(?P<pk>\d+)/$', login_required(addPassageiroToReserva), name="add-passageiro"),
	url(r'^dashboard/reservapassageiro/edit/$', login_required(editPassageiroReserva), name="edit-passageiro"),
	url(r'^dashboard/opcionalpassageiro/(?P<pk>\d+)/$', login_required(addOpcionalPassageiro), name="add-opcional"),
	url(r'^dashboard/finalizaragendamento/(?P<pk>\d+)/(?P<cl>\d+)/', login_required(finalizarAgendamento), name="finalizar-agendamento"),
)
