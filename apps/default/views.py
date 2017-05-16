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

from .models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneUsuario, TelefoneEmpresa, Genero, TipoUsuario 
from .forms import LoginForm, RegisterForm 
from .forms import ProfileForm 
from .forms import UserRegisterForm 
from .forms import CompanyRegisterForm
from .forms import PhoneForm 
import requests
import re

class JSONResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        return context


class Register(JSONResponseMixin,View):
	def get(self, request):
		form = RegisterForm
		return render (request, 'default/register.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = RegisterForm(request.POST)
			
			nome = request.POST['nome']
			sobrenome = request.POST['sobrenome']
			email = request.POST['email']
			password = request.POST['password']
			
			if not nome:
				context['error_msg'] = 'nome cannot be empty !'
			if not sobrenome:
				context['error_msg'] = 'sobrenome cannot be empty !'
			if not email:
				context['error_msg'] = 'email cannot be empty !'
			if not password:
				context['error_msg'] = 'password cannot be empty !'

			if not context:
				user = Usuario.objects.create_user(email, password)
				user.nome = nome
				user.sobrenome = sobrenome
				usuario.is_active =  True
				user.save()
				return redirect(reverse_lazy("home"))

			else:
				form = RegisterForm()

		return render(request, 'default/register.html', {'form': form})


class Login(JSONResponseMixin,View):
	def get(self, request):
		form = LoginForm
		return render (request, 'default/login.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = LoginForm(request.POST)
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect(reverse_lazy("home"))
				else:
					context['error'] = "Usuario não ativo"
					return render(request, 'default/login.html',{'form':form,'context':context})
			else:
				context['error'] = "Usuário não cadastrado"
				return render(request, 'default/login.html',{'form':form,'context':context})
		else:
		    form = LoginForm()

		return render(request, 'default/login.html', {'form': form})


class Logout(JSONResponseMixin, View):
	def get(self, request):
		logout(request)
		return redirect('/')


class Dashboard(JSONResponseMixin, View):
	def get(self, request):
		return render (request, 'default/dashboard.html')


class Profile(JSONResponseMixin,UpdateView):
	form_class = ProfileForm
	template_name = 'default/profile.html'
	success_url = reverse_lazy("profile")

	def get_object(self, queryset=None):
		return self.request.user


class UserRegister(JSONResponseMixin,View):
	def get(self, request):
		form = UserRegisterForm
		formset = formset_factory(PhoneForm)
		request.session["view"]="usuario"
		context = {'form':form, 'formset':formset}
		return render (request, 'default/user/register.html', context)

	def post(self, request, *args, **kwargs):
		form = UserRegisterForm(request.POST, request.FILES)
		PhoneFormSet = formset_factory(PhoneForm)		
		formset = PhoneFormSet(request.POST, request.FILES)
		request.session["view"]="usuario"
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
			usuario.set_password(form.cleaned_data.get("password"))
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

			return redirect(reverse_lazy("user-list"))

		context = {'form':form, 'formset':formset}
		return render(request, 'default/user/register.html', context)


class UserEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		usuario = Usuario.objects.get(pk=pk)
		telefones = TelefoneUsuario.objects.filter(id_usuario=pk).extra(select={'tipo_telefone': 'id_tipo_telefone_id'}).values('tipo_telefone', 'numero')
		extra = 1

		form = UserRegisterForm(instance=usuario)
		form.fields['password'].required = False
		form.initial['password'] = None
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

		request.session["view"]="usuario"
		context = {'form':form, 'formset':formset}
		return render (request, 'default/user/register.html', context)

	def post(self, request, pk, *args, **kwargs):
		user = Usuario.objects.get(pk=pk)
		telefones = TelefoneUsuario.objects.filter(id_usuario=pk)
		extra = 1
		form = UserRegisterForm(request.POST, request.FILES, instance=user)
		form.fields['password'].required = False
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(request.POST, request.FILES)
		request.session["view"]="usuario"
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
			if form.cleaned_data.get("password"):
				usuario.set_password(form.cleaned_data.get("password"))
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

			return redirect(reverse_lazy("user-list"))

		context = {'form':form, 'formset':formset}
		return render(request, 'default/user/register.html', context)


class UserList(JSONResponseMixin,ListView):
	queryset = Usuario.objects.filter(is_admin=False).filter(is_active=True)
	template_name = 'default/user/list.html'

	def get_context_data(self, **kwargs):
		context = super(UserList, self).get_context_data(**kwargs)
		return context


class UserDetail(JSONResponseMixin,DetailView):
	model = Usuario
	template_name = 'default/user/detail.html'

	def get_context_data(self, **kwargs):
		context = super(UserDetail, self).get_context_data(**kwargs)
		return context


class UserDelete(JSONResponseMixin,DeleteView):
	model = Usuario
	success_url = reverse_lazy('user-list')
	template_name = 'default/user/delete.html'


'''
----------------------------------------
			END USER METHODS
----------------------------------------
'''



'''
----------------------------------------
			COMPANY METHODS
----------------------------------------
'''

def validaCNPJ(cnpj):
	empresa = Empresa.objects.filter(cnpj=cnpj)
	if empresa:
		return True

	cnpj = ''.join(re.findall('\d', str(cnpj)))

	if (not cnpj) or (len(cnpj) < 14):
	    return True

	# Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
	inteiros = list(map(int, cnpj))
	novo = inteiros[:12]

	prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
	while len(novo) < 14:
	    r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
	    if r > 1:
	        f = 11 - r
	    else:
	        f = 0
	    novo.append(f)
	    prod.insert(0, 6)

	# Se o número gerado coincidir com o número original, é válido
	if novo == inteiros:
	    return False
	else:
		return True
    


class CompanyRegister(JSONResponseMixin,View):
	def get(self, request):
		form = CompanyRegisterForm
		PhoneFormSet = formset_factory(PhoneForm)
		formset = PhoneFormSet()
		request.session["view"]=""		
		context = {'form':form, 'formset':formset}
		return render(request, 'default/company/register.html', context)

	def post(self, request, *args, **kwargs):
		form = CompanyRegisterForm(request.POST, request.FILES)
		PhoneFormSet = formset_factory(PhoneForm)		
		formset = PhoneFormSet(request.POST, request.FILES)
		request.session["view"]=""		
		context = {'form':form, 'formset':formset}
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

			return redirect(reverse_lazy("company-list"))
		
		context = {'form':form, 'formset':formset}
		return render(request, 'default/company/register.html', context)


class CompanyEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		empresa = Empresa.objects.get(pk=pk)
		telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk).extra(select={'tipo_telefone': 'id_tipo_telefone_id'}).values('tipo_telefone', 'numero', 'ramal','nome_contato')
		extra = 1

		form = CompanyRegisterForm(instance=empresa)
		form.initial['cep'] = empresa.id_endereco.id_logradouro.cep if empresa.id_endereco else ''
		form.initial['rua'] = empresa.id_endereco.id_logradouro.nome if empresa.id_endereco else ''
		form.initial['bairro'] = empresa.id_endereco.id_logradouro.bairro if empresa.id_endereco else ''
		form.initial['cidade'] = empresa.id_endereco.id_logradouro.cidade if empresa.id_endereco else ''
		form.initial['estado'] = empresa.id_endereco.id_logradouro.estado if empresa.id_endereco else ''
		form.initial['pais'] = empresa.id_endereco.id_logradouro.pais if empresa.id_endereco else ''
		form.initial['numeroed'] = empresa.id_endereco.numero if empresa.id_endereco else ''
		form.initial['complemento'] = empresa.id_endereco.complemento if empresa.id_endereco else ''
		form.initial['pontoreferencia'] = empresa.id_endereco.pontoreferencia if empresa.id_endereco else ''
		if telefones:
			extra = 0
		PhoneFormSet = formset_factory(PhoneForm, extra=extra)
		formset = PhoneFormSet(initial=telefones)
		request.session["view"]=""		
		context = {'form':form, 'formset':formset}
		return render (request, 'default/company/edit.html', context)

	def post(self, request, pk, *args, **kwargs):
		empresa = Empresa.objects.get(pk=pk)
		telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk)
		extra = 1

		form = CompanyRegisterForm(request.POST, request.FILES, instance=empresa)
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
			

			return redirect(reverse_lazy("company-list"))
		context = {'form':form, 'formset':formset}
		return render (request, 'default/company/edit.html', context)


class CompanyList(JSONResponseMixin,ListView):
	model = Empresa
	template_name = 'default/company/list.html'

	def get_context_data(self, **kwargs):
		context = super(CompanyList, self).get_context_data(**kwargs)
		return context      


class CompanyDetail(JSONResponseMixin,DetailView):
	model = Empresa
	template_name = 'default/company/detail.html'

	def get_context_data(self, **kwargs):
		context = super(CompanyDetail, self).get_context_data(**kwargs)
		return context


class CompanyDelete(JSONResponseMixin,DeleteView):
	model = Empresa
	success_url = reverse_lazy('company-list')
	template_name = 'default/user/delete.html'

'''
----------------------------------------
			END COMPANY METHODS
----------------------------------------
'''    


'''
----------------------------------------
			API'S INTEGRATION
----------------------------------------
'''
def get_cnpj_json(request):
	if request.method == 'GET':
		response = requests.get('http://receitaws.com.br/v1/cnpj/' + request.GET.get('cnpj')).json()
	return JsonResponse(response)

def get_cep_json(request):
	if request.method == 'GET':
		response = requests.get(
			'http://www.cepaberto.com/api/v2/ceps.json?cep=' + request.GET.get('cep'),
			headers={'Authorization': 'Token token=055cc8e8b0e25d6b6bb30a6dad8b1932'}
			).json()
	return JsonResponse(response)
