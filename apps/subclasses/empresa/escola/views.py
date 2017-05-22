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

from apps.default.models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneEmpresa # MODELS
from .forms import EscolaRegisterForm
from apps.default.forms import PhoneForm 
from apps.default.views import JSONResponseMixin, validaCNPJ
from .models import Escola


class EscolaRegister(JSONResponseMixin,View):
	def get(self, request):
		form = EscolaRegisterForm
		PhoneFormSet = formset_factory(PhoneForm)
		formset = PhoneFormSet()
		request.session["view"]="escola"		
		context = {'form':form, 'formset':formset}
		return render (request, 'subclasses/empresa/escola/register.html', context)

	def post(self, request, *args, **kwargs):
		if request.POST.get('is_modal'):
			form = EscolaRegisterForm(request.POST, request.FILES, prefix="escola")
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES, prefix="phone2")
		else:
			form = EscolaRegisterForm(request.POST, request.FILES)
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

			company.id_tipo_empresa =  TipoEmpresa.objects.get_or_create(descricao = "Escola")[0]
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

			escola = Escola()
			escola.id_empresa = company
			escola.save()

			if request.POST.get('is_modal'):
				return JsonResponse({'status':'success', 'id_escola':escola.pk, 'nomefantasia': escola.id_empresa.nomefantasia})
			else:
				return redirect(reverse_lazy("escola-list"))
		
		context = {'form':form, 'formset':formset}
		return render (request, 'subclasses/empresa/escola/register.html', context)


class EscolaEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		escola = Escola.objects.get(pk=pk)
		empresa = Empresa.objects.get(pk=escola.id_empresa.pk)
		telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk).extra(select={'tipo_telefone': 'id_tipo_telefone_id'}).values('tipo_telefone', 'numero', 'ramal','nome_contato')
		extra = 1

		form = EscolaRegisterForm(instance=empresa)
		form.initial['cep'] = escola.id_empresa.id_endereco.id_logradouro.cep if escola.id_empresa.id_endereco else ''
		form.initial['rua'] = escola.id_empresa.id_endereco.id_logradouro.nome if escola.id_empresa.id_endereco else ''
		form.initial['bairro'] = escola.id_empresa.id_endereco.id_logradouro.bairro if escola.id_empresa.id_endereco else ''
		form.initial['cidade'] = escola.id_empresa.id_endereco.id_logradouro.cidade if escola.id_empresa.id_endereco else ''
		form.initial['estado'] = escola.id_empresa.id_endereco.id_logradouro.estado if escola.id_empresa.id_endereco else ''
		form.initial['pais'] = escola.id_empresa.id_endereco.id_logradouro.pais if escola.id_empresa.id_endereco else ''
		form.initial['numeroed'] = escola.id_empresa.id_endereco.numero if escola.id_empresa.id_endereco else ''
		form.initial['complemento'] = escola.id_empresa.id_endereco.complemento if escola.id_empresa.id_endereco else ''
		form.initial['pontoreferencia'] = escola.id_empresa.id_endereco.pontoreferencia if escola.id_empresa.id_endereco else ''
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(initial=telefones)
		request.session["view"]="escola"		
		context = {'form':form, 'formset':formset}
		return render (request, 'subclasses/empresa/escola/edit.html', context)

	def post(self, request, pk, *args, **kwargs):
		escola = Escola.objects.get(pk=pk)
		empresa = Empresa.objects.get(pk=escola.id_empresa.pk)
		telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk)
		extra = 1

		form = EscolaRegisterForm(request.POST, request.FILES, instance=empresa)
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

			company.id_tipo_empresa =  TipoEmpresa.objects.get_or_create(descricao = "Escola")[0]
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
			
			escola.id_empresa = company
			escola.save()

			return redirect(reverse_lazy("escola-list"))
		context = {'form':form, 'formset':formset}
		return render (request, 'subclasses/empresa/escola/edit.html', context)




class EscolaList(JSONResponseMixin,ListView):
	model = Escola
	template_name = 'subclasses/empresa/escola/list.html'

	def get_context_data(self, **kwargs):
		context = super(EscolaList, self).get_context_data(**kwargs)
		return context 


class EscolaDetail(JSONResponseMixin,DetailView):
	model = Escola
	template_name = 'subclasses/empresa/escola/detail.html'

	def get_context_data(self, **kwargs):
		context = super(EscolaDetail, self).get_context_data(**kwargs)
		return context		


class EscolaDelete(JSONResponseMixin,DeleteView):
	model = Empresa
	success_url = reverse_lazy('escola-list')
	template_name = 'subclasses/empresa/escola/delete.html'

'''
----------------------------------------
			END ESCOLA METHODS
----------------------------------------
'''
