#-*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from apps.default.forms import CompanyRegisterForm

class AgenciaRegisterForm(CompanyRegisterForm, forms.ModelForm):
    logo = forms.ImageField(label='Logo:', required=False)
    def __init__(self, *args, **kwargs):
        super(AgenciaRegisterForm, self).__init__(*args, **kwargs)
        self.fields['logo'].widget.attrs['class'] = 'form-control'
        self.fields['logo'].widget.attrs['placeholder'] = 'Escolha uma logo'

       
