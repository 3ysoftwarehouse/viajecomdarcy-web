#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
from django.conf import settings
from django.contrib.admin.widgets import FilteredSelectMultiple
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from .models import Acomodacao # MODELS
##################################################

class AcomodacaoForm(forms.ModelForm):

    class Meta:
        model = Acomodacao
        fields = ('acomodacao_desc', 'sigla', 'numero',)


    def __init__(self, *args, **kwargs):
        super(AcomodacaoForm, self).__init__(*args, **kwargs)
        # acomodacao_desc Fields widget
        self.fields['acomodacao_desc'].widget.attrs['class'] = 'form-control'
        self.fields['acomodacao_desc'].widget.attrs['placeholder'] = 'Descrição'

        # sigla Fields widget
        self.fields['sigla'].widget.attrs['class'] = 'form-control'
        self.fields['sigla'].widget.attrs['placeholder'] = 'Sigla'

        # numero Fields widget
        self.fields['numero'].widget.attrs['class'] = 'form-control'
        self.fields['numero'].widget.attrs['placeholder'] = 'Número'

    pass