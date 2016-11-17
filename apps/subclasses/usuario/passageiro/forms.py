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
from apps.subclasses.empresa.escola.models import Escola
##################################################

class PassageiroRegisterForm(UserRegisterForm, forms.Form):

	id_escola = forms.ModelChoiceField (label='Escola:', queryset = Escola.objects.all())
	matricula = forms.IntegerField(label='Matricula CN:')
	natularidade = forms.CharField(label='Natularidade:', max_length=30)
	observacao = forms.CharField(label='Obs:', max_length=250, widget=forms.Textarea)
	numero_passaporte = forms.CharField(label='Numero do Passaporte:', max_length=10, required=False)
	data_validade_passaporte = forms.DateField(required=False)

	def __init__(self, *args, **kwargs):
		super(PassageiroRegisterForm, self).__init__(*args, **kwargs)

		self.fields['id_escola'].widget.attrs['class'] = 'form-control'
		self.fields['matricula'].widget.attrs['class'] = 'form-control'
		self.fields['matricula'].widget.attrs['placeholder'] = 'Digite a matricula'
		self.fields['natularidade'].widget.attrs['class'] = 'form-control'
		self.fields['natularidade'].widget.attrs['placeholder'] = 'Digite a natularidade'
		self.fields['observacao'].widget.attrs['class'] = 'form-control'
		self.fields['observacao'].widget.attrs['placeholder'] = 'Digite algumas observacões'
		self.fields['numero_passaporte'].widget.attrs['class'] = 'form-control'
		self.fields['data_validade_passaporte'].widget.attrs['class'] = 'form-control'