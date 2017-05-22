#-*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from apps.default.forms import UserRegisterForm
from .models import Cliente

class ClienteRegisterForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = '__all__'

	
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
		self.fields['usuario'].required = False
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
		self.fields['telefone'].widget.attrs['class'] = 'form-control input-number'
		self.fields['telefone'].widget.attrs['placeholder'] = 'Digite o telefone da empresa'
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


		self.fields['nome_pai'].label = "Nome do Pai"
		self.fields['nome_mae'].label = "Nome do Mãe"
		self.fields['numero_dependentes'].label = "Numero de Dependentes"
		self.fields['tipo_residencia'].label = "Tipo de Residência"
		self.fields['tempo_residencia'].label = "Tempo de Residência"
		self.fields['dt_admissao'].label = "Data de Admissão"
		self.fields['dt_emissao_rg'].label = "Data de Admissão RG"
		self.fields['dt_banco'].label = "Data de Criação da Conta"
		self.fields['telefone_banco'].label = "Telefone do Banco"

	def clean(self):
		cleaned_data = super(ClienteRegisterForm, self).clean()

		cep = cleaned_data.get("cep_empresa_cliente")
		rua = cleaned_data.get("rua_empresa")
		bairro = cleaned_data.get("bairro_empresa")
		cidade = cleaned_data.get("cidade_empresa")
		estado = cleaned_data.get("estado_empresa")
		pais = cleaned_data.get("pais_empresa")
		numero = cleaned_data.get("numero_empresa")


		msg = "Este campo é obrigatório."
		if cep:
		    if not rua:
		        self.add_error('rua_empresa', msg)
		    if not bairro:
		        self.add_error('bairro_empresa', msg)
		    if not cidade:
		        self.add_error('cidade_empresa', msg)
		    if not estado:
		        self.add_error('estado_empresa', msg)
		    if not pais:
		        self.add_error('pais_empresa', msg)
		    if not numero:
		        self.add_error('numero_empresa', msg)
		elif rua:
		    if not rua:
		        self.add_error('rua_empresa', msg)
		    if not bairro:
		        self.add_error('bairro_empresa', msg)
		    if not cidade:
		        self.add_error('cidade_empresa', msg)
		    if not estado:
		        self.add_error('estado_empresa', msg)
		    if not pais:
		        self.add_error('pais_empresa', msg)
		    if not numero:
		        self.add_error('numero_empresa', msg)
		elif bairro:
		    if not cep:
		        self.add_error('cep_empresa_cliente', msg)
		    if not rua:
		        self.add_error('rua_empresa', msg)
		    if not cidade:
		        self.add_error('cidade_empresa', msg)
		    if not estado:
		        self.add_error('estado_empresa', msg)
		    if not pais:
		        self.add_error('pais_empresa', msg)
		    if not numero:
		        self.add_error('numero_empresa', msg)
		elif cidade:
		    if not cep:
		        self.add_error('cep_empresa_cliente', msg)
		    if not rua:
		        self.add_error('rua_empresa', msg)
		    if not bairro:
		        self.add_error('bairro_empresa', msg)
		    if not estado:
		        self.add_error('estado_empresa', msg)
		    if not pais:
		        self.add_error('pais_empresa', msg)
		    if not numero:
		        self.add_error('numero_empresa', msg)
		elif estado:
		    if not cep:
		        self.add_error('cep_empresa_cliente', msg)
		    if not rua:
		        self.add_error('rua_empresa', msg)
		    if not bairro:
		        self.add_error('bairro_empresa', msg)
		    if not cidade:
		        self.add_error('cidade_empresa', msg)
		    if not pais:
		        self.add_error('pais_empresa', msg)
		    if not numero:
		        self.add_error('numero_empresa', msg)
		elif pais:
		    if not cep:
		        self.add_error('cep_empresa_cliente', msg)
		    if not rua:
		        self.add_error('rua_empresa', msg)
		    if not bairro:
		        self.add_error('bairro_empresa', msg)
		    if not cidade:
		        self.add_error('cidade_empresa', msg)
		    if not estado:
		        self.add_error('estado_empresa', msg)
		    if not numero:
		        self.add_error('numero_empresa', msg)
		elif numero:
		    if not cep:
		        self.add_error('cep_empresa_cliente', msg)
		    if not rua:
		        self.add_error('rua_empresa', msg)
		    if not bairro:
		        self.add_error('bairro_empresa', msg)
		    if not cidade:
		        self.add_error('cidade_empresa', msg)
		    if not estado:
		        self.add_error('estado_empresa', msg)
		    if not pais:
		        self.add_error('pais_empresa', msg)