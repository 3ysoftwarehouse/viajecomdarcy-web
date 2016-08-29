#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.contrib import admin
##################################################

##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .models import Acomodacao
##################################################

# Registra as alteracoes no painel admin
admin.site.register(Acomodacao)