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

from apps.default.models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneUsuario, TipoUsuario, Genero 
from .models import Emissor
from apps.subclasses.empresa.agencia.models import Agencia 
from .forms import EmissorRegisterForm
from apps.default.forms import PhoneForm 
from apps.default.views import JSONResponseMixin
from datetime import datetime, timedelta




def get_emissor(self):
	emissor = []
	try:
		emissor = Emissor.objects.get(id_usuario=self.request.user.pk)
		return emissor
	except:
		return emissor
		pass

class EmissorRegister(JSONResponseMixin,View):
	def get(self, request):
		form = EmissorRegisterForm
		formset = formset_factory(PhoneForm)
		request.session["view"]="emissor"
		context = {'form':form, 'formset':formset}
		return render(request, 'subclasses/usuario/emissor/register.html', context)

	def post(self, request, *args, **kwargs):
		form = EmissorRegisterForm(request.POST, request.FILES)
		PhoneFormSet = formset_factory(PhoneForm)		
		formset = PhoneFormSet(request.POST, request.FILES)
		request.session["view"]="emissor"
		try:
			request.POST['data_nascimento'] = datetime.strptime(request.POST['data_prevista'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		if form.is_valid() and formset.is_valid():
			usuario = form.save(commit=False)

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

			usuario.id_endereco = id_endereco
			usuario.is_active = True
			usuario.id_tipo_usuario = TipoUsuario.objects.get_or_create(descricao="EMISSOR")[0]
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

			emissor = Emissor()
			emissor.id_usuario = usuario
			emissor.id_agencia = form.cleaned_data.get("id_agencia")
			emissor.save()

			return redirect(reverse_lazy("emissor-list"))

		context = {'form':form, 'formset':formset}
		return render(request, 'subclasses/usuario/emissor/register.html', context)

		


class EmissorEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		emissor = Emissor.objects.get(pk=pk)
		usuario = Usuario.objects.get(pk=emissor.id_usuario.pk)
		telefones = TelefoneUsuario.objects.filter(id_usuario=usuario.pk).extra(select={'tipo_telefone': 'id_tipo_telefone_id'}).values('tipo_telefone', 'numero')
		extra = 1

		form = EmissorRegisterForm(instance=usuario)
		form.initial['id_agencia'] = emissor.id_agencia
		form.initial['cep'] = usuario.id_endereco.id_logradouro.cep if usuario.id_endereco else ''
		form.initial['rua'] = usuario.id_endereco.id_logradouro.nome if usuario.id_endereco else ''
		form.initial['bairro'] = usuario.id_endereco.id_logradouro.bairro if usuario.id_endereco else ''
		form.initial['cidade'] = usuario.id_endereco.id_logradouro.cidade if usuario.id_endereco else ''
		form.initial['estado'] = usuario.id_endereco.id_logradouro.estado if usuario.id_endereco else ''
		form.initial['pais'] = usuario.id_endereco.id_logradouro.pais if usuario.id_endereco else ''
		form.initial['numero'] = usuario.id_endereco.numero if usuario.id_endereco else ''
		form.initial['complemento'] = usuario.id_endereco.complemento if usuario.id_endereco else ''
		form.initial['pontoreferencia'] = usuario.id_endereco.pontoreferencia if usuario.id_endereco else ''
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(initial=telefones)

		request.session["view"]="emissor"
		context = {'form':form, 'formset':formset}
		return render(request, 'subclasses/usuario/emissor/edit.html', context)

	def post(self, request, pk, *args, **kwargs):
		emissor = Emissor.objects.get(pk=pk)
		user = Usuario.objects.get(pk=emissor.id_usuario.pk)
		telefones = TelefoneUsuario.objects.filter(id_usuario=user.pk)
		extra = 1
		form = EmissorRegisterForm(request.POST, request.FILES, instance=user)
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(request.POST, request.FILES)
		request.session["view"]="emissor"
		try:
			request.POST['data_nascimento'] = datetime.strptime(request.POST['data_prevista'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		if form.is_valid() and formset.is_valid():
			usuario = form.save(commit=False)

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

			usuario.id_endereco = id_endereco
			usuario.is_active = True
			usuario.id_tipo_usuario = TipoUsuario.objects.get_or_create(descricao="EMISSOR")[0]
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

			emissor.id_usuario = usuario
			emissor.id_agencia = form.cleaned_data.get("id_agencia")
			emissor.save()

			return redirect(reverse_lazy("emissor-list"))

		context = {'form':form, 'formset':formset}
		return render(request, 'subclasses/usuario/emissor/edit.html', context)



class EmissorList(JSONResponseMixin,ListView):
	queryset = Emissor.objects.all()
	template_name = 'subclasses/usuario/emissor/list.html'

	def get_context_data(self, **kwargs):

		context = super(EmissorList, self).get_context_data(**kwargs)
		emissores = Emissor.objects.all()
		lists = []

		for value in emissores:
			telefone = TelefoneUsuario.objects.filter(id_usuario=value.id_usuario)
			if telefone:
				lists.append([value,telefone[0]])
			else:
				lists.append([value,telefone])

		context["emissores"] = lists

		return context


class EmissorDetail(JSONResponseMixin,DetailView):
	model = Emissor
	template_name = 'subclasses/usuario/emissor/detail.html'

	def get_context_data(self, **kwargs):
		context = super(EmissorDetail, self).get_context_data(**kwargs)
		return context


class EmissorDelete(JSONResponseMixin,DeleteView):
	model = Usuario
	success_url = reverse_lazy('emissor-list')
	template_name = 'subclasses/usuario/emissor/delete.html'

'''
----------------------------------------
			END EMISSOR METHODS
----------------------------------------
'''