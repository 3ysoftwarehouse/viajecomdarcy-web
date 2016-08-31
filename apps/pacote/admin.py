#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.contrib import admin
##################################################

##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .models import Pacote, PacoteCidade, PacoteOpcional, PacoteAcomadacao
##################################################

# Registra as alteracoes no painel admin
admin.site.register(Pacote)
admin.site.register(PacoteCidade)
admin.site.register(PacoteOpcional)
admin.site.register(PacoteAcomadacao)