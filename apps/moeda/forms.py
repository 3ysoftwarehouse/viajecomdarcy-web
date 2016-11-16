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
from .models import Moeda # MODELS
##################################################

class MoedaForm(forms.ModelForm):

    class Meta:
        model = Moeda
        fields = ('moeda_desc', 'moeda_cambio', 'moeda_simbolo',)


    def __init__(self, *args, **kwargs):
        super(MoedaForm, self).__init__(*args, **kwargs)
        # moeda_desc Fields widget
        self.fields['moeda_desc'].widget.attrs['class'] = 'form-control'
        self.fields['moeda_desc'].widget.attrs['placeholder'] = 'Descrição'

        # moeda_cambio Fields widget
        self.fields['moeda_cambio'].widget.attrs['class'] = 'form-control'
        self.fields['moeda_cambio'].widget.attrs['placeholder'] = 'Cambio'

        # moeda_simbolo Fields widget
        self.fields['moeda_simbolo'].widget.attrs['class'] = 'form-control'
        self.fields['moeda_simbolo'].widget.attrs['placeholder'] = 'Simbolo'

    pass