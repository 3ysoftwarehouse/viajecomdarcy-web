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

from apps.default.models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneUsuario, TipoUsuario, Genero,TipoDocumento, Documento 
from .models import Passageiro 
from apps.subclasses.empresa.escola.models import Escola 
from .forms import PassageiroRegisterForm, DocumentoForm, RequiredFormSet
from apps.default.forms import PhoneForm 
from apps.default.views import JSONResponseMixin
from apps.subclasses.usuario.emissor.views import get_emissor
from apps.subclasses.empresa.escola.forms import EscolaRegisterForm


class PassageiroRegister(JSONResponseMixin,View):
	def get(self, request):
		form = PassageiroRegisterForm		
		PhoneFormSet = formset_factory(PhoneForm)
		formset = PhoneFormSet(prefix='phone')
		form_escola = EscolaRegisterForm(prefix='escola')
		formset2 = PhoneFormSet(prefix='phone2')
		DocFormSet = formset_factory(DocumentoForm, formset=RequiredFormSet)
		doc_formset = DocFormSet(prefix='doc')
		request.session["view"]="passageiro"
		context = {'form':form, 'formset':formset, 'form_escola':form_escola, 'formset2':formset2, 'doc_formset':doc_formset}
		return render(request, 'subclasses/usuario/passageiro/register.html', context)

	def post(self, request, *args, **kwargs):
		form = PassageiroRegisterForm(request.POST,request.FILES)
		PhoneFormSet = formset_factory(PhoneForm)		
		formset = PhoneFormSet(request.POST, request.FILES, prefix='phone')
		DocFormSet = formset_factory(DocumentoForm,formset=RequiredFormSet)
		doc_formset = DocFormSet(request.POST, request.FILES, prefix='doc')
		request.session["view"]="passageiro"
		try:
			request.POST['data_nascimento'] = datetime.strptime(request.POST['data_prevista'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		try:
			request.POST['data_validade_passaporte'] = datetime.strptime(request.POST['data_validade_passaporte'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		if form.is_valid() and formset.is_valid() and doc_formset.is_valid():
			emissor = get_emissor(self)
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

			for  f  in doc_formset:
				doc = f.cleaned_data
				if doc.get('id_tipo_documento') and doc.get('anexo'):
					documento = Documento()
					documento.id_usuario = usuario
					documento.id_tipo_documento = doc.get('id_tipo_documento')
					documento.anexo = doc.get('anexo')
					documento.save()

			passageiro = Passageiro()
			passageiro.id_escola = form.cleaned_data.get("id_escola")
			passageiro.id_usuario = usuario
			passageiro.matricula = form.cleaned_data.get("matricula")
			passageiro.natularidade = form.cleaned_data.get("natularidade")
			passageiro.observacao = form.cleaned_data.get("observacao")
			passageiro.numero_passaporte = form.cleaned_data.get("numero_passaporte")
			passageiro.data_validade_passaporte = form.cleaned_data.get("data_validade_passaporte")

			passageiro.nome_pai = form.cleaned_data.get("nome_pai")
			passageiro.nome_mae = form.cleaned_data.get("responsavel")
			passageiro.responsavel = form.cleaned_data.get("observacao")
			passageiro.telefone_responsavel = form.cleaned_data.get("telefone_responsavel")
			passageiro.email_responsavel = form.cleaned_data.get("email_responsavel")

			if emissor:
				passageiro.id_emissor = emissor
				passageiro.id_agencia = emissor.id_agencia
			passageiro.save()

			return redirect(reverse_lazy("passageiro-list"))

		context = {'form':form, 'formset':formset, 'doc_formset':doc_formset}
		return render(request, 'subclasses/usuario/passageiro/register.html', context)


class PassageiroEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		passageiro = Passageiro.objects.get(pk=pk)
		usuario = Usuario.objects.get(pk=passageiro.id_usuario.pk)
		telefones = TelefoneUsuario.objects.filter(id_usuario=usuario.pk).extra(select={'tipo_telefone': 'id_tipo_telefone_id'}).values('tipo_telefone', 'numero')
		documentos = Documento.objects.filter(id_usuario=usuario.pk).values('id_tipo_documento', 'anexo')
		extra = 1

		form = PassageiroRegisterForm(instance=usuario)
		form.initial['id_escola'] = passageiro.id_escola
		form.initial['matricula'] = passageiro.matricula
		form.initial['natularidade'] = passageiro.natularidade
		form.initial['observacao'] = passageiro.observacao
		form.initial['numero_passaporte'] = passageiro.numero_passaporte
		form.initial['data_validade_passaporte'] = passageiro.data_validade_passaporte
		
		form.initial['nome_pai'] = passageiro.nome_pai
		form.initial['nome_mae'] = passageiro.nome_mae
		form.initial['responsavel'] = passageiro.responsavel
		form.initial['telefone_responsavel'] = passageiro.telefone_responsavel
		form.initial['email_responsavel'] = passageiro.email_responsavel

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
		if documentos:
			extra = 0
		DocFormSet = formset_factory(DocumentoForm, extra=extra, formset=RequiredFormSet, can_delete=True)
		doc_formset = DocFormSet(prefix='doc', initial=documentos)

		request.session["view"]="passageiro"
		context = {'form':form, 'formset':formset, 'doc_formset':doc_formset}
		return render(request, 'subclasses/usuario/passageiro/edit.html', context)

	def post(self, request, pk, *args, **kwargs):
		passageiro = Passageiro.objects.get(pk=pk)
		user = Usuario.objects.get(pk=passageiro.id_usuario.pk)
		telefones = TelefoneUsuario.objects.filter(id_usuario=user.pk)
		documentos = Documento.objects.filter(id_usuario=user.pk)
		extra = 1
		form = PassageiroRegisterForm(request.POST, request.FILES, instance=user)
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(request.POST, request.FILES)
		if telefones:
			documentos = 0
		DocFormSet = formset_factory(DocumentoForm)
		doc_formset = DocFormSet(request.POST, request.FILES, prefix='doc')
		request.session["view"]="passageiro"
		try:
			request.POST['data_nascimento'] = datetime.strptime(request.POST['data_prevista'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		try:
			request.POST['data_validade_passaporte'] = datetime.strptime(request.POST['data_validade_passaporte'], '%d/%m/%Y').strftime('%Y-%m-%d')    
		except:
			pass
		if form.is_valid() and formset.is_valid() and doc_formset.is_valid():
			emissor = get_emissor(self)
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
			usuario.id_tipo_usuario = TipoUsuario.objects.get_or_create(descricao="CLIENTE")[0]
			usuario.nomecompleto = form.cleaned_data.get("nome")
			usuario.save()

			for telefone in telefones:
				telefone.delete()


			

			for value in request.POST.getlist('deletar_anexo'):
				doc = Documento.objects.filter(anexo=value)
				doc.delete()

			for  f  in formset:
				phone = f.cleaned_data
				if phone:
					teluser = TelefoneUsuario()
					teluser.id_tipo_telefone =  phone.get('tipo_telefone')
					teluser.id_usuario = usuario
					teluser.numero =  phone.get('numero')
					teluser.save()

			for  f  in doc_formset:
				doc = f.cleaned_data
				if doc.get('id_tipo_documento') and doc.get('anexo'):
					documento = Documento()
					documento.id_usuario = usuario
					documento.id_tipo_documento = doc.get('id_tipo_documento')
					documento.anexo = doc.get('anexo')
					documento.save()


			passageiro.id_escola = form.cleaned_data.get("id_escola")
			passageiro.id_usuario = usuario
			passageiro.matricula = form.cleaned_data.get("matricula")
			passageiro.natularidade = form.cleaned_data.get("natularidade")
			passageiro.observacao = form.cleaned_data.get("observacao")
			passageiro.numero_passaporte = form.cleaned_data.get("numero_passaporte")
			passageiro.data_validade_passaporte = form.cleaned_data.get("data_validade_passaporte")

			passageiro.nome_pai = form.cleaned_data.get("nome_pai")
			passageiro.nome_mae = form.cleaned_data.get("responsavel")
			passageiro.responsavel = form.cleaned_data.get("observacao")
			passageiro.telefone_responsavel = form.cleaned_data.get("telefone_responsavel")
			passageiro.email_responsavel = form.cleaned_data.get("email_responsavel")

			if emissor:
				passageiro.id_emissor = emissor
				passageiro.id_agencia = emissor.id_agencia
			passageiro.save()

			return redirect(reverse_lazy("passageiro-list"))

		context = {'form':form, 'formset':formset}
		return render(request, 'subclasses/usuario/passageiro/edit.html', context)



class PassageiroList(JSONResponseMixin,ListView):
	queryset = Passageiro.objects.all()
	template_name = 'subclasses/usuario/passageiro/list.html'

	def get_context_data(self, **kwargs):

		context = super(PassageiroList, self).get_context_data(**kwargs)
		emissor = get_emissor(self)
		if emissor:
			passageiros = Passageiro.objects.filter(id_agencia=emissor.id_agencia.pk)
		else:
			passageiros = Passageiro.objects.all()
		lists = []

		for value in passageiros:
			telefone = TelefoneUsuario.objects.filter(id_usuario=value.id_usuario)
			if telefone:
				lists.append([value,telefone[0]])
			else:
				lists.append([value,telefone])

		context["passageiros"] = lists

		return context


class PassageiroDetail(JSONResponseMixin,DetailView):
	model = Passageiro
	template_name = 'subclasses/usuario/passageiro/detail.html'

	def get_context_data(self, **kwargs):
		context = super(PassageiroDetail, self).get_context_data(**kwargs)
		return context


class PassageiroDelete(JSONResponseMixin,DeleteView):
	model = Usuario
	success_url = reverse_lazy('passageiro-list')
	template_name = 'subclasses/usuario/passageiro/delete.html'

'''
----------------------------------------
			END PASSAGEIRO METHODS
----------------------------------------
'''