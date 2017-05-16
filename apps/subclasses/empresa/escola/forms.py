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
from .models import Escola
##################################################

class EscolaRegisterForm(CompanyRegisterForm, forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(EscolaRegisterForm, self).__init__(*args, **kwargs)

		self.fields['razaosocial'].required = False
		self.fields['nomefantasia'].required = True
		self.fields['cnpj'].required = False
		self.fields['ie'].required = False
		self.fields['id_tipo_empresa'].required = False


		self.fields['cep'].required = False
		self.fields['rua'].required = False
		self.fields['bairro'].required = False
		self.fields['bairro'].required = False
		self.fields['cidade'].required = False
		self.fields['estado'].required = False
		self.fields['pais'].required = False
		self.fields['numeroed'].required = False
		self.fields['complemento'].required = False
		self.fields['pontoreferencia'].required = False
        
       
	
