#-*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Acomodacao 

class AcomodacaoForm(forms.ModelForm):

    class Meta:
        model = Acomodacao
        fields = ('acomodacao_desc', 'sigla', 'numero',)


    def __init__(self, *args, **kwargs):
        super(AcomodacaoForm, self).__init__(*args, **kwargs)
        self.fields['acomodacao_desc'].widget.attrs['class'] = 'form-control'
        self.fields['acomodacao_desc'].widget.attrs['placeholder'] = 'Descrição'
        self.fields['sigla'].widget.attrs['class'] = 'form-control'
        self.fields['sigla'].widget.attrs['placeholder'] = 'Sigla'
        self.fields['numero'].widget.attrs['class'] = 'form-control'
        self.fields['numero'].widget.attrs['placeholder'] = 'Número'

