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

from apps.default.models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneEmpresa 
from .forms import AgenciaRegisterForm
from apps.default.forms import PhoneForm 
from apps.default.views import JSONResponseMixin, validaCNPJ
from .models import Agencia



class AgenciaRegister(JSONResponseMixin,View):
	def get(self, request):
		form = AgenciaRegisterForm
		PhoneFormSet = formset_factory(PhoneForm)
		formset = PhoneFormSet()
		request.session["view"]="agencia"		
		context = {'form':form, 'formset':formset}
		return render (request, 'subclasses/empresa/agencia/register.html', context)

	def post(self, request, *args, **kwargs):
		form = AgenciaRegisterForm(request.POST, request.FILES)
		PhoneFormSet = formset_factory(PhoneForm)		
		formset = PhoneFormSet(request.POST, request.FILES)
		if form.is_valid() and formset.is_valid():
			company = form.save(commit=False)

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
				id_endereco.numero = form.cleaned_data.get("numeroed")
				id_endereco.complemento = form.cleaned_data.get("complemento",None)
				id_endereco.pontoreferencia = form.cleaned_data.get("pontoreferencia",None)
				id_endereco.save()
			else:
				id_endereco = None

			company.id_tipo_empresa =  TipoEmpresa.objects.get_or_create(descricao = "Agência")[0]
			company.id_endereco = id_endereco
			company.verificada = True
			company.save()

			for  f  in formset:
				phone = f.cleaned_data
				if phone:
					telempresa = TelefoneEmpresa()
					telempresa.id_tipo_telefone =  phone.get('tipo_telefone')
					telempresa.id_empresa = company
					telempresa.numero =  phone.get('numero')
					telempresa.ramal =  phone.get('ramal')
					telempresa.nome_contato = phone.get('nome_contato')
					telempresa.save()

			agencia = Agencia()
			agencia.id_empresa = company
			agencia.logo = request.FILES.get('logo', None)
			agencia.save()

			return redirect(reverse_lazy("agencia-list"))
		
		context = {'form':form, 'formset':formset}
		return render (request, 'subclasses/empresa/agencia/register.html', context)


class AgenciaEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		agencia = Agencia.objects.get(pk=pk)
		empresa = Empresa.objects.get(pk=agencia.id_empresa.pk)
		telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk).extra(select={'tipo_telefone': 'id_tipo_telefone_id'}).values('tipo_telefone', 'numero', 'ramal','nome_contato')
		extra = 1

		form = AgenciaRegisterForm(instance=empresa)
		form.initial['cep'] = agencia.id_empresa.id_endereco.id_logradouro.cep if agencia.id_empresa.id_endereco else ''
		form.initial['rua'] = agencia.id_empresa.id_endereco.id_logradouro.nome if agencia.id_empresa.id_endereco else ''
		form.initial['bairro'] = agencia.id_empresa.id_endereco.id_logradouro.bairro if agencia.id_empresa.id_endereco else ''
		form.initial['cidade'] = agencia.id_empresa.id_endereco.id_logradouro.cidade if agencia.id_empresa.id_endereco else ''
		form.initial['estado'] = agencia.id_empresa.id_endereco.id_logradouro.estado if agencia.id_empresa.id_endereco else ''
		form.initial['pais'] = agencia.id_empresa.id_endereco.id_logradouro.pais if agencia.id_empresa.id_endereco else ''
		form.initial['numeroed'] = agencia.id_empresa.id_endereco.numero if agencia.id_empresa.id_endereco else ''
		form.initial['complemento'] = agencia.id_empresa.id_endereco.complemento if agencia.id_empresa.id_endereco else ''
		form.initial['pontoreferencia'] = agencia.id_empresa.id_endereco.pontoreferencia if agencia.id_empresa.id_endereco else ''
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(initial=telefones)
		request.session["view"]="agencia"		
		context = {'form':form, 'formset':formset}
		return render (request, 'subclasses/empresa/agencia/edit.html', context)

	def post(self, request, pk, *args, **kwargs):
		agencia = Agencia.objects.get(pk=pk)
		empresa = Empresa.objects.get(pk=agencia.id_empresa.pk)
		telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk)
		extra = 1

		form = AgenciaRegisterForm(request.POST, request.FILES, instance=empresa)
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(request.POST)

		if form.is_valid() and formset.is_valid():
			company = form.save(commit=False)

			if empresa.id_endereco:
				id_endereco = Endereco.objects.get(pk=empresa.id_endereco.pk)
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
				id_endereco.numero = form.cleaned_data.get("numeroed")
				id_endereco.complemento = form.cleaned_data.get("complemento",None)
				id_endereco.pontoreferencia = form.cleaned_data.get("pontoreferencia",None)
				id_endereco.save()
			else:
				id_endereco = None

			company.id_tipo_empresa =  TipoEmpresa.objects.get_or_create(descricao = "Agência")[0]
			company.id_endereco = id_endereco
			company.verificada = True
			company.save()

			for telefone in telefones:
				telefone.delete()

			for  f  in formset:
				phone = f.cleaned_data
				if phone:
					telempresa = TelefoneEmpresa()
					telempresa.id_tipo_telefone =  phone.get('tipo_telefone')
					telempresa.id_empresa = company
					telempresa.numero =  phone.get('numero')
					telempresa.ramal =  phone.get('ramal')
					telempresa.nome_contato = phone.get('nome_contato')
					telempresa.save()
			
			agencia.id_empresa = company
			agencia.logo = request.FILES.get('logo', None)
			agencia.save()

			return redirect(reverse_lazy("agencia-list"))
		context = {'form':form, 'formset':formset}
		return render (request, 'subclasses/empresa/agencia/edit.html', context)



class AgenciaList(JSONResponseMixin,ListView):
	model = Agencia
	template_name = 'subclasses/empresa/agencia/list.html'

	def get_context_data(self, **kwargs):
		context = super(AgenciaList, self).get_context_data(**kwargs)
		return context      


class AgenciaDetail(JSONResponseMixin,DetailView):
	model = Agencia
	template_name = 'subclasses/empresa/agencia/detail.html'

	def get_context_data(self, **kwargs):
		context = super(AgenciaDetail, self).get_context_data(**kwargs)
		return context


class AgenciaDelete(JSONResponseMixin,DeleteView):
	model = Empresa
	success_url = reverse_lazy('agencia-list')
	template_name = 'subclasses/empresa/agencia/delete.html'

