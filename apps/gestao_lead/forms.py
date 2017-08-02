#-*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from .models import *


class ProspectForm(forms.ModelForm):

    class Meta:
        model = Prospect
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProspectForm, self).__init__(*args, **kwargs)
        self.fields['nome_completo'].widget.attrs['class'] = 'form-control'
        self.fields['nome_completo'].widget.attrs['placeholder'] = 'Digite o nome completo'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite o email'
        self.fields['telefone'].widget.attrs['class'] = 'form-control telefone'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Digite o telefone' 
        self.fields['escola'].widget.attrs['class'] = 'form-control'
        self.fields['escola'].widget.attrs['placeholder'] = 'Selecione uma Escola' 
        self.fields['observacao'].widget.attrs['class'] = 'form-control'
        self.fields['observacao'].widget.attrs['placeholder'] = 'Digite as observações' 