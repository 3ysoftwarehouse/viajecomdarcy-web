#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from apps.default.forms import CompanyRegisterForm
##################################################

class AgenciaRegisterForm(CompanyRegisterForm, forms.Form):
    logo = forms.ImageField(label='Logo:', required=False)


    def __init__(self, *args, **kwargs):
        super(AgenciaRegisterForm, self).__init__(*args, **kwargs)
       
        self.fields['logo'].widget.attrs['class'] = 'form-control'
        self.fields['logo'].widget.attrs['placeholder'] = 'Escolha uma logo'

       
        pass
