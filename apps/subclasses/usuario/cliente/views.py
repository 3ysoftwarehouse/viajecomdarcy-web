#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import (HttpResponse,
                         HttpResponseForbidden,
                         HttpResponseBadRequest)
from django.forms import formset_factory
from datetime import datetime
##################################################



##################################################
#				CUSTOM IMPORTS                   #
##################################################
from apps.default.models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneUsuario, TipoUsuario, Genero # MODELS
from .models import Cliente # MODELS
from .forms import ClienteRegisterForm
from apps.default.forms import PhoneForm # PHONE FORMS
from apps.default.views import JSONResponseMixin
from apps.subclasses.usuario.emissor.views import get_emissor
##################################################



'''
----------------------------------------
			CLIENTE METHODS
----------------------------------------
''' 

class ClienteRegister(JSONResponseMixin,View):
	
	def get(self, request):
		form = ClienteRegisterForm
		formset = formset_factory(PhoneForm)
		request.session["view"]="cliente"
		return render (request, 'subclasses/usuario/cliente/register.html', {'form':form, 'formset':formset})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = ClienteRegisterForm(request.POST,request.FILES)
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)

			emissor = get_emissor(self)
			
			nome = request.POST['nome']
			sobrenome = ''
			email = request.POST['email']
			password = request.POST['password']
			genero = request.POST['genero']
			data_nascimento = request.POST['data_nascimento']
			cpf = request.POST['cpf']
			rg = request.POST['rg']
			orgaoemissor = request.POST['orgaoemissor']
			foto = request.FILES.get('foto', None)

			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numero = request.POST['numero']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']

			# EXTRAS
			
			nome_mae = request.POST['nome_mae']
			nome_pai = request.POST['nome_pai']
			naturalidade = request.POST['naturalidade']
			numero_dependentes = request.POST['numero_dependentes']
			tipo_residencia = request.POST['tipo_residencia']
			dt_emissao_rg = request.POST['dt_emissao_rg']
			tempo_residencia = request.POST['tempo_residencia']
			empresa = request.POST['empresa']
			telefone_empresa = request.POST['telefone_empresa']
			dt_admissao = request.POST['dt_admissao']
			cargo = request.POST['cargo']
			principal_renda = request.POST['principal_renda']
			outra_renda = request.POST['outra_renda']
			patrimonio = request.POST['patrimonio']
			banco = request.POST['banco']
			agencia = request.POST['agencia']
			conta = request.POST['conta']
			dt_banco = request.POST['dt_banco']
			telefone_banco = request.POST['telefone_banco']
			cnpj_empresa = request.POST['cnpj_empresa']
			

			cep_empresa_cliente = request.POST['cep_empresa_cliente']
			rua_empresa = request.POST['rua_empresa']
			cidade_empresa = request.POST['cidade_empresa']
			bairro_empresa = request.POST['bairro_empresa']
			estado_empresa = request.POST['estado_empresa']
			pais_empresa = request.POST['pais_empresa']
			numero_empresa = request.POST['numero_empresa']
			complemento_empresa = request.POST['complemento_empresa']
			pontoreferencia_empresa = request.POST['pontoreferencia_empresa']


			if data_nascimento:
				data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')
			else:
				data_nascimento = None

			if dt_emissao_rg:
				dt_emissao_rg = datetime.strptime(dt_emissao_rg, '%d/%m/%Y').strftime('%Y-%m-%d')
			else:
				dt_emissao_rg = None

			if dt_admissao:				
				dt_admissao = datetime.strptime(dt_admissao, '%d/%m/%Y').strftime('%Y-%m-%d')
			else:
				dt_admissao = None

			if dt_banco:
				dt_banco = datetime.strptime(dt_banco, '%d/%m/%Y').strftime('%Y-%m-%d')
			else:
				dt_banco = None	

			if not nome:
				context['error_msg'] = 'nome cannot be empty !'
			else:
				nomeSeparado = nome.split(" ", 1)
				try:
					sobrenome =  nomeSeparado[1]
				except:
					sobrenome = ' '
			if not email:
				context['error_msg'] = 'email cannot be empty !'
			if not password:
				context['error_msg'] = 'password cannot be empty !'
			if not genero:
				context['error_msg'] = 'genero cannot be empty !'
			if not data_nascimento:
				context['error_msg'] = 'data_nascimento cannot be empty !'
			if not cpf:
				context['error_msg'] = 'cpf cannot be empty !'
			if not rg:
				context['error_msg'] = 'rg cannot be empty !'
			if not orgaoemissor:
				context['error_msg'] = 'orgaoemissor cannot be empty !'
			'''
			if not foto:
				context['error_msg'] = 'foto cannot be empty !'
			'''
			if not cep:
				context['error_msg'] = 'cep cannot be empty !'
			if not rua:
				context['error_msg'] = 'rua cannot be empty !'
			if not bairro:
				context['error_msg'] = 'bairro cannot be empty !'
			if not cidade:
				context['error_msg'] = 'cidade cannot be empty !'
			if not estado:
				context['error_msg'] = 'estado cannot be empty !'
			if not pais:
				context['error_msg'] = 'pais cannot be empty !'
			if not numero:
				context['error_msg'] = 'numero cannot be empty !'


			# EXTRAS
			'''
			if not dt_emissao_rg:
				context['error_msg'] = 'dt_emissao_rg cannot be empty !'
			if not tempo_residencia:
				context['error_msg'] = 'tempo_residencia cannot be empty !'
			if not empresa:
				context['error_msg'] = 'empresa cannot be empty !'
			if not cep_empresa:
				context['error_msg'] = 'cep_empresa cannot be empty !'
			if not endereco_empresa:
				context['error_msg'] = 'endereco_empresa cannot be empty !'
			if not telefone_empresa:
				context['error_msg'] = 'telefone_empresa cannot be empty !'
			if not dt_admissao:
				context['error_msg'] = 'dt_admissao cannot be empty !'
			if not cargo:
				context['error_msg'] = 'cargo cannot be empty !'
			if not principal_renda:
				context['error_msg'] = 'principal_renda cannot be empty !'
			if not outra_renda:
				context['error_msg'] = 'outra_renda cannot be empty !'
			if not patrimonio:
				context['error_msg'] = 'patrimonio cannot be empty !'
			if not banco:
				context['error_msg'] = 'banco cannot be empty !'
			if not agencia:
				context['error_msg'] = 'agencia cannot be empty !'
			if not conta:
				context['error_msg'] = 'conta cannot be empty !'
			if not dt_banco:
				context['error_msg'] = 'dt_banco cannot be empty !'
			if not telefone_banco:
				context['error_msg'] = 'telefone_banco cannot be empty !'
			'''
			
			if not numero_dependentes:
				numero_dependentes = 0

			listphones = []

			if formset.is_valid():
				for f in formset:
					phone = f.cleaned_data
					listphones.append([phone.get('tipo_telefone'),phone.get('numero')])

					if not phone.get('tipo_telefone'):
						context['Tipo Telefone'] = ' cannot be empty !'
					if not phone.get('numero'):
						context['Numero'] = ' cannot be empty !'
			else:
				for erro in formset.errors:					
					context['error'] = erro
				pass

			if not context:

				id_logradouro = Logradouro()
				id_logradouro.cep = cep
				id_logradouro.nome = rua
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.save()

				id_endereco = Endereco()
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numero
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				if cep_empresa_cliente:

					id_logradouro_empresa = Logradouro()
					id_logradouro_empresa.cep = cep_empresa_cliente
					id_logradouro_empresa.nome = rua_empresa
					id_logradouro_empresa.bairro = bairro_empresa
					id_logradouro_empresa.cidade = cidade_empresa
					id_logradouro_empresa.estado = estado_empresa
					id_logradouro_empresa.pais = pais_empresa
					id_logradouro_empresa.save()

					id_endereco_empresa = Endereco()
					id_endereco_empresa.id_logradouro = id_logradouro_empresa
					id_endereco_empresa.numero = numero_empresa
					id_endereco_empresa.complemento = complemento_empresa
					id_endereco_empresa.pontoreferencia = pontoreferencia_empresa
					id_endereco_empresa.save()
				else:
					id_endereco_empresa = None


				usuario = Usuario.objects.create_user(email, password)				
				usuario.nome = nomeSeparado[0]
				usuario.sobrenome = sobrenome
				usuario.nomecompleto = nomeSeparado[0] +" "+sobrenome
				try:
					tipo_usuario = TipoUsuario.objects.get(descricao__icontains='CLIENTE')
				except:
					tipo_usuario = TipoUsuario.objects.create(descricao="CLIENTE")
				usuario.id_tipo_usuario = tipo_usuario
				usuario.id_genero = Genero.objects.get(pk=genero)
				usuario.data_nascimento = data_nascimento
				usuario.cpf = cpf
				usuario.rg = rg
				usuario.orgaoemissor = orgaoemissor
				usuario.foto = foto
				usuario.id_endereco = id_endereco
				usuario.is_active =  False
				usuario.save()

				for listphone in listphones:
					id_tipo_telefone = TipoTelefone.objects.filter(descricao=listphone[0])[0]			
					teluser = TelefoneUsuario()
					teluser.id_tipo_telefone = id_tipo_telefone
					teluser.id_usuario = usuario
					teluser.numero = listphone[1]
					teluser.save()

				cliente = Cliente()
				cliente.nome_pai = nome_pai
				cliente.nome_mae = nome_mae
				cliente.tipo_residencia = tipo_residencia
				cliente.naturalidade = naturalidade
				cliente.numero_dependentes = numero_dependentes
				cliente.usuario = usuario
				cliente.dt_emissao_rg = dt_emissao_rg
				cliente.tempo_residencia = tempo_residencia
				cliente.empresa = empresa
				cliente.telefone = telefone_empresa
				cliente.dt_admissao = dt_admissao
				cliente.cargo = cargo
				cliente.principal_renda = principal_renda
				cliente.outra_renda = outra_renda
				cliente.patrimonio = patrimonio
				cliente.banco = banco
				cliente.agencia = agencia
				cliente.conta = conta
				cliente.dt_banco = dt_banco
				cliente.telefone_banco = telefone_banco
				cliente.id_endereco_empresa = id_endereco_empresa
				cliente.cnpj_empresa = cnpj_empresa
				if emissor:
					cliente.id_emissor = emissor
					cliente.id_agencia = emissor.id_agencia
				cliente.save()

				return redirect(reverse_lazy("cliente-list"))

			else:
				form = ClienteRegisterForm(request.POST,request.FILES)
				PhoneFormSet = formset_factory(PhoneForm)		
				formset = PhoneFormSet(request.POST, request.FILES)

		return render(request, 'subclasses/usuario/cliente/register.html', {'form': form, 'formset':formset, 'context': context})


class ClienteEdit(JSONResponseMixin,View):
	def get(self, request, pk=None):
		cliente = Cliente.objects.get(pk=pk)
		usuario = Usuario.objects.get(pk=cliente.usuario.pk)
		id_endereco = Endereco.objects.get(pk=usuario.id_endereco.pk)
		id_logradouro = Logradouro.objects.get(pk=id_endereco.id_logradouro.pk)

		telefones = TelefoneUsuario.objects.filter(id_usuario=usuario.pk)
		PhoneFormSet = formset_factory(PhoneForm,extra=0)
		
		data = []
		for telefone in telefones:
			data.append({'tipo_telefone':telefone.id_tipo_telefone,'numero':telefone.numero})
		
				
		formset = PhoneFormSet(
			initial=data
			)

		form = ClienteRegisterForm(
			initial={
			'nome': usuario.nomecompleto,
			'sobrenome': usuario.sobrenome,
			'email': usuario.email,			
			'genero' : usuario.id_genero,
			'data_nascimento' : usuario.data_nascimento,
			'cpf' : usuario.cpf,
			'rg' : usuario.rg,
			'orgaoemissor' : usuario.orgaoemissor,
			'foto' : usuario.foto,
			'cep' : id_logradouro.cep, 
			'rua' : id_logradouro.nome,
			'bairro' : id_logradouro.bairro,
			'cidade' : id_logradouro.cidade,
			'estado' : id_logradouro.estado,
			'pais' : id_logradouro.pais,
			'numero': id_endereco.numero,
			'complemento' : id_endereco.complemento,
			'pontoreferencia' : id_endereco.pontoreferencia,
			'nome_pai' : cliente.nome_pai,
			'nome_mae' : cliente.nome_mae,
			'naturalidade' : cliente.naturalidade,
			'numero_dependentes' : cliente.numero_dependentes,
			'tipo_residencia' : cliente.tipo_residencia,
			'dt_emissao_rg' : cliente.dt_emissao_rg,
			'tempo_residencia' : cliente.tempo_residencia,
			'empresa' : cliente.empresa,
			'telefone' : cliente.telefone,
			'dt_admissao' : cliente.dt_admissao,
			'cargo' : cliente.cargo,
			'principal_renda' : cliente.principal_renda,
			'outra_renda' : cliente.outra_renda,
			'patrimonio' : cliente.patrimonio,
			'banco' : cliente.banco,
			'agencia' : cliente.agencia,
			'conta' : cliente.conta,
			'dt_banco' : cliente.dt_banco,
			'telefone_banco' : cliente.telefone_banco,
			'cnpj_empresa' : cliente.cnpj_empresa,	
			}
			)
		return render (request, 'subclasses/usuario/cliente/edit.html', {'form':form,'formset':formset})

	def post(self, request, pk=None, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = ClienteRegisterForm(request.POST,request.FILES)
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)

			emissor = get_emissor(self)

			nome = request.POST['nome']
			sobrenome = ''
			email = request.POST['email']			
			genero = request.POST['genero']
			data_nascimento = request.POST['data_nascimento']
			cpf = request.POST['cpf']
			rg = request.POST['rg']
			orgaoemissor = request.POST['orgaoemissor']
			foto = request.FILES.get('foto', None)

			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numero = request.POST['numero']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']

			# EXTRAS
			dt_emissao_rg = request.POST['dt_emissao_rg']
			tempo_residencia = request.POST['tempo_residencia']
			empresa = request.POST['empresa']
			cep_empresa = request.POST['cep']
			endereco_empresa = request.POST['endereco_empresa']
			telefone_empresa = request.POST['telefone_empresa']
			dt_admissao = request.POST['dt_admissao']
			cargo = request.POST['cargo']
			principal_renda = request.POST['principal_renda']
			outra_renda = request.POST['outra_renda']
			patrimonio = request.POST['patrimonio']
			banco = request.POST['banco']
			agencia = request.POST['agencia']
			conta = request.POST['conta']
			dt_banco = request.POST['dt_banco']
			telefone_banco = request.POST['telefone_banco']

			#Empresa
			cep_empresa_cliente = request.POST['cep_empresa_cliente']
			pais_empresa = request.POST['pais_empresa']
			estado_empresa = request.POST['estado_empresa']
			cidade_empresa = request.POST['cidade_empresa']
			rua_empresa = request.POST['rua_empresa']
			bairro_empresa = request.POST['bairro_empresa']
			complemento_empresa = request.POST['complemento_empresa']
			pontoreferencia_empresa = request.POST['pontoreferencia_empresa']
			numero_empresa = request.POST['numero_empresa']

			listphones = []

			if formset.is_valid():
				for f in formset:
					phone = f.cleaned_data
					listphones.append([phone.get('tipo_telefone'),phone.get('numero')])

					if not phone.get('tipo_telefone'):
						context['Tipo Telefone'] = ' cannot be empty !'
					if not phone.get('numero'):
						context['Numero'] = ' cannot be empty !'
			else:
				for erro in formset.errors:					
					context['error'] = erro
				pass

			
			if not nome:
				context['Nome'] = ' cannot be empty !'
			else:
				nomeSeparado = nome.split(" ", 1)
				try:
					sobrenome =  nomeSeparado[1]
				except:
					sobrenome = ' '
			if not email:
				context['E-mail'] = ' cannot be empty !'			
			if not genero:
				context['Genero'] = ' cannot be empty !'
			if not data_nascimento:
				context['Data de nascimento'] = ' cannot be empty !'
			if not cpf:
				context['CPF'] = ' cannot be empty !'
			if not rg:
				context['RG'] = ' cannot be empty !'
			if not orgaoemissor:
				context['Orgão'] = ' cannot be empty !'
			'''
			if not foto:
				context['error_msg'] = 'foto cannot be empty !'
			'''
			if not cep:
				context['CEP'] = ' cannot be empty !'
			if not rua:
				context['Rua'] = ' cannot be empty !'
			if not bairro:
				context['Bairro'] = ' cannot be empty !'
			if not cidade:
				context['Cidade'] = ' cannot be empty !'
			if not estado:
				context['Estado'] = ' cannot be empty !'
			if not pais:
				context['Pais'] = ' cannot be empty !'
			if not numero:
				context['Número'] = ' cannot be empty !'
			if not complemento:
				context['Complemento'] = ' cannot be empty !'
			if not pontoreferencia:
				context['Refêrencia'] = ' cannot be empty !'

			# EXTRAS
			'''
			if not dt_emissao_rg:
				context['error_msg'] = 'dt_emissao_rg cannot be empty !'
			if not tempo_residencia:
				context['error_msg'] = 'tempo_residencia cannot be empty !'
			if not empresa:
				context['error_msg'] = 'empresa cannot be empty !'
			if not cep_empresa:
				context['error_msg'] = 'cep_empresa cannot be empty !'
			if not endereco_empresa:
				context['error_msg'] = 'endereco_empresa cannot be empty !'
			if not telefone_empresa:
				context['error_msg'] = 'telefone_empresa cannot be empty !'
			if not dt_admissao:
				context['error_msg'] = 'dt_admissao cannot be empty !'
			if not cargo:
				context['error_msg'] = 'cargo cannot be empty !'
			if not principal_renda:
				context['error_msg'] = 'principal_renda cannot be empty !'
			if not outra_renda:
				context['error_msg'] = 'outra_renda cannot be empty !'
			if not patrimonio:
				context['error_msg'] = 'patrimonio cannot be empty !'
			if not banco:
				context['error_msg'] = 'banco cannot be empty !'
			if not agencia:
				context['error_msg'] = 'agencia cannot be empty !'
			if not conta:
				context['error_msg'] = 'conta cannot be empty !'
			if not dt_banco:
				context['error_msg'] = 'dt_banco cannot be empty !'
			if not telefone_banco:
				context['error_msg'] = 'telefone_banco cannot be empty !'
			'''

			if not context:

				cliente = Cliente.objects.get(pk=pk)
				usuario = Usuario.objects.get(pk=cliente.usuario.pk)
				id_endereco = Endereco.objects.get(pk=usuario.id_endereco.pk)
				id_logradouro = Logradouro.objects.get(pk=id_endereco.id_logradouro.pk)
				id_endereco_empresa = Endereco.objects.get(pk=usuario.id_endereco.pk)
				id_logradouro_empresa = Logradouro.objects.get(pk=id_endereco.id_logradouro.pk)

				telefones = TelefoneUsuario.objects.filter(id_usuario=usuario.pk)
				for telefone in telefones:
					telefone.delete()
	
				id_logradouro.cep = cep
				id_logradouro.nome = rua
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.save()

				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numero
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				id_logradouro_empresa.cep = cep_empresa_cliente
				id_logradouro_empresa.nome = rua_empresa
				id_logradouro_empresa.bairro = bairro_empresa
				id_logradouro_empresa.cidade = cidade_empresa
				id_logradouro_empresa.estado = estado_empresa
				id_logradouro_empresa.pais = pais_empresa
				id_logradouro_empresa.save()


				id_endereco_empresa.id_logradouro = id_logradouro
				id_endereco_empresa.numero = numero_empresa
				id_endereco_empresa.complemento = complemento_empresa
				id_endereco_empresa.pontoreferencia = pontoreferencia_empresa
				id_endereco_empresa.save()

				
				usuario.nome = nomeSeparado[0]
				usuario.sobrenome = sobrenome
				usuario.nomecompleto = nomeSeparado[0] +" "+sobrenome
				try:
					tipo_usuario = TipoUsuario.objects.get(descricao__icontains='CLIENTE')
				except:
					tipo_usuario = TipoUsuario.objects.create(descricao="CLIENTE")
				usuario.id_tipo_usuario = tipo_usuario
				usuario.id_genero = Genero.objects.get(pk=genero)
				usuario.data_nascimento = data_nascimento
				usuario.cpf = cpf
				usuario.rg = rg
				usuario.orgaoemissor = orgaoemissor
				usuario.foto = foto
				usuario.id_endereco = id_endereco
				usuario.is_active =  False
				usuario.save()

				# EXTRAS
				cliente.usuario = usuario
				cliente.dt_emissao_rg = dt_emissao_rg
				cliente.tempo_residencia = tempo_residencia
				cliente.empresa = empresa
				cliente.cep = cep_empresa
				cliente.endereco = endereco_empresa
				cliente.telefone = telefone_empresa
				cliente.dt_admissao = dt_admissao
				cliente.cargo = cargo
				cliente.principal_renda = principal_renda
				cliente.outra_renda = outra_renda
				cliente.patrimonio = patrimonio
				cliente.banco = banco
				cliente.agencia = agencia
				cliente.conta = conta
				cliente.dt_banco = dt_banco
				cliente.telefone_banco = telefone_banco
				if emissor:
					cliente.id_emissor = emissor
					cliente.id_agencia = emissor.id_agencia
				cliente.save()

				for listphone in listphones:
					id_tipo_telefone = TipoTelefone.objects.filter(descricao=listphone[0])[0]			
					teluser = TelefoneUsuario()
					teluser.id_tipo_telefone = id_tipo_telefone
					teluser.id_usuario = usuario
					teluser.numero = listphone[1]
					teluser.save()

				return redirect(reverse_lazy("cliente-list"))

			else:
				form = ClienteRegisterForm(request.POST)
				PhoneFormSet = formset_factory(PhoneForm)		
				formset = PhoneFormSet(request.POST, request.FILES)

		return render (request, 'subclasses/usuario/cliente/edit.html', {'form':form ,'formset':formset,'context':context})



class ClienteList(JSONResponseMixin,ListView):
	template_name = 'subclasses/usuario/cliente/list.html'


	def get_queryset(self):
		emissor = get_emissor(self)
		if emissor:
			return Cliente.objects.filter(id_agencia=emissor.id_agencia.pk)
		else:
			return Cliente.objects.all()

	def get_context_data(self, **kwargs):
		context = super(ClienteList, self).get_context_data(**kwargs)
		return context


class ClienteDetail(JSONResponseMixin,DetailView):
	model = Cliente
	template_name = 'subclasses/usuario/cliente/detail.html'

	def get_context_data(self, **kwargs):
		context = super(ClienteDetail, self).get_context_data(**kwargs)
		return context


class ClienteDelete(JSONResponseMixin,DeleteView):
	model = Usuario
	success_url = reverse_lazy('cliente-list')
	template_name = 'subclasses/usuario/cliente/delete.html'

'''
----------------------------------------
			END CLIENTE METHODS
----------------------------------------
'''