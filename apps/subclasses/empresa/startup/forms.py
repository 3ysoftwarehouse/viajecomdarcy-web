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

class StartupRegisterForm(CompanyRegisterForm, forms.Form):

	representante = forms.CharField(label='Representante:', max_length=150, required=True)
	logo = forms.ImageField(label='Logo:')
