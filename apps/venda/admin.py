#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.contrib import admin
##################################################

##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .models import StatusReserva, StatusReservaPassageiro, Reserva, ReservaPassageiro, PassageiroOpcional
##################################################
# Registra as alteracoes no painel admin
admin.site.register(StatusReserva)
admin.site.register(StatusReservaPassageiro)
admin.site.register(Reserva)
admin.site.register(ReservaPassageiro)
admin.site.register(PassageiroOpcional)