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

	nome_pai = forms.CharField(label='Nome do Pai:', max_length=45, required=False)
	nome_mae = forms.CharField(label='Nome da Mãe:', max_length=45, required=False)
	naturalidade = forms.CharField(label='Naturalidade:', max_length=45, required=False)
	numero_dependentes = forms.IntegerField(label='Numero de Dependentes:', required=False)
	tipo_residencia = forms.CharField(label='Tipo da Residência:', max_length=45, required=False)
	dt_emissao_rg = forms.DateField(label='Data emissão RG:',input_formats=settings.DATE_INPUT_FORMATS, required=False)
	tempo_residencia = forms.CharField(label='Tempo de residência:', max_length=45, required=False)
	empresa = forms.CharField(label='Nome da Empresa:', max_length=45, required=False)
	telefone_empresa = forms.CharField(label='Telefone da Empresa:', max_length=45, required=False)
	dt_admissao = forms.CharField(label='Data de admissão:', required=False)
	cargo = forms.CharField(label='Cargo ou Função:', max_length=45, required=False)
	principal_renda = forms.CharField(label='Renda Principal:', max_length=45, required=False)
	outra_renda = forms.CharField(label='Outras Rendas:', max_length=45, required=False)
	patrimonio = forms.CharField(label='Patrimonio:', max_length=45, required=False)
	banco = forms.CharField(label='Banco onde tem conta:', max_length=45, required=False)
	agencia = forms.CharField(label='Agência:', max_length=45, required=False)
	conta = forms.CharField(label='Conta:', max_length=45, required=False)
	dt_banco = forms.DateField(label='Cliente do bancos desde:',input_formats=settings.DATE_INPUT_FORMATS, required=False)
	telefone_banco = forms.CharField(label='Telefone do banco:', max_length=45, required=False)
	cnpj_empresa = forms.CharField(label='CNPJ da Empresa:', max_length=45, required=False)

	#Dados Empresa
	cep_empresa_cliente = forms.CharField(label='CEP:', max_length=45, required=False)
	pais_empresa = forms.CharField(label='País:', max_length=45, required=False)
	estado_empresa = forms.CharField(label='Estado:', max_length=45, required=False)
	cidade_empresa = forms.CharField(label='Cidade', max_length=45, required=False)
	rua_empresa = forms.CharField(label='Rua:', max_length=45, required=False)
	bairro_empresa = forms.CharField(label='Bairro:', max_length=45, required=False)
	complemento_empresa = forms.CharField(label='Complemento:', max_length=45, required=False)
	pontoreferencia_empresa = forms.CharField(label='Ponto de Referência:', max_length=45, required=False)
	numero_empresa =  forms.CharField(label='Número:', max_length=45, required=False)

	def __init__(self, *args, **kwargs):
		super(ClienteRegisterForm, self).__init__(*args, **kwargs)

		self.fields['nome_pai'].widget.attrs['class'] = 'form-control'
		self.fields['nome_pai'].widget.attrs['placeholder'] = 'Nome do Pai'
		self.fields['nome_mae'].widget.attrs['class'] = 'form-control'
		self.fields['nome_mae'].widget.attrs['placeholder'] = 'Nome da Mãe'
		self.fields['naturalidade'].widget.attrs['class'] = 'form-control'
		self.fields['naturalidade'].widget.attrs['placeholder'] = 'Naturalidade'
		self.fields['tipo_residencia'].widget.attrs['class'] = 'form-control'
		self.fields['tipo_residencia'].widget.attrs['placeholder'] = 'Tipo da Residência'
		self.fields['numero_dependentes'].widget.attrs['class'] = 'form-control input-number'
		self.fields['numero_dependentes'].widget.attrs['placeholder'] = 'Numero de Dependentes'
		self.fields['dt_emissao_rg'].widget.attrs['class'] = 'form-control'
		self.fields['dt_emissao_rg'].widget.attrs['placeholder'] = 'Digite a data de emissão do RG'
		self.fields['tempo_residencia'].widget.attrs['class'] = 'form-control'
		self.fields['tempo_residencia'].widget.attrs['placeholder'] = 'Digite o tempo de residência'
		self.fields['empresa'].widget.attrs['class'] = 'form-control'
		self.fields['empresa'].widget.attrs['placeholder'] = 'Digite o nome da empresa'
		self.fields['telefone_empresa'].widget.attrs['class'] = 'form-control input-number'
		self.fields['telefone_empresa'].widget.attrs['placeholder'] = 'Digite o telefone da empresa'
		self.fields['dt_admissao'].widget.attrs['class'] = 'form-control'
		self.fields['dt_admissao'].widget.attrs['placeholder'] = 'Digite a data de adminissão'
		self.fields['cargo'].widget.attrs['class'] = 'form-control'
		self.fields['cargo'].widget.attrs['placeholder'] = 'Digite o cargo'
		self.fields['principal_renda'].widget.attrs['class'] = 'form-control input-number'
		self.fields['principal_renda'].widget.attrs['placeholder'] = 'Digite o valor da reda principal'
		self.fields['outra_renda'].widget.attrs['class'] = 'form-control input-number'
		self.fields['outra_renda'].widget.attrs['placeholder'] = 'Digite o valor de outras rendas'
		self.fields['patrimonio'].widget.attrs['class'] = 'form-control input-number'
		self.fields['patrimonio'].widget.attrs['placeholder'] = 'Digite o valor do patrimonio'
		self.fields['banco'].widget.attrs['class'] = 'form-control'
		self.fields['banco'].widget.attrs['placeholder'] = 'Digite o numero do banco'
		self.fields['agencia'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['placeholder'] = 'Digite a agência'
		self.fields['conta'].widget.attrs['class'] = 'form-control'
		self.fields['conta'].widget.attrs['placeholder'] = 'Digite o numero da conta'
		self.fields['dt_banco'].widget.attrs['class'] = 'form-control'
		self.fields['dt_banco'].widget.attrs['placeholder'] = 'Digite a data aproximada de inicio da conta'
		self.fields['telefone_banco'].widget.attrs['class'] = 'form-control input-number'
		self.fields['telefone_banco'].widget.attrs['placeholder'] = 'Digite o telefone do banco'
		self.fields['cnpj_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['cnpj_empresa'].widget.attrs['placeholder'] = 'CNPJ da Empresa'

		#Empresa
		self.fields['cep_empresa_cliente'].widget.attrs['class'] = 'form-control'
		self.fields['cep_empresa_cliente'].widget.attrs['placeholder'] = 'CEP'
		self.fields['cep_empresa_cliente'].widget.attrs['onblur'] = 'get_cep_data_empresa(this.value)'
		self.fields['bairro_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['bairro_empresa'].widget.attrs['placeholder'] = 'Bairro'
		self.fields['rua_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['rua_empresa'].widget.attrs['placeholder'] = 'Rua'
		self.fields['cidade_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['cidade_empresa'].widget.attrs['placeholder'] = 'Cidade'
		self.fields['estado_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['estado_empresa'].widget.attrs['placeholder'] = 'Estado'
		self.fields['pais_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['pais_empresa'].widget.attrs['placeholder'] = 'País'
		self.fields['complemento_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['complemento_empresa'].widget.attrs['placeholder'] = 'Complemento'
		self.fields['pontoreferencia_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['pontoreferencia_empresa'].widget.attrs['placeholder'] = 'Ponto de Referência'
		self.fields['numero_empresa'].widget.attrs['class'] = 'form-control'
		self.fields['numero_empresa'].widget.attrs['placeholder'] = 'Número'
