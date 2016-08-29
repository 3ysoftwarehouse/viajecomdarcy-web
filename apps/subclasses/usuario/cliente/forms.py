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

class ClienteRegisterForm(UserRegisterForm, forms.Form):

	dt_emissao_rg = forms.DateField(label='Data emissão RG:',input_formats=settings.DATE_INPUT_FORMATS)
	tempo_residencia = forms.CharField(label='Tempo de residência:', max_length=45)
	empresa = forms.CharField(label='Nome da Empresa:', max_length=45)
	cep_empresa = forms.CharField(label='Cep da empresa:', max_length=45)
	endereco_empresa = forms.CharField(label='Endereço da Empresa:', max_length=45)
	telefone_empresa = forms.CharField(label='Telefone da Empresa:', max_length=45)
	dt_admissao = forms.DateField(label='Data de adminissão:',input_formats=settings.DATE_INPUT_FORMATS)
	cargo = forms.CharField(label='Cargo ou Função:', max_length=45)
	principal_renda = forms.CharField(label='Renda Principal:', max_length=45)
	outra_renda = forms.CharField(label='Outras Rendas:', max_length=45)
	patrimonio = forms.CharField(label='Patrimonio:', max_length=45)
	banco = forms.CharField(label='Banco onde tem conta:', max_length=45)
	agencia = forms.CharField(label='Agência:', max_length=45)
	conta = forms.CharField(label='Conta:', max_length=45)
	dt_banco = forms.DateField(label='Cliente do bancos desde:',input_formats=settings.DATE_INPUT_FORMATS)
	telefone_banco = forms.CharField(label='Telefone do banco:', max_length=45)

	def __init__(self, *args, **kwargs):
		super(ClienteRegisterForm, self).__init__(*args, **kwargs)

		self.fields['dt_emissao_rg'].widget.attrs['class'] = 'form-control'
		self.fields['dt_emissao_rg'].widget.attrs['placeholder'] = 'Digite a data de emissão do RG'
		self.fields['tempo_residencia'].widget.attrs['class'] = 'form-control'
		self.fields['tempo_residencia'].widget.attrs['placeholder'] = 'Digite o tempo de residência'
		self.fields['empresa'].widget.attrs['class'] = 'form-control'
		self.fields['empresa'].widget.attrs['placeholder'] = 'Digite o nome da empresa'
		self.fields['cep_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['cep_empresa'].widget.attrs['placeholder'] = 'Digite o cep da empresa'
		self.fields['endereco_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['endereco_empresa'].widget.attrs['placeholder'] = 'Digite o endereço da empresa'
		self.fields['telefone_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['telefone_empresa'].widget.attrs['placeholder'] = 'Digite o telefone da empresa'
		self.fields['dt_admissao'].widget.attrs['class'] = 'form-control'
		self.fields['dt_admissao'].widget.attrs['placeholder'] = 'Digite a data de adminissão'
		self.fields['cargo'].widget.attrs['class'] = 'form-control'
		self.fields['cargo'].widget.attrs['placeholder'] = 'Digite o cargo'
		self.fields['principal_renda'].widget.attrs['class'] = 'form-control'
		self.fields['principal_renda'].widget.attrs['placeholder'] = 'Digite o valor da reda principal'
		self.fields['outra_renda'].widget.attrs['class'] = 'form-control'
		self.fields['outra_renda'].widget.attrs['placeholder'] = 'Digite o valor de outras rendas'
		self.fields['patrimonio'].widget.attrs['class'] = 'form-control'
		self.fields['patrimonio'].widget.attrs['placeholder'] = 'Digite o valor do patrimonio'
		self.fields['banco'].widget.attrs['class'] = 'form-control'
		self.fields['banco'].widget.attrs['placeholder'] = 'Digite o numero do banco'
		self.fields['agencia'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['placeholder'] = 'Digite a agência'
		self.fields['conta'].widget.attrs['class'] = 'form-control'
		self.fields['conta'].widget.attrs['placeholder'] = 'Digite o numero da conta'
		self.fields['dt_banco'].widget.attrs['class'] = 'form-control'
		self.fields['dt_banco'].widget.attrs['placeholder'] = 'Digite a data aproximada de inicio da conta'
		self.fields['telefone_banco'].widget.attrs['class'] = 'form-control'
		self.fields['telefone_banco'].widget.attrs['placeholder'] = 'Digite o telefone do banco'

