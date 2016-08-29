#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.contrib import admin
##################################################

##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .models import Excursao, Cidade, Opcional
##################################################

# Registra as alteracoes no painel admin
admin.site.register(Excursao)
admin.site.register(Cidade)
admin.site.register(Opcional)