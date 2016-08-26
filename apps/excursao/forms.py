#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
from django.conf import settings
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################

##################################################

class ExcursaoRegisterForm(forms.Form):

	excurcao_desc = forms.CharField(label='Descrição',max_length=45)
	is_active = forms.BooleanField(label='Ativa')

	def __init__(self, *args, **kwargs):
		super(ExcursaoRegisterForm, self).__init__(*args, **kwargs)
		# excurcao_desc Fields widget
		self.fields['excurcao_desc'].widget.attrs['class'] = 'form-control'
		self.fields['excurcao_desc'].widget.attrs['placeholder'] = 'Digite a descrição'

		# is_active Fields widget
		self.fields['is_active'].widget.attrs['class'] = 'form-control'
		self.fields['is_active'].widget.attrs['checked'] = 'checked'
		pass


