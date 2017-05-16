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
from apps.default.forms import UserRegisterForm
from apps.subclasses.empresa.agencia.models import Agencia
##################################################

class EmissorRegisterForm(UserRegisterForm, forms.ModelForm):
	id_agencia = forms.ModelChoiceField (label='Agência:', queryset = Agencia.objects.all(),required=True)
	def __init__(self, *args, **kwargs):
		super(EmissorRegisterForm, self).__init__(*args, **kwargs)
		self.fields['id_agencia'].widget.attrs['class'] = 'form-control'
		self.fields['password'].required = False
