#-*- coding: utf-8 -*-
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

from apps.default.models import *
from .models import * # MODELS
from apps.subclasses.usuario.passageiro.models import *
from .forms import ClienteRegisterForm
from apps.default.forms import PhoneForm, UserRegisterForm
from apps.default.views import JSONResponseMixin
from apps.subclasses.usuario.emissor.views import get_emissor


class ClienteRegister(JSONResponseMixin,View):
	def get(self, request):
		form = UserRegisterForm()
		form.fields['password'].required = False
		form_cliente = ClienteRegisterForm()
		formset = formset_factory(PhoneForm)
		request.session["view"]="cliente"
		context = {'form':form, 'form_cliente':form_cliente, 'formset':formset}
		return render (request, 'subclasses/usuario/cliente/register.html', context)

	def post(self, request, *args, **kwargs):
		form = UserRegisterForm(request.POST, request.FILES)
		form_cliente = ClienteRegisterForm(request.POST, request.FILES)
		form.fields['password'].required = False
		PhoneFormSet = formset_factory(PhoneForm)		
		formset = PhoneFormSet(request.POST, request.FILES)
		request.session["view"]="cliente"
		try:
			request.POST['data_nascimento'] = datetime.strptime(request.POST['data_prevista'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		try:
			request.POST['dt_emissao_rg'] = datetime.strptime(request.POST['dt_emissao_rg'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass

		try:
			request.POST['dt_admissao'] = datetime.strptime(request.POST['dt_admissao'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		try:
			request.POST['dt_banco'] = datetime.strptime(request.POST['dt_banco'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		if form.is_valid() and formset.is_valid() and form_cliente.is_valid():
			usuario = form.save(commit=False)
			cliente = form_cliente.save(commit=False)

			emissor = get_emissor(self)

			if form.cleaned_data.get("cep") :
				id_logradouro = Logradouro()
				id_logradouro.cep = form.cleaned_data.get("cep")
				id_logradouro.nome = form.cleaned_data.get("rua")
				id_logradouro.bairro = form.cleaned_data.get("bairro")
				id_logradouro.cidade = form.cleaned_data.get("cidade")
				id_logradouro.estado = form.cleaned_data.get("estado")
				id_logradouro.pais = form.cleaned_data.get("pais")
				id_logradouro.save()

				id_endereco = Endereco()
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = form.cleaned_data.get("numero")
				id_endereco.complemento = form.cleaned_data.get("complemento",None)
				id_endereco.pontoreferencia = form.cleaned_data.get("pontoreferencia",None)
				id_endereco.save()
			else:
				id_endereco = None

			if form_cliente.cleaned_data.get("cep_empresa_cliente"):
				id_logradouro_empresa = Logradouro()
				id_logradouro_empresa.cep = form_cliente.cleaned_data.get("cep_empresa_cliente")
				id_logradouro_empresa.nome = form_cliente.cleaned_data.get("rua_empresa")
				id_logradouro_empresa.bairro = form_cliente.cleaned_data.get("bairro_empresa")
				id_logradouro_empresa.cidade = form_cliente.cleaned_data.get("cidade_empresa")
				id_logradouro_empresa.estado = form_cliente.cleaned_data.get("estado_empresa")
				id_logradouro_empresa.pais = form_cliente.cleaned_data.get("pais_empresa")
				id_logradouro_empresa.save()

				id_endereco_empresa = Endereco()
				id_endereco_empresa.id_logradouro = id_logradouro_empresa
				id_endereco_empresa.numero = form_cliente.cleaned_data.get("numero_empresa")
				id_endereco_empresa.complemento = form_cliente.cleaned_data.get("complemento_empresa",None)
				id_endereco_empresa.pontoreferencia = form_cliente.cleaned_data.get("pontoreferencia_empresa",None)
				id_endereco_empresa.save()
			else:
				id_endereco_empresa = None

			usuario.id_endereco = id_endereco
			usuario.is_active = True
			usuario.id_tipo_usuario = TipoUsuario.objects.get_or_create(descricao="CLIENTE")[0]
			usuario.nomecompleto = form.cleaned_data.get("nome")
			usuario.save()

			for  f  in formset:
				phone = f.cleaned_data
				if phone:
					teluser = TelefoneUsuario()
					teluser.id_tipo_telefone =  phone.get('tipo_telefone')
					teluser.id_usuario = usuario
					teluser.numero =  phone.get('numero')
					teluser.save()

			cliente.usuario = usuario
			cliente.id_endereco_empresa = id_endereco_empresa
			if emissor:
				cliente.id_emissor = emissor
				cliente.id_agencia = emissor.id_agencia
			cliente.save()

			passageiro = Passageiro()
			passageiro.id_usuario = cliente.usuario
			if emissor:
				passageiro.id_emissor = cliente.id_emissor
				passageiro.id_agencia = cliente.id_agencia
			passageiro.nome_pai = cliente.nome_pai
			passageiro.nome_mae = cliente.nome_mae
			passageiro.naturalidade = cliente.naturalidade
			passageiro.save()

			return redirect(reverse_lazy("cliente-list"))
		
		context = {'form':form, 'form_cliente':form_cliente, 'formset':formset}
		return render(request, 'subclasses/usuario/cliente/register.html', context)


class ClienteEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		cliente = Cliente.objects.get(pk=pk)
		usuario = Usuario.objects.get(pk=cliente.usuario.pk)
		telefones = TelefoneUsuario.objects.filter(id_usuario=cliente.usuario.pk).extra(select={'tipo_telefone': 'id_tipo_telefone_id'}).values('tipo_telefone', 'numero')
		extra = 1

		form = UserRegisterForm(instance=usuario)		
		form.fields['password'].required = False
		form.initial['cep'] = usuario.id_endereco.id_logradouro.cep if usuario.id_endereco else ''
		form.initial['rua'] = usuario.id_endereco.id_logradouro.nome if usuario.id_endereco else ''
		form.initial['bairro'] = usuario.id_endereco.id_logradouro.bairro if usuario.id_endereco else ''
		form.initial['cidade'] = usuario.id_endereco.id_logradouro.cidade if usuario.id_endereco else ''
		form.initial['estado'] = usuario.id_endereco.id_logradouro.estado if usuario.id_endereco else ''
		form.initial['pais'] = usuario.id_endereco.id_logradouro.pais if usuario.id_endereco else ''
		form.initial['numero'] = usuario.id_endereco.numero if usuario.id_endereco else ''
		form.initial['complemento'] = usuario.id_endereco.complemento if usuario.id_endereco else ''
		form.initial['pontoreferencia'] = usuario.id_endereco.pontoreferencia if usuario.id_endereco else ''

		form_cliente = ClienteRegisterForm(instance=cliente)
		form_cliente.initial['cep_empresa_cliente'] = cliente.id_endereco_empresa.id_logradouro.cep if cliente.id_endereco_empresa else ''
		form_cliente.initial['rua_empresa'] = cliente.id_endereco_empresa.id_logradouro.nome if cliente.id_endereco_empresa else ''
		form_cliente.initial['bairro_empresa'] = cliente.id_endereco_empresa.id_logradouro.bairro if cliente.id_endereco_empresa else ''
		form_cliente.initial['cidade_empresa'] = cliente.id_endereco_empresa.id_logradouro.cidade if cliente.id_endereco_empresa else ''
		form_cliente.initial['estado_empresa'] = cliente.id_endereco_empresa.id_logradouro.estado if cliente.id_endereco_empresa else ''
		form_cliente.initial['pais_empresa'] = cliente.id_endereco_empresa.id_logradouro.pais if cliente.id_endereco_empresa else ''
		form_cliente.initial['numero_empresa'] = cliente.id_endereco_empresa.numero if cliente.id_endereco_empresa else ''
		form_cliente.initial['complemento_empresa'] = cliente.id_endereco_empresa.complemento if cliente.id_endereco_empresa else ''
		form_cliente.initial['pontoreferencia_empresa'] = cliente.id_endereco_empresa.pontoreferencia if cliente.id_endereco_empresa else ''

		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(initial=telefones)

		request.session["view"]="cliente"
		context = {'form':form, 'form_cliente':form_cliente, 'formset':formset}
		return render(request, 'subclasses/usuario/cliente/edit.html', context)

	def post(self, request, pk, *args, **kwargs):
		cliente = Cliente.objects.get(pk=pk)
		try:
			passageiro = Passageiro.objects.get(id_usuario=cliente.usuario)
		except:
			passageiro = Passageiro()
			
		user = Usuario.objects.get(pk=cliente.usuario.pk)
		telefones = TelefoneUsuario.objects.filter(id_usuario=user.pk)
		extra = 1
		form = UserRegisterForm(request.POST, request.FILES, instance=user)
		form_cliente = ClienteRegisterForm(request.POST, request.FILES,instance=cliente)
		form.fields['password'].required = False
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(request.POST, request.FILES)
		request.session["view"]="cliente"
		try:
			request.POST['data_nascimento'] = datetime.strptime(request.POST['data_prevista'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		try:
			request.POST['dt_emissao_rg'] = datetime.strptime(request.POST['dt_emissao_rg'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass

		try:
			request.POST['dt_admissao'] = datetime.strptime(request.POST['dt_admissao'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		try:
			request.POST['dt_banco'] = datetime.strptime(request.POST['dt_banco'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		if form.is_valid() and formset.is_valid() and form_cliente.is_valid():
			usuario = form.save(commit=False)
			cliente = form_cliente.save(commit=False)

			emissor = get_emissor(self)
			
			if user.id_endereco:
				id_endereco = Endereco.objects.get(pk=user.id_endereco.pk)
				id_logradouro = Logradouro.objects.get(pk=id_endereco.id_logradouro.pk)
			else:
				id_endereco = Endereco()
				id_logradouro = Logradouro()

			if form.cleaned_data.get("cep") :
				id_logradouro.cep = form.cleaned_data.get("cep")
				id_logradouro.nome = form.cleaned_data.get("rua")
				id_logradouro.bairro = form.cleaned_data.get("bairro")
				id_logradouro.cidade = form.cleaned_data.get("cidade")
				id_logradouro.estado = form.cleaned_data.get("estado")
				id_logradouro.pais = form.cleaned_data.get("pais")
				id_logradouro.save()

				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = form.cleaned_data.get("numero")
				id_endereco.complemento = form.cleaned_data.get("complemento",None)
				id_endereco.pontoreferencia = form.cleaned_data.get("pontoreferencia",None)
				id_endereco.save()
			else:
				id_endereco = None

			if cliente.id_endereco_empresa:
				id_endereco_empresa = Endereco.objects.get(pk=cliente.id_endereco_empresa.pk)
				id_logradouro_empresa = Logradouro.objects.get(pk=id_endereco_empresa.id_logradouro.pk)
			else:
				id_endereco_empresa = Endereco()
				id_logradouro_empresa = Logradouro()

			if form_cliente.cleaned_data.get("cep_empresa_cliente") :
				id_logradouro_empresa.cep = form_cliente.cleaned_data.get("cep_empresa_cliente")
				id_logradouro_empresa.nome = form_cliente.cleaned_data.get("rua_empresa")
				id_logradouro_empresa.bairro = form_cliente.cleaned_data.get("bairro_empresa")
				id_logradouro_empresa.cidade = form_cliente.cleaned_data.get("cidade_empresa")
				id_logradouro_empresa.estado = form_cliente.cleaned_data.get("estado_empresa")
				id_logradouro_empresa.pais = form_cliente.cleaned_data.get("pais_empresa")
				id_logradouro_empresa.save()

				id_endereco_empresa.id_logradouro = id_logradouro_empresa
				id_endereco_empresa.numero = form_cliente.cleaned_data.get("numero_empresa")
				id_endereco_empresa.complemento = form_cliente.cleaned_data.get("complemento_empresa",None)
				id_endereco_empresa.pontoreferencia = form_cliente.cleaned_data.get("pontoreferencia_empresa",None)
				id_endereco_empresa.save()
			else:
				id_endereco_empresa = None

			usuario.id_endereco = id_endereco
			usuario.is_active = True
			usuario.id_tipo_usuario = TipoUsuario.objects.get_or_create(descricao="CLIENTE")[0]
			usuario.nomecompleto = form.cleaned_data.get("nome")
			usuario.save()

			for telefone in telefones:
				telefone.delete()

			for  f  in formset:
				phone = f.cleaned_data
				if phone:
					teluser = TelefoneUsuario()
					teluser.id_tipo_telefone =  phone.get('tipo_telefone')
					teluser.id_usuario = usuario
					teluser.numero =  phone.get('numero')
					teluser.save()

			cliente.usuario = usuario
			cliente.id_endereco_empresa = id_endereco_empresa
			if emissor:
				cliente.id_emissor = emissor
				cliente.id_agencia = emissor.id_agencia
			cliente.save()

			passageiro.id_usuario = cliente.usuario
			if emissor:
				passageiro.id_emissor = cliente.id_emissor
				passageiro.id_agencia = cliente.id_agencia
			passageiro.nome_pai = cliente.nome_pai
			passageiro.nome_mae = cliente.nome_mae
			passageiro.naturalidade = cliente.naturalidade
			passageiro.save()

			return redirect(reverse_lazy("cliente-list"))

		context = {'form':form, 'form_cliente':form_cliente, 'formset':formset}
		return render(request, 'subclasses/usuario/cliente/edit.html', context)



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

		emissor = get_emissor(self)
		if emissor:
			clientes = Cliente.objects.filter(id_agencia=emissor.id_agencia.pk)
		else:
			clientes = Cliente.objects.all()

		object_list = []
		for cliente in clientes:
			telefones = TelefoneUsuario.objects.filter(id_usuario=cliente.usuario)
			object_list.append({'cliente':cliente, 'telefones':telefones})

		context['object_list'] = object_list
		
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

