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
##################################################

class EmployeeRegisterForm(UserRegisterForm, forms.Form):

	nickname = forms.CharField(label='Nickname:', max_length=20)

	def __init__(self, *args, **kwargs):
		super(EmployeeRegisterForm, self).__init__(*args, **kwargs)

		self.fields['nickname'].widget.attrs['class'] = 'form-control'
		self.fields['nickname'].widget.attrs['placeholder'] = 'Digite o nickname'